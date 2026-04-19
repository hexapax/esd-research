#!/usr/bin/env python3
"""
ESDPA-vs-ours deviation report.

For every ESDPA-listed incident where our dataset differs from ESDPA, produce a
single structured entry documenting:
  - ESDPA entry numbers
  - What ESDPA said (date, narrative)
  - What we say (date, narrative)
  - Each logged deviation with the source/reasoning
  - Verification level

Output: analysis/outputs/audit/esdpa_deviations.md
        analysis/outputs/audit/esdpa_deviations.csv
"""
from __future__ import annotations
import csv
import re
import sys
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


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?\n)---\s*\n(.*)$", txt, re.DOTALL)
    if not m:
        return {}, txt
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}, m.group(2)
    return fm, m.group(2)


def bool_or_none(v: Any) -> bool | None:
    if v is None:
        return None
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    return True if s in ("true", "1", "yes") else (False if s in ("false", "0", "no") else None)


def main() -> None:
    files = sorted(DATASET.glob("ESD-*.md"))
    deviation_rows = []

    for p in files:
        fm, _body = parse_frontmatter(p)
        if not fm:
            continue
        listed = bool_or_none(fm.get("esdpa_listed"))
        if listed is not True:
            continue

        issues = fm.get("esdpa_data_issues") or []
        date_correct = bool_or_none(fm.get("esdpa_date_correct"))
        date_listed = fm.get("esdpa_date_listed") or ""

        # Has any deviation?
        has_issue = len(issues) > 0 or date_correct is False
        if not has_issue:
            continue

        victims = fm.get("victims") or []
        names = []
        for v in victims:
            fn = str(v.get("first_name", "")).strip()
            ln = str(v.get("last_name", "")).strip()
            age = v.get("age")
            gender = v.get("gender", "")
            if (fn and fn.lower() != "unknown") or (ln and ln.lower() != "unknown"):
                tag = f"{fn} {ln}".strip()
                if age is not None and str(age).strip():
                    tag += f" ({age}"
                    if gender:
                        tag += f"{gender}"
                    tag += ")"
                elif gender:
                    tag += f" ({gender})"
                names.append(tag)

        entry_nums = fm.get("esdpa_entry_numbers") or []
        sources = fm.get("sources") or []
        primary_urls = [
            str(s.get("url", "")) for s in sources[:3]
            if isinstance(s, dict) and s.get("url")
        ]

        deviation_rows.append({
            "file": p.name,
            "incident_id": fm.get("incident_id", ""),
            "our_date": str(fm.get("date", "")),
            "esdpa_date_listed": str(date_listed),
            "esdpa_date_correct": date_correct,
            "state": str(fm.get("state", "")),
            "body_of_water": str(fm.get("body_of_water", "")),
            "facility_name": str(fm.get("facility_name", "")),
            "victims_named": " + ".join(names) if names else "(no victim named)",
            "fatality_count": fm.get("fatality_count", 0),
            "verification_level": str(fm.get("verification_level", "")),
            "independent_source_count": fm.get("independent_source_count", 0),
            "esdpa_entry_numbers": "; ".join(str(x) for x in entry_nums),
            "data_issues": issues,
            "primary_sources": primary_urls,
            "notes": str(fm.get("notes", ""))[:400],
            "research_notes": str(fm.get("research_notes", ""))[:400],
        })

    # ---- CSV ----
    csv_path = OUT / "esdpa_deviations.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "file", "incident_id", "our_date", "esdpa_date_listed",
            "esdpa_date_correct", "state", "body_of_water", "facility_name",
            "victims_named", "fatality_count", "verification_level",
            "independent_source_count", "esdpa_entry_numbers",
            "data_issues_joined", "primary_sources_joined", "notes",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in deviation_rows:
            out_r = {k: v for k, v in r.items() if k in fieldnames}
            out_r["data_issues_joined"] = " | ".join(r["data_issues"])
            out_r["primary_sources_joined"] = " | ".join(r["primary_sources"])
            w.writerow(out_r)

    # ---- Markdown narrative ----
    md_path = OUT / "esdpa_deviations.md"
    with md_path.open("w", encoding="utf-8") as f:
        w = f.write
        w("# ESDPA → Our Dataset: Deviation Report\n\n")
        w(f"_Every ESDPA-listed incident where our independently-verified data ")
        w(f"differs from what ESDPA published. Total: **{len(deviation_rows)}** "
          f"entries._\n\n")
        w("This report is the primary evidence that we did not simply copy the ")
        w("ESDPA list. For each entry below:\n\n")
        w("- **ESDPA#** — the entry number(s) in the ESDPA compilation\n")
        w("- **ESDPA date** — the date ESDPA published\n")
        w("- **Our date** — the date we assigned after independent verification\n")
        w("- **Deviations logged** — every specific issue we documented\n")
        w("- **Primary sources** — non-ESDPA sources we used\n\n")
        w("---\n\n")

        # Group by state for browsability
        by_state: dict[str, list] = {}
        for r in deviation_rows:
            by_state.setdefault(r["state"] or "(unknown)", []).append(r)

        for st in sorted(by_state.keys()):
            rs = by_state[st]
            w(f"## {st}  ({len(rs)} entries)\n\n")
            for r in sorted(rs, key=lambda x: x["our_date"]):
                title = r["victims_named"]
                if title == "(no victim named)":
                    title = r["body_of_water"] or r["facility_name"] or "(unnamed)"
                w(f"### `{r['file']}` — {title}\n\n")
                w(f"- **Our date:** {r['our_date'] or '(blank)'}\n")
                w(f"- **ESDPA date listed:** {r['esdpa_date_listed'] or '(not recorded)'}\n")
                w(f"- **ESDPA date correct:** {r['esdpa_date_correct']}\n")
                w(f"- **ESDPA entry #:** {r['esdpa_entry_numbers'] or '(not recorded)'}\n")
                w(f"- **Location:** {r['body_of_water']} | "
                  f"{r['facility_name'] or '(no facility)'}\n")
                w(f"- **Verification:** {r['verification_level']} "
                  f"(independent sources: {r['independent_source_count']})\n")
                if r["data_issues"]:
                    w(f"- **Deviations logged:**\n")
                    for iss in r["data_issues"]:
                        w(f"  - {iss}\n")
                else:
                    w(f"- **Deviations logged:** (date-only correction)\n")
                if r["primary_sources"]:
                    w(f"- **Primary sources (up to 3):**\n")
                    for u in r["primary_sources"]:
                        w(f"  - {u}\n")
                if r["notes"]:
                    w(f"- **Summary:** {r['notes']}\n")
                w("\n")

    print(f"Wrote {csv_path}")
    print(f"Wrote {md_path}")
    print(f"Total deviations: {len(deviation_rows)}")


if __name__ == "__main__":
    main()
