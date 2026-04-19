#!/usr/bin/env python3
"""
Weak-evidence triage list.

Flags incidents most likely to be challenged in a hostile Q&A:
  - ESDPA-listed with 0 independent sources (they rest on ESDPA alone)
  - Novel incidents with <=1 independent source (we added them on thin evidence)
  - Fatality cases with no named victim
  - Incidents with only secondary-source citations (no news / obit / court / gov)

For each, suggest a concrete next action with effort estimate.

Output: analysis/outputs/audit/weak_evidence.md
        analysis/outputs/audit/weak_evidence.csv
"""
from __future__ import annotations
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.stderr.write("Install pyyaml: pip install pyyaml\n")
    sys.exit(1)

ROOT = Path("/opt/repos/esd-research")
DATASET = ROOT / "esd-dataset"
OUT = ROOT / "analysis/outputs/audit"
OUT.mkdir(parents=True, exist_ok=True)

PRIMARY_TYPES = {"news", "court", "government", "obituary",
                 "academic", "legal", "video", "memorial"}


def parse_frontmatter(path: Path) -> dict[str, Any]:
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?\n)---\s*\n(.*)$", txt, re.DOTALL)
    if not m:
        return {}
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}
    fm["_body"] = m.group(2)
    return fm


def bool_or_none(v: Any) -> bool | None:
    if isinstance(v, bool):
        return v
    if v is None:
        return None
    s = str(v).strip().lower()
    return True if s in ("true", "1", "yes") else (False if s in ("false", "0", "no") else None)


def int_or_zero(v: Any) -> int:
    try:
        return int(v) if v is not None else 0
    except (TypeError, ValueError):
        return 0


def classify(r: dict[str, Any]) -> tuple[str, str, str]:
    """Return (tier, action, effort)."""
    listed = r["esdpa_listed"]
    indep = r["independent_source_count"]
    vlevel = r["verification_level"]
    year = r["year"]
    named = r["victims_named"]

    # Tier A: most concerning
    if not listed and indep <= 1:
        return ("A: Novel + thin", "Find second independent source, or mark SUSPECTED", "medium")
    if listed and indep == 0 and vlevel == "UNVERIFIED":
        if year and str(year).isdigit() and int(year) < 2000:
            return ("B: ESDPA-only, old", "Check obituary archives, local newspaper morgues", "hard")
        else:
            return ("B: ESDPA-only, recent", "Search news + obituaries for named victim", "easy")
    if listed and indep == 0:
        return ("C: ESDPA-only, ambiguous", "Verify classification; search local news", "easy")
    if not named and r["fatality_count"] > 0:
        return ("D: Fatal + anonymous", "Obituary / coroner search for victim name", "medium")
    return ("E: Other", "Review if flagged", "low")


