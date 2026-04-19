#!/usr/bin/env python3
"""
Novel-incidents provenance report.

For every incident NOT in ESDPA, document:
  - How we found it (discovery_source LOA)
  - Which primary sources support it
  - Verification level + source count
  - Victim, date, location as we have them
  - What remains open (research_notes)

Output: analysis/outputs/audit/novel_incidents.md
        analysis/outputs/audit/novel_incidents.csv
"""
from __future__ import annotations
import csv
import re
import sys
from collections import Counter
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
    novel = []

    for p in files:
        fm, _body = parse_frontmatter(p)
        if not fm:
            continue
        listed = bool_or_none(fm.get("esdpa_listed"))
        if listed is True:
            continue  # skip ESDPA-listed

        victims = fm.get("victims") or []
        names = []
        for v in victims:
            fn = str(v.get("first_name", "")).strip()
            ln = str(v.get("last_name", "")).strip()
            age = v.get("age")
            gender = v.get("gender", "")
            tag = f"{fn} {ln}".strip()
            if tag.lower() in ("unknown unknown", "unknown"):
                tag = ""
            if tag:
                if age is not None and str(age).strip():
                    tag += f" ({age}"
                    if gender:
                        tag += f"{gender}"
                    tag += ")"
                names.append(tag)

        sources = fm.get("sources") or []
        src_summary = []
        for s in sources:
            if not isinstance(s, dict):
                continue
            t = str(s.get("type", ""))
            o = str(s.get("outlet", ""))
            u = str(s.get("url", ""))
            src_summary.append({"type": t, "outlet": o, "url": u})

        novel.append({
            "file": p.name,
            "incident_id": str(fm.get("incident_id", "")),
            "date": str(fm.get("date", "")),
            "year": fm.get("year", ""),
            "date_precision": str(fm.get("date_precision", "")),
            "state": str(fm.get("state", "")),
            "county": str(fm.get("county", "")),
            "city": str(fm.get("city", "")),
            "body_of_water": str(fm.get("body_of_water", "")),
            "facility_name": str(fm.get("facility_name", "")),
            "victims_named": " + ".join(names),
            "fatality_count": fm.get("fatality_count", 0),
            "injury_count": fm.get("injury_count", 0),
            "near_miss_count": fm.get("near_miss_count", 0),
            "incident_type": str(fm.get("incident_type", "")),
            "electrical_source": str(fm.get("electrical_source", "")),
            "verification_level": str(fm.get("verification_level", "")),
            "discovery_source": str(fm.get("discovery_source", "")),
            "additional_sources": fm.get("additional_sources") or [],
            "independent_source_count": fm.get("independent_source_count", 0),
            "sources": src_summary,
            "notes": str(fm.get("notes", "")),
            "research_notes": str(fm.get("research_notes", "")),
        })

    # ---- CSV ----
    csv_path = OUT / "novel_incidents.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "file", "incident_id", "date", "state", "body_of_water",
            "facility_name", "victims_named", "fatality_count", "incident_type",
            "verification_level", "discovery_source",
            "additional_sources_joined", "independent_source_count",
            "sources_count", "sources_joined", "notes"
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in novel:
            row = {k: v for k, v in r.items() if k in fieldnames}
            row["additional_sources_joined"] = "; ".join(
                str(x) for x in r["additional_sources"])
            row["sources_count"] = len(r["sources"])
            row["sources_joined"] = " | ".join(
                f"{s['type']}:{s['outlet']}:{s['url']}" for s in r["sources"])
            row["notes"] = r["notes"][:500]
            w.writerow(row)

    # ---- Markdown narrative ----
    md_path = OUT / "novel_incidents.md"
    by_vlevel = Counter(r["verification_level"] or "(blank)" for r in novel)
    by_disc = Counter(r["discovery_source"] or "(blank)" for r in novel)

    with md_path.open("w", encoding="utf-8") as f:
        w = f.write
        w("# Novel Incidents: Not In ESDPA\n\n")
        w(f"_{len(novel)} incidents in our dataset were not present in the ESDPA "
          "compilation. This report documents how each was found, which primary "
          "sources support it, and what remains open._\n\n")

        w("## Summary\n\n")
        w("**Verification levels:**\n\n")
        for k, v in sorted(by_vlevel.items(), key=lambda x: -x[1]):
            w(f"- {k}: {v}\n")
        w("\n**Discovery source (Line of Attack):**\n\n")
        for k, v in sorted(by_disc.items(), key=lambda x: -x[1]):
            w(f"- {k}: {v}\n")
        w("\n---\n\n")

        # Sort: verified/confirmed first, then by date
        order = {"VERIFIED": 0, "CONFIRMED": 1, "PROBABLE": 2,
                 "SUSPECTED": 3, "UNVERIFIED": 4, "": 5}
        novel.sort(key=lambda r: (order.get(r["verification_level"], 9),
                                   r["date"] or "0000-00-00"))

        for r in novel:
            title = r["victims_named"] or r["body_of_water"] or r["facility_name"] or r["incident_id"]
            w(f"## `{r['file']}` — {title}\n\n")
            w(f"- **Date:** {r['date'] or '(unknown)'} "
              f"({r['date_precision'] or 'no precision given'})\n")
            loc = ", ".join(p for p in [r["city"], r["county"], r["state"]] if p)
            w(f"- **Location:** {loc or '(unspecified)'}\n")
            if r["body_of_water"]:
                w(f"- **Body of water:** {r['body_of_water']}\n")
            if r["facility_name"]:
                w(f"- **Facility:** {r['facility_name']}\n")
            w(f"- **Outcome:** {r['incident_type']} — {r['fatality_count']} fatal / "
              f"{r['injury_count']} injury / {r['near_miss_count']} near-miss\n")
            w(f"- **Electrical mechanism:** {r['electrical_source'] or '(unspecified)'}\n")
            w(f"- **Verification level:** **{r['verification_level']}**\n")
            w(f"- **How we found it:** discovery_source = `{r['discovery_source']}`")
            if r["additional_sources"]:
                addl = ", ".join(str(x) for x in r["additional_sources"])
                w(f"; also found via: {addl}")
            w("\n")
            w(f"- **Independent source count:** {r['independent_source_count']}\n")
            if r["sources"]:
                w(f"- **Primary sources:**\n")
                for s in r["sources"]:
                    line = f"  - {s['type']}: {s['outlet']}" if s["outlet"] else f"  - {s['type']}"
                    if s["url"]:
                        line += f" — {s['url']}"
                    w(line + "\n")
            else:
                w(f"- **Primary sources:** _none listed in YAML_\n")
            if r["notes"]:
                w(f"\n**Summary:** {r['notes']}\n")
            if r["research_notes"]:
                w(f"\n**Open / research notes:** {r['research_notes']}\n")
            w("\n---\n\n")

    print(f"Wrote {csv_path}")
    print(f"Wrote {md_path}")
    print(f"Total novel incidents: {len(novel)}")


if __name__ == "__main__":
    main()
