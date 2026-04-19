#!/usr/bin/env python3
"""
Audit inventory: one row per incident across all 201 ESD-*.md files.

Produces:
  analysis/outputs/audit/inventory.csv  — machine-readable full audit grid
  analysis/outputs/audit/inventory.md   — human-readable summary tables
  analysis/outputs/audit/audit_flags.md — list of incidents with audit concerns

Used to give Nicole confidence that every one of the 201 has been seen, what
each one rests on (ESDPA + independent sources), and where the weak spots are.
"""
from __future__ import annotations
import csv
import json
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


def parse_frontmatter(path: Path) -> dict[str, Any]:
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?\n)---\s*\n(.*)$", txt, re.DOTALL)
    if not m:
        return {"_parse_error": "no frontmatter", "_body": txt}
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return {"_parse_error": f"yaml: {e}", "_body": m.group(2)}
    fm["_body"] = m.group(2)
    return fm


def bool_or_none(v: Any) -> bool | None:
    if v is None:
        return None
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in ("true", "1", "yes", "y"):
        return True
    if s in ("false", "0", "no", "n"):
        return False
    return None


def nonempty(v: Any) -> bool:
    if v is None:
        return False
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, (list, dict)):
        return bool(v)
    return True


def build_row(path: Path) -> dict[str, Any]:
    fm = parse_frontmatter(path)
    victims = fm.get("victims") or []
    sources = fm.get("sources") or []
    addl = fm.get("additional_sources") or []
    refs = fm.get("project_refs") or []
    issues = fm.get("esdpa_data_issues") or []
    entry_nums = fm.get("esdpa_entry_numbers") or []

    # Victim identification detail
    def named(v: dict) -> bool:
        fn = str(v.get("first_name", "")).strip().lower()
        ln = str(v.get("last_name", "")).strip().lower()
        return bool(fn) and fn not in ("unknown", "") and ln not in ("unknown", "")

    victims_named = sum(1 for v in victims if named(v))
    victims_age_known = sum(1 for v in victims if nonempty(v.get("age")))
    victims_gender_known = sum(1 for v in victims
                               if str(v.get("gender", "")).strip()
                               and str(v.get("gender", "")).lower() != "unknown")

    # Sources tally by type
    src_types = Counter()
    src_outlets = set()
    src_primary = 0  # primary = news, court, government, obituary (non-advocacy)
    primary_types = {"news", "court", "government", "obituary",
                     "academic", "legal", "video", "memorial"}
    for s in sources:
        if not isinstance(s, dict):
            continue
        t = str(s.get("type", "")).strip().lower()
        if t:
            src_types[t] += 1
            if t in primary_types:
                src_primary += 1
        o = str(s.get("outlet", "")).strip()
        if o:
            src_outlets.add(o)

    # Coordinates present?
    coords = fm.get("coordinates") or {}
    has_coords = bool(coords.get("lat") if isinstance(coords, dict) else None)

    # Missing key fields
    missing = []
    for k in ("state", "body_of_water", "date", "facility_name"):
        if not nonempty(fm.get(k)):
            missing.append(k)

    # ESDPA fields
    esdpa_listed = bool_or_none(fm.get("esdpa_listed"))
    esdpa_date_correct = bool_or_none(fm.get("esdpa_date_correct"))
    esdpa_date_listed = fm.get("esdpa_date_listed")
    has_deviation_flags = len(issues) > 0

    # Verification level
    vlevel = str(fm.get("verification_level", "")).strip().upper()

    # Discovery source normalization
    disc = str(fm.get("discovery_source", "")).strip()

    # Independent source count per YAML
    indep_ct = fm.get("independent_source_count")
    try:
        indep_ct = int(indep_ct) if indep_ct is not None else None
    except (TypeError, ValueError):
        indep_ct = None

    # Audit red flags
    flags = []
    if esdpa_listed and (indep_ct or 0) == 0 and vlevel in ("UNVERIFIED", ""):
        flags.append("ESDPA_ONLY_NO_INDEP")
    if not esdpa_listed and (indep_ct or 0) <= 1 and vlevel not in ("VERIFIED",):
        flags.append("NOVEL_LOW_SOURCES")
    if not sources:
        flags.append("NO_SOURCES_LIST")
    if not victims_named and fm.get("fatality_count", 0) and vlevel != "EXCLUDED":
        flags.append("NO_VICTIM_NAMED")
    if not nonempty(fm.get("date")) or fm.get("date_precision") in ("approximate",):
        flags.append("DATE_WEAK")
    if missing:
        flags.append("MISSING:" + ",".join(missing))
    if esdpa_listed and esdpa_date_correct is False and not esdpa_date_listed:
        flags.append("ESDPA_DATE_DEV_UNDOCUMENTED")
    if has_deviation_flags:
        flags.append("ESDPA_DEVIATION")
    if fm.get("_parse_error"):
        flags.append(f"PARSE_ERROR:{fm['_parse_error']}")

    return {
        "file": path.name,
        "incident_id": fm.get("incident_id", ""),
        "date": fm.get("date", ""),
        "year": fm.get("year", ""),
        "date_precision": fm.get("date_precision", ""),
        "state": fm.get("state", ""),
        "county": fm.get("county", ""),
        "city": fm.get("city", ""),
        "body_of_water": fm.get("body_of_water", ""),
        "facility_name": fm.get("facility_name", ""),
        "has_coordinates": has_coords,
        "incident_type": fm.get("incident_type", ""),
        "fatality_count": fm.get("fatality_count", 0),
        "injury_count": fm.get("injury_count", 0),
        "near_miss_count": fm.get("near_miss_count", 0),
        "victim_count": len(victims),
        "victims_named": victims_named,
        "victims_age_known": victims_age_known,
        "victims_gender_known": victims_gender_known,
        "electrical_source": fm.get("electrical_source", ""),
        "water_type": fm.get("water_type", ""),
        "voltage_reported": nonempty(fm.get("voltage")),
        "has_fault_description": nonempty(fm.get("fault_description")),
        "is_freshwater_private_dock": bool_or_none(fm.get("is_freshwater_private_dock")),
        "is_freshwater_marina": bool_or_none(fm.get("is_freshwater_marina")),
        "setting_classifier_confidence": fm.get("setting_classifier_confidence", ""),
        "verification_level": vlevel,
        "esdpa_listed": esdpa_listed,
        "esdpa_entry_count": len(entry_nums),
        "esdpa_entry_numbers": "; ".join(str(x) for x in entry_nums),
        "esdpa_date_correct": esdpa_date_correct,
        "esdpa_date_listed": esdpa_date_listed or "",
        "esdpa_data_issue_count": len(issues),
        "esdpa_data_issues": "; ".join(str(x) for x in issues),
        "discovery_source": disc,
        "additional_sources": "; ".join(str(x) for x in addl),
        "independent_source_count_yaml": indep_ct if indep_ct is not None else "",
        "sources_total": len(sources),
        "sources_primary": src_primary,
        "sources_by_type": json.dumps(dict(src_types), sort_keys=True),
        "distinct_outlets": len(src_outlets),
        "project_refs_count": len(refs),
        "has_notes": nonempty(fm.get("notes")),
        "has_research_notes": nonempty(fm.get("research_notes")),
        "missing_key_fields": ", ".join(missing),
        "audit_flags": " | ".join(flags),
        "audit_flag_count": len(flags),
    }


