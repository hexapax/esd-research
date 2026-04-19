#!/usr/bin/env python3
"""Classify ESD incidents as freshwater private dock vs. freshwater marina.

Reads classifier_input.json, applies heuristics, writes classifier_output.json.

Decision order per record:
  1. If water_type != "fresh" → both False (high confidence).
  2. If the record describes a non-dock electrocution (pool, fountain, overhead
     power line, flooded basement/street, irrigation, construction site, etc.)
     → both False.
  3. Look at facility_name:
     - explicit private-dock phrase → private = True (high).
     - explicit marina / yacht-club / boat-club / harbor / boat-works → marina
       = True (high). Guard against false hits like "Harbor Road" or a
       subdivision name; the keyword must describe a facility.
  4. Fall back to narrative (notes + body):
     - strong private cue ("private dock", "lakehouse", "family's dock",
       "at their lake home", "neighbor's dock", "parents' home on Lake X")
       → private = True (high or medium depending on explicitness).
     - strong marina cue ("at X Marina", "marina slip", "moored at the marina",
       facility mentioned without qualifier like "at a marina") → marina = True.
     - mere proximity to a marina ("near Capital Cove Marina", "marina
       infrastructure", "not a dock/marina ESD") → no flag.
  5. Otherwise → both False (confidence low if unclear, medium if public dock).
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

INPUT = Path("/opt/repos/esd-research/analysis/classifier_input.json")
OUTPUT = Path("/opt/repos/esd-research/analysis/classifier_output.json")


# --- Regex helpers -----------------------------------------------------------

FACILITY_PRIVATE = re.compile(
    r"\b("
    r"private\s+(?:[\w-]+\s+){0,3}?(?:dock|pier|boathouse|boat\s+house)"
    r"|family\s+(?:[\w'-]+\s+){0,2}?(?:dock|pier|boathouse|lakehouse|lake\s+home)"
    r"|family[''`]?s\s+(?:[\w'-]+\s+){0,2}?(?:dock|pier|boathouse|lakehouse|lake\s+home)"
    r"|lakehouse\s+dock"
    r"|lake\s+home\s+dock"
    r"|backyard\s+dock"
    r"|residential\s+dock"
    r"|home\s+dock"
    r"|neighbor[''`]?s\s+dock"
    r"|privately[- ]owned\s+(?:dock|pier|boathouse)"
    r"|rental\s+property\s+(?:dock|pier|boathouse)"
    r")\b",
    re.IGNORECASE,
)

FACILITY_MARINA = re.compile(
    r"\b("
    r"marina"                        # any occurrence in facility name
    r"|yacht\s+club"
    r"|boat\s+club"
    r"|boat\s+works"
    r"|boatworks"
    r"|boat\s+basin"
    r"|boat\s+harbor"
    r"|boat\s+harbour"
    r"|\w+\s+harbor"                 # "Racine Harbor", "International Harbor"
    r"|\w+\s+harbour"
    r"|\w+\s+marine$"                # "Lou Wendell Marine" — commercial marina
    r")\b",
    re.IGNORECASE,
)

# Facility-name "Harbor" used as a marina (e.g., "Main Harbor Marina",
# "Racine Harbor", "International Harbor"). Avoid generic addresses like
# "Harbor Road" or "Harbor Drive".
FACILITY_HARBOR = re.compile(
    r"\b(\w+\s+Harbor|Harbor)\b(?!\s*(?:Road|Rd\.?|Drive|Dr\.?|Street|St\.?|Avenue|Ave\.?|Boulevard|Blvd\.?|Lane|Ln\.?))",
    re.IGNORECASE,
)

# In narrative — "at a marina", "at the marina", "at X Marina", "marina slip/pier/dock"
NARRATIVE_MARINA = re.compile(
    r"\b(?:"
    r"at\s+(?:a|the|an)\s+marina\b"
    r"|at\s+[A-Z][\w']+(?:\s+[A-Z][\w']+){0,4}\s+Marina\b"
    r"|marina\s+(?:manager|slip|pier|dock|pedestal)"
    r"|moored\s+at\s+(?:a|the)?\s*\w*\s*marina"
    r"|drowned\s+at\s+a\s+marina"
    r"|at\s+(?:a|the)\s+yacht\s+club"
    r"|yacht\s+club\s+(?:dock|slip|pier)"
    r"|at\s+(?:a|the)\s+boat\s+club"
    r")\b",
    re.IGNORECASE,
)

NARRATIVE_PRIVATE = re.compile(
    r"\b("
    r"private\s+(?:\w+\s+){0,3}?(?:dock|pier|boathouse|boat\s+house)"
    r"|lakehouse\s+dock"
    r"|lake\s+(?:home|house|cabin)\s+(?:dock|pier|boathouse)"
    r"|backyard\s+dock"
    r"|residential\s+dock"
    r"|neighbor[''`]?s\s+(?:dock|pier|boathouse|boat\s+hoist|boat\s+lift)"
    r"|family[''`]?s\s+(?:dock|pier|boathouse|lake\s+home|lake\s+house|lake\s+cabin)"
    r"|(?:his|her|their)\s+(?:parents[''`]?|family[''`]?s?)\s+(?:home|lake\s+home|lake\s+house|lake\s+place|property)"
    r"|(?:at|to|from)\s+(?:the\s+)?victim[''`]?s?\s+(?:home|dock|lake\s+home|lake\s+house)"
    r")\b",
    re.IGNORECASE,
)

# Weaker private-dock cues: "at his parents' home", "at the family lake home"
NARRATIVE_PRIVATE_WEAK = re.compile(
    r"\b("
    r"(?:his|her|their)\s+parents[''`]?\s+(?:home|house|property|lake\s+home|cabin)"
    r"|(?:his|her|their)\s+family[''`]?s?\s+(?:lake\s+home|lake\s+house|lakehouse|cabin|vacation\s+home)"
    r"|at\s+(?:his|her|their)\s+(?:lake\s+home|lake\s+house|lakehouse|vacation\s+home|cabin)"
    r")\b",
    re.IGNORECASE,
)

# Non-dock electrocution contexts — these override any keyword matches
NON_DOCK_STRONG = re.compile(
    r"\b("
    r"swimming\s+pool"
    r"|flooded\s+basement"
    r"|flooded\s+laundry"
    r"|flooded\s+street"
    r"|flooded\s+field"
    r"|flooded\s+apartment"
    r"|floodwater"
    r"|fountain"
    r"|overhead\s+(?:power|transmission)\s+line"
    r"|downed\s+power\s+line"
    r"|extension\s+cord"
    r"|irrigation\s+(?:canal|pump|pivot|system|meter)"
    r"|cornfield"
    r"|corn\s+field"
    r"|center\s+pivot"
    r"|construction\s+site"
    r"|concrete\s+saw"
    r"|sump\s+pump"
    r"|wave\s+pool"
    r"|waterpark"
    r"|hurricane\s+\w+\s+floodwater"
    r"|tropical\s+storm\s+\w+\s+floodwater"
    r"|sandbag"
    r"|bollard\s+light"
    r"|sailboat\s+mast"
    r"|mast\s+struck"
    r"|mast\s+contacted"
    r"|fire\s+hydrant"
    r"|car\s+crash"
    r")\b",
    re.IGNORECASE,
)

# Phrases meaning "this is NOT a marina/dock case"
EXPLICIT_NOT_MARINA = re.compile(
    r"\b(?:"
    r"not\s+(?:a\s+)?(?:classic\s+)?dock[\/\s-]*marina"
    r"|non[- ]marina\s+context"
    r"|not\s+(?:a\s+)?dock[\/\s-]*marina"
    r"|esd[- ]adjacent"
    r"|not\s+(?:a\s+)?classic\s+esd"
    r"|rather\s+than\s+commercial\s+marina"
    r"|rather\s+than\s+(?:a\s+)?marina"
    r"|not\s+in\s+(?:a\s+)?marina"
    r")",
    re.IGNORECASE,
)

# Phrases that downgrade to "mere proximity / area reference"
PROXIMITY_ONLY = re.compile(
    r"\b(?:"
    r"near\s+\w*\s*marina\s+(?:area|infrastructure)"
    r"|with\s+\w*\s*marina\s+infrastructure"
    r"|major\s+marina\s+infrastructure"
    r"|marina\s+area"
    r"|likely\s+\w+\s+\(.*marina"     # "Likely location is Bolling AFB (Capital Cove Marina area)"
    r")\b",
    re.IGNORECASE,
)


def text_bundle(rec: dict) -> dict[str, str]:
    return {
        "facility": rec.get("facility_name") or "",
        "body": rec.get("body_of_water") or "",
        "elec": rec.get("electrical_source") or "",
        "fault": rec.get("fault_description") or "",
        "notes": rec.get("notes") or "",
        "research_notes": rec.get("research_notes") or "",
        "body_md": rec.get("body") or "",
    }


def any_match(pattern: re.Pattern, *strings: str) -> str | None:
    """Return the first non-overlapping match text across the strings, or None."""
    for s in strings:
        m = pattern.search(s)
        if m:
            return m.group(0)
    return None


def classify(rec: dict) -> dict:
    inc_id = rec["incident_id"]
    water_type = (rec.get("water_type") or "").lower().strip()
    tb = text_bundle(rec)
    facility = tb["facility"]
    narrative = " ".join([tb["notes"], tb["research_notes"], tb["body_md"], tb["fault"]])
    # Strip the research_notes/body "Not dock/marina" phrases for the marina keyword-hit check
    # (we still want to detect them separately via EXPLICIT_NOT_MARINA).

    # --- 1. water_type gate --------------------------------------------------
    if water_type != "fresh":
        return {
            "incident_id": inc_id,
            "is_freshwater_private_dock": False,
            "is_freshwater_marina": False,
            "confidence": "high",
            "reasoning": f"water_type '{water_type or 'missing'}' is not fresh; both flags forced false per rule.",
        }

    # --- 2. Non-dock contexts ------------------------------------------------
    non_dock_hit = any_match(NON_DOCK_STRONG, facility, tb["body"], narrative)
    explicit_not = any_match(EXPLICIT_NOT_MARINA, narrative)

    # --- 3. Facility-based decisions (strongest signal) --------------------
    fac_priv = FACILITY_PRIVATE.search(facility)
    fac_mar = FACILITY_MARINA.search(facility)

    # Guard: if facility says "Private residence" with no dock keyword AND
    # non-dock hit → clear (this is e.g. flooded basement).
    if fac_priv and non_dock_hit:
        # Keep private match only if the facility name itself contains a dock
        # noun (dock, pier, boathouse, lakehouse, family lake home).
        if not re.search(r"\b(?:dock|pier|boathouse|lakehouse|lake\s+home)\b", facility, re.I):
            fac_priv = None

    if fac_mar and non_dock_hit:
        # Keep marina match only if facility explicitly says "Marina" etc.
        # (most "Marina" facility names indicate the real location even if
        # narrative mentions ancillary non-dock hazards).
        pass  # keep as-is — marina keyword in facility is strong.

    if fac_priv:
        return {
            "incident_id": inc_id,
            "is_freshwater_private_dock": True,
            "is_freshwater_marina": False,
            "confidence": "high",
            "reasoning": f"facility_name '{facility}' contains explicit private-dock keyword ({fac_priv.group(0)!r}).",
        }

    if fac_mar:
        return {
            "incident_id": inc_id,
            "is_freshwater_private_dock": False,
            "is_freshwater_marina": True,
            "confidence": "high",
            "reasoning": f"facility_name '{facility}' contains marina/yacht-club/boat-club/harbor keyword ({fac_mar.group(0)!r}).",
        }

    # --- 3b. Resort/campground with dock — commercial/shared use (marina-equivalent) ---
    # e.g. "Lake Hamilton Resort", "Brady Mountain Resort", "Piney Shores Resort",
    # "Franklin Lock Campground"
    if re.search(r"\b(resort|campground)\b", facility, re.I):
        # confirm there's a dock/boat/shore-power context
        dock_mention = re.search(
            r"\b(?:dock|pier|boathouse|ladder|slip|houseboat|shore\s+power|swim|boat\s+owner|prop\s+shaft|boat\s+lift)\b",
            facility + " " + narrative,
            re.I,
        )
        # Skip if the resort's dock is explicitly called "private"
        if dock_mention and not re.search(r"\bprivate\s+(?:dock|pier|boathouse)\b", facility + " " + narrative, re.I):
            return {
                "incident_id": inc_id,
                "is_freshwater_private_dock": False,
                "is_freshwater_marina": True,
                "confidence": "medium",
                "reasoning": f"facility_name '{facility}' is a commercial resort/campground with dock/boat activity — shared-use marina-equivalent setting.",
            }

    # --- 4. Non-dock early exit ---------------------------------------------
    if non_dock_hit:
        return {
            "incident_id": inc_id,
            "is_freshwater_private_dock": False,
            "is_freshwater_marina": False,
            "confidence": "high",
            "reasoning": f"non-dock electrocution context detected ({non_dock_hit!r}); both flags false.",
        }

    # --- 5. Narrative-based inference ---------------------------------------
    narr_priv = NARRATIVE_PRIVATE.search(narrative)
    narr_priv_weak = NARRATIVE_PRIVATE_WEAK.search(narrative)
    narr_mar = NARRATIVE_MARINA.search(narrative)

    if explicit_not:
        # The narrative explicitly says this is NOT a marina/dock case
        # But we may have already decided via facility. At this point facility
        # has no keyword, so: leave both false.
        return {
            "incident_id": inc_id,
            "is_freshwater_private_dock": False,
            "is_freshwater_marina": False,
            "confidence": "high",
            "reasoning": f"narrative explicitly states non-marina/non-dock context ({explicit_not!r}).",
        }

    # If narrative mentions marina only as proximity, discount it
    if narr_mar and any_match(PROXIMITY_ONLY, narrative):
        narr_mar = None

    # Mutually-exclusive narrative hits
    if narr_priv and narr_mar:
        # ambiguous
        return {
            "incident_id": inc_id,
            "is_freshwater_private_dock": False,
            "is_freshwater_marina": False,
            "confidence": "low",
            "reasoning": f"conflicting narrative cues (private: {narr_priv.group(0)!r}; marina: {narr_mar.group(0)!r}); leaving both false.",
        }

    if narr_priv:
        return {
            "incident_id": inc_id,
            "is_freshwater_private_dock": True,
            "is_freshwater_marina": False,
            "confidence": "high",
            "reasoning": f"narrative contains explicit private-dock cue: {narr_priv.group(0)!r}.",
        }

    if narr_mar:
        return {
            "incident_id": inc_id,
            "is_freshwater_private_dock": False,
            "is_freshwater_marina": True,
            "confidence": "medium",
            "reasoning": f"narrative indicates marina / yacht-club / boat-club setting: {narr_mar.group(0)!r}.",
        }

    if narr_priv_weak:
        # "At his parents' home", "at their lake home" — strong private-residence cue
        # but we want to confirm it was a dock incident. Check for dock/water mention.
        dock_mention = re.search(r"\b(?:dock|pier|boathouse|boat\s+lift|boat\s+hoist|swim\s+platform)\b", narrative, re.I)
        if dock_mention:
            return {
                "incident_id": inc_id,
                "is_freshwater_private_dock": True,
                "is_freshwater_marina": False,
                "confidence": "medium",
                "reasoning": f"narrative suggests private lake-home setting ({narr_priv_weak.group(0)!r}) with dock/lift mention.",
            }

    # "family home" + lake + dock/boat-lift: private residential
    if re.search(r"\bfamily\s+home\b", facility + " " + narrative, re.I):
        dock_mention = re.search(r"\b(?:dock|pier|boathouse|boat\s+lift|boat\s+hoist)\b", narrative, re.I)
        lake_mention = re.search(r"\b(?:lake|river|reservoir)\b", narrative + " " + tb["body"], re.I)
        if dock_mention and lake_mention:
            return {
                "incident_id": inc_id,
                "is_freshwater_private_dock": True,
                "is_freshwater_marina": False,
                "confidence": "medium",
                "reasoning": "narrative indicates 'family home' on a lake/river with a dock/boat-lift — residential private-dock setting.",
            }

    # "Private residence" on waterfront + dock/boat-lift: private residential
    if re.search(r"\bprivate\s+residence\b", facility, re.I):
        dock_mention = re.search(r"\b(?:dock|pier|boathouse|boat\s+lift|boat\s+hoist)\b", narrative + " " + facility, re.I)
        water_mention = re.search(r"\b(?:lake|river|reservoir|lagoon|channel|cove)\b", narrative + " " + tb["body"], re.I)
        if dock_mention and water_mention:
            return {
                "incident_id": inc_id,
                "is_freshwater_private_dock": True,
                "is_freshwater_marina": False,
                "confidence": "medium",
                "reasoning": "facility_name 'Private residence' on waterfront with dock/boat-lift — residential private-dock setting.",
            }

    # --- 6. No confident cue ------------------------------------------------
    # Check for public dock / park
    if re.search(r"\b(?:state\s+park|public\s+(?:dock|pier|ramp)|city\s+dock|municipal\s+dock|boat\s+ramp|public\s+boat|county\s+park)\b", narrative + " " + facility, re.I):
        return {
            "incident_id": inc_id,
            "is_freshwater_private_dock": False,
            "is_freshwater_marina": False,
            "confidence": "medium",
            "reasoning": "appears to be public / park / boat-ramp setting; neither private nor marina.",
        }

    return {
        "incident_id": inc_id,
        "is_freshwater_private_dock": False,
        "is_freshwater_marina": False,
        "confidence": "low",
        "reasoning": "no explicit facility or narrative cue distinguishing private dock vs. marina.",
    }


def main() -> int:
    data = json.loads(INPUT.read_text())
    assert len(data) == 201, f"Expected 201 records, got {len(data)}"

    results = [classify(r) for r in data]

    # Validation
    seen_ids = set()
    for r in results:
        if r["incident_id"] in seen_ids:
            raise RuntimeError(f"Duplicate id: {r['incident_id']}")
        seen_ids.add(r["incident_id"])
        if r["is_freshwater_private_dock"] and r["is_freshwater_marina"]:
            raise RuntimeError(f"Both flags true for {r['incident_id']}")
    in_ids = {r["incident_id"] for r in data}
    out_ids = {r["incident_id"] for r in results}
    missing = in_ids - out_ids
    extra = out_ids - in_ids
    if missing or extra:
        raise RuntimeError(f"id mismatch missing={missing} extra={extra}")

    wt = {r["incident_id"]: (r.get("water_type") or "").lower() for r in data}
    for r in results:
        if wt[r["incident_id"]] != "fresh":
            assert not r["is_freshwater_private_dock"]
            assert not r["is_freshwater_marina"]

    OUTPUT.write_text(json.dumps(results, indent=2))

    n_priv = sum(1 for r in results if r["is_freshwater_private_dock"])
    n_mar = sum(1 for r in results if r["is_freshwater_marina"])
    n_both_false = sum(
        1 for r in results
        if not r["is_freshwater_private_dock"] and not r["is_freshwater_marina"]
    )
    conf = Counter(r["confidence"] for r in results)

    print(f"Total: {len(results)}")
    print(f"  freshwater private dock: {n_priv}")
    print(f"  freshwater marina:       {n_mar}")
    print(f"  both false:              {n_both_false}")
    print(f"  confidence: {dict(conf)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
