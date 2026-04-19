#!/usr/bin/env python3
"""
Geocode every incident in esd-dataset/ from body_of_water + city + state.

Uses Nominatim (OpenStreetMap) — free, 1 req/sec rate limit, no API key.
Caches results in analysis/geocode_cache.json so re-runs are instant.

Output: analysis/outputs/map/incidents_geocoded.csv
Columns: file, lat, lon, query_used, match_type, display_name, everything we
need for static + interactive maps.
"""
from __future__ import annotations
import json
import re
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

try:
    import yaml
except ImportError:
    sys.stderr.write("pip install pyyaml\n"); sys.exit(1)

ROOT = Path("/opt/repos/esd-research")
DATASET = ROOT / "esd-dataset"
OUT_DIR = ROOT / "analysis/outputs/map"
OUT_DIR.mkdir(parents=True, exist_ok=True)
CACHE = ROOT / "analysis/geocode_cache.json"

# Non-US state codes (pass country as Canada instead)
CANADA = {"QC", "ON", "BC", "AB", "MB", "SK", "NS", "NB", "NL", "NT", "PE",
          "YT", "NU"}

# State centroid fallback (rough; only used when all else fails)
STATE_CENTROIDS = {
    "AL": (32.806671, -86.791130), "AK": (61.370716, -152.404419),
    "AZ": (33.729759, -111.431221), "AR": (34.969704, -92.373123),
    "CA": (36.116203, -119.681564), "CO": (39.059811, -105.311104),
    "CT": (41.597782, -72.755371), "DE": (39.318523, -75.507141),
    "FL": (27.766279, -81.686783), "GA": (33.040619, -83.643074),
    "HI": (21.094318, -157.498337), "ID": (44.240459, -114.478828),
    "IL": (40.349457, -88.986137), "IN": (39.849426, -86.258278),
    "IA": (42.011539, -93.210526), "KS": (38.526600, -96.726486),
    "KY": (37.668140, -84.670067), "LA": (31.169546, -91.867805),
    "ME": (44.693947, -69.381927), "MD": (39.063946, -76.802101),
    "MA": (42.230171, -71.530106), "MI": (43.326618, -84.536095),
    "MN": (45.694454, -93.900192), "MS": (32.741646, -89.678696),
    "MO": (38.456085, -92.288368), "MT": (46.921925, -110.454353),
    "NE": (41.125370, -98.268082), "NV": (38.313515, -117.055374),
    "NH": (43.452492, -71.563896), "NJ": (40.298904, -74.521011),
    "NM": (34.840515, -106.248482), "NY": (42.165726, -74.948051),
    "NC": (35.630066, -79.806419), "ND": (47.528912, -99.784012),
    "OH": (40.388783, -82.764915), "OK": (35.565342, -96.928917),
    "OR": (44.572021, -122.070938), "PA": (40.590752, -77.209755),
    "RI": (41.680893, -71.511780), "SC": (33.856892, -80.945007),
    "SD": (44.299782, -99.438828), "TN": (35.747845, -86.692345),
    "TX": (31.054487, -97.563461), "UT": (40.150032, -111.862434),
    "VT": (44.045876, -72.710686), "VA": (37.769337, -78.169968),
    "WA": (47.400902, -121.490494), "WV": (38.491226, -80.954453),
    "WI": (44.268543, -89.616508), "WY": (42.755966, -107.302490),
    "DC": (38.897438, -77.026817),
    "QC": (52.939916, -73.549138), "BC": (53.726669, -127.647621),
}

HEADERS = {
    "User-Agent": "esd-research-mapping/1.0 (github.com/hexapax/esd-research)"
}


def parse_frontmatter(path: Path) -> dict[str, Any]:
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?\n)---\s*\n(.*)$", txt, re.DOTALL)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def clean_body(s: str) -> str:
    # Strip "Mile Marker" annotations, addresses, parenthetical bits
    s = re.sub(r",?\s*\d+(?:\.\d+)?\s*mile marker.*", "", s, flags=re.I)
    s = re.sub(r"\s*\([^)]*\)", "", s)
    s = s.split(" — ")[0]
    s = s.split(" - ")[0] if " - " in s and len(s.split(" - ")[0]) > 6 else s
    return s.strip(", ")


def load_cache() -> dict:
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def save_cache(c: dict) -> None:
    CACHE.write_text(json.dumps(c, indent=2), encoding="utf-8")


def nominatim_query(q: str, country: str = "usa") -> dict | None:
    params = {
        "q": q,
        "format": "json",
        "limit": 1,
        "addressdetails": 1,
        "countrycodes": "us" if country == "usa" else "ca",
    }
    url = "https://nominatim.openstreetmap.org/search?" + urlencode(params)
    req = Request(url, headers=HEADERS)
    try:
        with urlopen(req, timeout=15) as f:
            data = json.loads(f.read().decode("utf-8"))
    except Exception as e:
        sys.stderr.write(f"  ! nominatim error for '{q}': {e}\n")
        return None
    if not data:
        return None
    r = data[0]
    return {
        "lat": float(r["lat"]),
        "lon": float(r["lon"]),
        "display_name": r.get("display_name", ""),
        "class": r.get("class", ""),
        "type": r.get("type", ""),
        "importance": r.get("importance", 0),
    }