def main() -> None:
    files = sorted(DATASET.glob("ESD-*.md"))
    if not files:
        sys.stderr.write("No ESD-*.md files found.\n")
        sys.exit(1)

    rows = [build_row(p) for p in files]

    # ---- CSV ----
    csv_path = OUT / "inventory.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # ---- Summary markdown ----
    n = len(rows)
    esdpa = sum(1 for r in rows if r["esdpa_listed"] is True)
    novel = sum(1 for r in rows if r["esdpa_listed"] is False)
    unknown_listed = sum(1 for r in rows if r["esdpa_listed"] is None)

    by_vlevel = Counter(r["verification_level"] or "(blank)" for r in rows)
    by_disc = Counter(r["discovery_source"] or "(blank)" for r in rows)
    by_itype = Counter(r["incident_type"] or "(blank)" for r in rows)

    with_dev = [r for r in rows if r["esdpa_data_issue_count"] > 0]
    zero_src = [r for r in rows if r["sources_total"] == 0]
    only_esdpa = [r for r in rows if r["esdpa_listed"] is True
                  and (r["independent_source_count_yaml"] or 0) == 0]
    novel_weak = [r for r in rows if r["esdpa_listed"] is False
                  and (r["independent_source_count_yaml"] or 0) <= 1]
    flagged = [r for r in rows if r["audit_flag_count"] > 0]

    def count_flag(tag: str) -> int:
        return sum(1 for r in rows if tag in r["audit_flags"])

    md = OUT / "inventory.md"
    with md.open("w", encoding="utf-8") as f:
        w = f.write
        w(f"# ESD Dataset Audit Inventory\n\n")
        w(f"_Generated across **{n}** incident files in `esd-dataset/`._\n\n")

        w("## 1. Provenance\n\n")
        w(f"| Group | Count | % |\n|---|---:|---:|\n")
        w(f"| From ESDPA list | {esdpa} | {esdpa/n:.1%} |\n")
        w(f"| Novel (not in ESDPA) | {novel} | {novel/n:.1%} |\n")
        if unknown_listed:
            w(f"| Ambiguous (esdpa_listed blank) | {unknown_listed} | "
              f"{unknown_listed/n:.1%} |\n")
        w("\n")

        w("## 2. Discovery source (where we first found it)\n\n")
        w("| Source | Count |\n|---|---:|\n")
        for k, v in by_disc.most_common():
            w(f"| {k} | {v} |\n")
        w("\n")

        w("## 3. Verification level\n\n")
        w("| Level | Count | % |\n|---|---:|---:|\n")
        order = ["VERIFIED", "CONFIRMED", "PROBABLE", "SUSPECTED",
                 "UNVERIFIED", "EXCLUDED", "(blank)"]
        for k in order:
            if k in by_vlevel:
                w(f"| {k} | {by_vlevel[k]} | {by_vlevel[k]/n:.1%} |\n")
        for k, v in by_vlevel.items():
            if k not in order:
                w(f"| {k} | {v} | {v/n:.1%} |\n")
        w("\n")

        w("## 4. Incident type\n\n")
        w("| Type | Count |\n|---|---:|\n")
        for k, v in by_itype.most_common():
            w(f"| {k} | {v} |\n")
        w("\n")

        w("## 5. ESDPA-vs-ours deviations\n\n")
        w(f"- Incidents with at least one deviation logged: **{len(with_dev)}**\n")
        w(f"- Incidents where `esdpa_date_correct = false`: "
          f"**{sum(1 for r in rows if r['esdpa_date_correct'] is False)}**\n\n")

        w("## 6. Source strength\n\n")
        w(f"- Files with **zero** sources in `sources:` list: **{len(zero_src)}**\n")
        w(f"- ESDPA-listed with 0 independent sources: **{len(only_esdpa)}**\n")
        w(f"- Novel (non-ESDPA) with ≤1 independent sources: **{len(novel_weak)}**\n")
        w(f"- Mean sources per incident: **"
          f"{sum(r['sources_total'] for r in rows)/n:.2f}**\n")
        w(f"- Max sources on a single incident: **"
          f"{max(r['sources_total'] for r in rows)}**\n\n")

        w("## 7. Audit-flag totals\n\n")
        w("| Flag | Count |\n|---|---:|\n")
        for tag in ["ESDPA_ONLY_NO_INDEP", "NOVEL_LOW_SOURCES",
                    "NO_SOURCES_LIST", "NO_VICTIM_NAMED", "DATE_WEAK",
                    "ESDPA_DEVIATION", "ESDPA_DATE_DEV_UNDOCUMENTED",
                    "PARSE_ERROR"]:
            w(f"| {tag} | {count_flag(tag)} |\n")
        w(f"\nTotal files with ≥1 audit flag: **{len(flagged)}** "
          f"({len(flagged)/n:.1%})\n\n")

        w("## 8. Geographic spread (top 15 states)\n\n")
        by_state = Counter(r["state"] or "(blank)" for r in rows)
        w("| State | Count |\n|---|---:|\n")
        for k, v in by_state.most_common(15):
            w(f"| {k} | {v} |\n")
        w("\n")

        w("## 9. Year span\n\n")
        yrs = [int(r["year"]) for r in rows if str(r["year"]).strip().isdigit()]
        if yrs:
            w(f"- Earliest: **{min(yrs)}**\n")
            w(f"- Latest: **{max(yrs)}**\n")
            w(f"- Span: **{max(yrs) - min(yrs) + 1} years**\n")
            w(f"- Incidents with a usable year: **{len(yrs)} / {n}**\n\n")

    # ---- Flags markdown ----
    flags_md = OUT / "audit_flags.md"
    with flags_md.open("w", encoding="utf-8") as f:
        w = f.write
        w("# Audit Flags: incidents that need closer review\n\n")
        w(f"_{len(flagged)} of {n} incidents have at least one audit flag._\n\n")
        w("Flags defined:\n\n")
        w("- **ESDPA_ONLY_NO_INDEP** — in ESDPA list, no independent sources found. ")
        w("Nicole will be asked why this is in the dataset.\n")
        w("- **NOVEL_LOW_SOURCES** — not in ESDPA, 0-1 independent sources. Claim is weakest.\n")
        w("- **NO_SOURCES_LIST** — `sources:` YAML is empty entirely.\n")
        w("- **NO_VICTIM_NAMED** — fatality case with no victim name known.\n")
        w("- **DATE_WEAK** — date missing or marked approximate.\n")
        w("- **ESDPA_DEVIATION** — we flagged at least one issue with ESDPA's entry.\n")
        w("- **MISSING:...** — a key field (state, body_of_water, date, facility_name) is blank.\n\n")

        # Group by primary flag
        by_flag = defaultdict(list)
        for r in flagged:
            primary = r["audit_flags"].split(" | ")[0]
            by_flag[primary].append(r)

        for flag in sorted(by_flag.keys()):
            rs = by_flag[flag]
            w(f"## {flag}  ({len(rs)})\n\n")
            for r in rs:
                who = r["victims_named"] and "named victim" or "no victim name"
                parts = [str(r["state"]) if r["state"] else "",
                         str(r["body_of_water"]) if r["body_of_water"] else ""]
                loc = " / ".join(p for p in parts if p) or "unknown location"
                w(f"- `{r['file']}` — {r['date'] or 'no date'} — {loc} — "
                  f"{r['verification_level'] or '(no level)'} — "
                  f"sources={r['sources_total']} — flags: {r['audit_flags']}\n")
            w("\n")

    print(f"Wrote {csv_path}")
    print(f"Wrote {md}")
    print(f"Wrote {flags_md}")
    print()
    print(f"Summary: {n} incidents  |  ESDPA-listed={esdpa}  novel={novel}  "
          f"|  flagged={len(flagged)}")


if __name__ == "__main__":
    main()