def main() -> None:
    files = sorted(DATASET.glob("ESD-*.md"))
    rows = []

    for p in files:
        fm = parse_frontmatter(p)
        if not fm:
            continue

        victims = fm.get("victims") or []
        names = []
        for v in victims:
            fn = str(v.get("first_name", "")).strip()
            ln = str(v.get("last_name", "")).strip()
            tag = f"{fn} {ln}".strip()
            if tag.lower() not in ("unknown unknown", "unknown", ""):
                names.append(tag)

        sources = fm.get("sources") or []
        primary_ct = 0
        src_summary = []
        for s in sources:
            if not isinstance(s, dict):
                continue
            t = str(s.get("type", "")).lower().strip()
            if t in PRIMARY_TYPES:
                primary_ct += 1
            src_summary.append({
                "type": t,
                "outlet": str(s.get("outlet", "")),
                "url": str(s.get("url", "")),
            })

        listed = bool_or_none(fm.get("esdpa_listed"))
        indep = int_or_zero(fm.get("independent_source_count"))
        fatality_ct = int_or_zero(fm.get("fatality_count"))
        vlevel = str(fm.get("verification_level", "")).upper()

        # Eligibility for weak-evidence list
        is_weak = False
        reasons = []
        if listed is True and indep == 0:
            is_weak = True
            reasons.append("ESDPA_ONLY_NO_INDEP")
        if listed is False and indep <= 1:
            is_weak = True
            reasons.append("NOVEL_LOW_INDEP")
        if not names and fatality_ct > 0 and vlevel != "EXCLUDED":
            is_weak = True
            reasons.append("FATAL_ANONYMOUS")
        if sources and primary_ct == 0:
            is_weak = True
            reasons.append("NO_PRIMARY_SOURCES")
        if len(sources) == 0 and listed is True:
            is_weak = True
            reasons.append("EMPTY_SOURCES_LIST")

        if not is_weak:
            continue

        r = {
            "file": p.name,
            "incident_id": str(fm.get("incident_id", "")),
            "date": str(fm.get("date", "")),
            "year": fm.get("year", ""),
            "state": str(fm.get("state", "")),
            "body_of_water": str(fm.get("body_of_water", "")),
            "facility_name": str(fm.get("facility_name", "")),
            "victims_named": " + ".join(names),
            "fatality_count": fatality_ct,
            "incident_type": str(fm.get("incident_type", "")),
            "verification_level": vlevel,
            "esdpa_listed": listed,
            "esdpa_entry_numbers": "; ".join(
                str(x) for x in (fm.get("esdpa_entry_numbers") or [])),
            "independent_source_count": indep,
            "sources_total": len(sources),
            "primary_source_count": primary_ct,
            "discovery_source": str(fm.get("discovery_source", "")),
            "notes": str(fm.get("notes", ""))[:300],
            "weakness_reasons": " | ".join(reasons),
            "sources_preview": " | ".join(
                f"{s['type']}:{s['outlet']}" for s in src_summary[:3]),
        }
        tier, action, effort = classify(r)
        r["tier"] = tier
        r["suggested_action"] = action
        r["effort"] = effort
        rows.append(r)

    # ---- CSV ----
    csv_path = OUT / "weak_evidence.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        if rows:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    # ---- Markdown ----
    md = OUT / "weak_evidence.md"
    by_tier = defaultdict(list)
    for r in rows:
        by_tier[r["tier"]].append(r)
    tier_order = sorted(by_tier.keys())

    tier_descriptions = {
        "A: Novel + thin": (
            "Incidents we added that rest on 0–1 independent sources. These are "
            "where the dataset's claim to go beyond ESDPA is weakest."
        ),
        "B: ESDPA-only, old": (
            "ESDPA-listed, no independent sources found, incident is pre-2000. "
            "Pre-digital-archive era makes verification inherently hard. "
            "Defensible to keep as 'carried forward from ESDPA compilation'."
        ),
        "B: ESDPA-only, recent": (
            "ESDPA-listed, no independent sources found, incident is 2000 or later. "
            "Most concerning — should be findable if real."
        ),
        "C: ESDPA-only, ambiguous": (
            "ESDPA-listed, no independent sources, but not straightforwardly in the "
            "ESDPA scope (e.g., pool, fountain, non-fatal)."
        ),
        "D: Fatal + anonymous": (
            "Fatality incidents where we have no victim name. Not necessarily weak "
            "evidence, but harder to defend without a name attached."
        ),
        "E: Other": "Other weak-evidence conditions.",
    }

    with md.open("w", encoding="utf-8") as f:
        w = f.write
        w("# Weak-Evidence Triage List\n\n")
        w(f"_{len(rows)} of 201 incidents flagged as having evidence weaker "
          "than the bulk of the dataset. For Nicole's pre-talk confidence check: "
          "these are the entries a skeptical questioner could target._\n\n")

        w("## Tier counts\n\n")
        w("| Tier | Count | Nature |\n|---|---:|---|\n")
        for tier in tier_order:
            desc = tier_descriptions.get(tier, "").split(".")[0] + "."
            w(f"| {tier} | {len(by_tier[tier])} | {desc} |\n")
        w("\n")

        w("## Defensive framing\n\n")
        w("For each tier, a one-line way to speak about these entries on stage:\n\n")
        w("- **Tier A (Novel, thin)**: \"These are leads we surfaced through deep "
          "search that we're holding at a cautious verification level; each has "
          "one documented source and we'd welcome more.\"\n")
        w("- **Tier B-old (ESDPA pre-2000)**: \"These predate digital news "
          "archives. We cite them as they appear in the ESDPA compilation and "
          "have classified them as UNVERIFIED to reflect that.\"\n")
        w("- **Tier B-recent (ESDPA post-2000)**: \"These are the ones we're "
          "still working to independently confirm. Current verification level "
          "UNVERIFIED is honest about the gap.\"\n")
        w("- **Tier C (ESDPA ambiguous scope)**: \"These are in the ESDPA list "
          "but fit the broader in-water-electrocution scope rather than classic "
          "dock/marina ESD; documented with EXCLUDED or SUSPECTED as appropriate.\"\n")
        w("- **Tier D (Fatal anonymous)**: \"Some incidents are reported without "
          "the victim's name in public records; we carry these with anonymized "
          "entries and flag them for obituary/coroner follow-up.\"\n\n")

        for tier in tier_order:
            rs = sorted(by_tier[tier], key=lambda r: (str(r["state"]),
                                                       r["date"] or "0"))
            w(f"## {tier}  ({len(rs)})\n\n")
            w(f"{tier_descriptions.get(tier, '')}\n\n")
            w("| File | Date | State | Body of water | Victim | Sources | "
              "Suggested action |\n")
            w("|---|---|---|---|---|:---:|---|\n")
            for r in rs:
                w(f"| `{r['file']}` | {r['date'] or '—'} | "
                  f"{r['state'] or '—'} | {r['body_of_water'] or '—'} | "
                  f"{r['victims_named'] or '(anonymous)'} | "
                  f"{r['sources_total']} | {r['suggested_action']} |\n")
            w("\n")

    # Aggregate weakness-reason counts
    reason_counts = Counter()
    for r in rows:
        for x in r["weakness_reasons"].split(" | "):
            reason_counts[x] += 1

    print(f"Wrote {csv_path}")
    print(f"Wrote {md}")
    print(f"Flagged: {len(rows)} of 201")
    print("Weakness reasons:")
    for k, v in reason_counts.most_common():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