def geocode_incident(fm: dict, cache: dict) -> dict:
    state = str(fm.get("state") or "").strip()
    body = clean_body(str(fm.get("body_of_water") or ""))
    facility = str(fm.get("facility_name") or "").strip()
    city = str(fm.get("city") or "").strip()
    county = str(fm.get("county") or "").strip()

    # Skip rubbish state values
    if state in ("True", "False", "None"):
        state = ""

    country = "canada" if state in CANADA else "usa"

    # Build query candidates in order of desirability
    queries = []
    if body and state:
        queries.append((f"{body}, {state}", "body+state"))
    if body and county and state:
        queries.append((f"{body}, {county} County, {state}", "body+county+state"))
    if facility and state:
        # Strip leading quotes if any
        f = facility.strip('"').split(",")[0]
        queries.append((f"{f}, {state}", "facility+state"))
    if city and state:
        queries.append((f"{city}, {state}", "city+state"))
    if county and state:
        queries.append((f"{county} County, {state}", "county+state"))

    for q, qtype in queries:
        key = f"{country}::{q}"
        if key in cache:
            hit = cache[key]
            if hit is not None:
                return {**hit, "query_used": q, "match_type": qtype, "from_cache": True}
            continue  # negative cache
        print(f"  -> {q}")
        time.sleep(1.1)  # Nominatim rate-limit
        res = nominatim_query(q, country)
        cache[key] = res
        save_cache(cache)
        if res:
            return {**res, "query_used": q, "match_type": qtype, "from_cache": False}

    # Final fallback: state centroid
    if state in STATE_CENTROIDS:
        lat, lon = STATE_CENTROIDS[state]
        return {
            "lat": lat, "lon": lon,
            "display_name": f"(state centroid: {state})",
            "class": "fallback", "type": "state_centroid",
            "importance": 0,
            "query_used": state,
            "match_type": "state_centroid",
            "from_cache": True,
        }

    return {
        "lat": None, "lon": None,
        "display_name": "(no location)",
        "query_used": "", "match_type": "none", "from_cache": False,
        "class": "", "type": "", "importance": 0,
    }


def main() -> None:
    cache = load_cache()
    files = sorted(DATASET.glob("ESD-*.md"))
    rows = []
    for i, p in enumerate(files, 1):
        fm = parse_frontmatter(p)
        print(f"[{i:3d}/{len(files)}] {p.name}")
        g = geocode_incident(fm, cache)
        rows.append({
            "file": p.name,
            "incident_id": fm.get("incident_id", ""),
            "date": fm.get("date", ""),
            "year": fm.get("year", ""),
            "state": fm.get("state", ""),
            "body_of_water": str(fm.get("body_of_water") or ""),
            "city": str(fm.get("city") or ""),
            "county": str(fm.get("county") or ""),
            "facility_name": str(fm.get("facility_name") or ""),
            "incident_type": fm.get("incident_type", ""),
            "fatality_count": fm.get("fatality_count", 0),
            "injury_count": fm.get("injury_count", 0),
            "near_miss_count": fm.get("near_miss_count", 0),
            "verification_level": fm.get("verification_level", ""),
            "is_freshwater_private_dock":
                str(fm.get("is_freshwater_private_dock", "")).lower() == "true",
            "is_freshwater_marina":
                str(fm.get("is_freshwater_marina", "")).lower() == "true",
            "esdpa_listed": str(fm.get("esdpa_listed", "")).lower() == "true",
            "lat": g["lat"], "lon": g["lon"],
            "query_used": g["query_used"],
            "match_type": g["match_type"],
            "display_name": g["display_name"],
            "from_cache": g.get("from_cache", False),
        })

    out_csv = OUT_DIR / "incidents_geocoded.csv"
    import csv as _csv
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = _csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\nWrote {out_csv}")

    ok = sum(1 for r in rows if r["lat"] is not None)
    body = sum(1 for r in rows if r["match_type"].startswith("body"))
    fac  = sum(1 for r in rows if r["match_type"].startswith("facility"))
    cty  = sum(1 for r in rows if r["match_type"].startswith("city"))
    cnty = sum(1 for r in rows if r["match_type"].startswith("county"))
    sc   = sum(1 for r in rows if r["match_type"] == "state_centroid")
    none = sum(1 for r in rows if r["match_type"] == "none")
    print(f"Geocoded: {ok}/{len(rows)}")
    print(f"  body_of_water match: {body}")
    print(f"  facility match:      {fac}")
    print(f"  city match:          {cty}")
    print(f"  county match:        {cnty}")
    print(f"  state-centroid:      {sc}")
    print(f"  no location:         {none}")


if __name__ == "__main__":
    main()
