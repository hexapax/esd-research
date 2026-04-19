#!/usr/bin/env python3
"""
Pull the fields needed to decide is_freshwater_private_dock / is_freshwater_marina
for every incident. Writes a single JSON file the classifier can read.

Only fields relevant to the decision are included to keep the payload compact.
"""
import glob, json, os, re, yaml

DATASET_DIR = "/opt/repos/esd-research/esd-dataset"
OUT = "/opt/repos/esd-research/analysis/classifier_input.json"

def parse_yaml(fp):
    with open(fp, "r", encoding="utf-8") as f:
        txt = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", txt, re.DOTALL)
    if not m:
        return None, ""
    data = yaml.safe_load(m.group(1))
    # Markdown body (for richer context)
    body = txt[m.end():].strip()
    return data, body

def g(d, *keys, default=""):
    for k in keys:
        d = d.get(k, default) if isinstance(d, dict) else default
    return d if d is not None else default

records = []
for fp in sorted(glob.glob(os.path.join(DATASET_DIR, "ESD-*.md"))):
    d, body = parse_yaml(fp)
    if not d:
        continue
    rec = {
        "incident_id": g(d, "incident_id"),
        "year": g(d, "year"),
        "state": g(d, "state"),
        "city": g(d, "city"),
        "body_of_water": g(d, "body_of_water"),
        "facility_name": g(d, "facility_name"),
        "water_type": g(d, "water_type"),
        "electrical_source": g(d, "electrical_source"),
        "fault_description": g(d, "fault_description"),
        "notes": g(d, "notes"),
        "research_notes": g(d, "research_notes"),
        "body": body[:1500],  # cap
    }
    records.append(rec)

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2, ensure_ascii=False)
print(f"Wrote {len(records)} records to {OUT}")
