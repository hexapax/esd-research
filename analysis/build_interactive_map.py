#!/usr/bin/env python3
"""
Interactive Folium map with layer toggles + heatmap overlay.

Output: analysis/outputs/map/esd_map.html

Features:
  - Base: CartoDB Positron (clean, light)
  - Layer groups: by setting (marina / private / other)
  - Layer group: heatmap (togglable)
  - Marker clusters at each lake, expand on click
  - Popup per incident with: date, location, victims, mechanism,
    verification level, source URLs
  - Fully self-contained HTML — no server required, works locally or on
    GitHub Pages
"""
from __future__ import annotations
import csv
import html as htmllib
import json
import re
from pathlib import Path

import folium
from folium import plugins

ROOT = Path("/opt/repos/esd-research")
DATASET = ROOT / "esd-dataset"
IN_CSV = ROOT / "analysis/outputs/map/incidents_geocoded.csv"
OUT = ROOT / "analysis/outputs/map"
OUT.mkdir(parents=True, exist_ok=True)

C_MARINA  = "#1B7F79"
C_PRIVATE = "#D2553A"
C_OTHER   = "#8892A6"


def load_body(path: Path) -> str:
    import yaml
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?\n)---\s*\n(.*)$", txt, re.DOTALL)
    return m.group(2) if m else txt


def load_frontmatter(path: Path) -> dict:
    import yaml
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?\n)---", txt, re.DOTALL)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def describe_victim(v: dict) -> str:
    fn = str(v.get("first_name", "")).strip()
    ln = str(v.get("last_name", "")).strip()
    age = v.get("age")
    gender = str(v.get("gender", "")).strip()
    outcome = str(v.get("outcome", "")).strip()
    role = str(v.get("role", "")).strip()
    if fn.lower() == "unknown" and ln.lower() == "unknown":
        name = "Unknown"
    else:
        name = f"{fn} {ln}".strip()
    parts = [name]
    mid = []
    if age: mid.append(str(age))
    if gender: mid.append(gender)
    if mid:
        parts.append(f"({' / '.join(mid)})")
    tail = []
    if outcome: tail.append(outcome)
    if role and role != "primary": tail.append(role)
    if tail:
        parts.append("— " + ", ".join(tail))
    return " ".join(parts)


def build_popup(fm: dict) -> str:
    loc_bits = []
    for k in ("facility_name", "body_of_water", "city", "county", "state"):
        v = fm.get(k)
        if v:
            loc_bits.append(str(v))
    loc = ", ".join(loc_bits) or "(unknown location)"

    victims = fm.get("victims") or []
    victim_lines = [describe_victim(v) for v in victims]

    sources = fm.get("sources") or []
    src_lines = []
    for s in sources[:4]:
        if not isinstance(s, dict):
            continue
        url = s.get("url", "")
        outlet = s.get("outlet", "") or s.get("type", "source")
        if url:
            src_lines.append(
                f'<a href="{htmllib.escape(url)}" target="_blank" '
                f'rel="noopener">{htmllib.escape(str(outlet))}</a>'
            )

    fatal_ct = fm.get("fatality_count", 0)
    inj_ct = fm.get("injury_count", 0)
    nm_ct = fm.get("near_miss_count", 0)
    vlevel = str(fm.get("verification_level", "")).upper()
    esdpa = "Yes" if str(fm.get("esdpa_listed", "")).lower() == "true" else "No"
    elec = str(fm.get("electrical_source", "")) or "unknown"
    fault = str(fm.get("fault_description", ""))

    date = str(fm.get("date", "")) or "(unknown date)"
    incident_id = str(fm.get("incident_id", ""))

    parts = [
        f'<div style="font-family:system-ui,sans-serif;font-size:13px;'
        f'max-width:340px;line-height:1.35;">',
        f'<div style="font-weight:700;color:#1F2A44;font-size:14px;'
        f'margin-bottom:4px;">{htmllib.escape(date)} &mdash; '
        f'{htmllib.escape(loc)}</div>',
        f'<div style="color:#55607A;margin-bottom:6px;">'
        f'Outcome: <b>{fatal_ct}</b> fatal / <b>{inj_ct}</b> injury / '
        f'<b>{nm_ct}</b> near-miss</div>',
    ]
    if victim_lines:
        parts.append('<div style="margin-bottom:6px;"><b>People:</b><br>'
                     + '<br>'.join(htmllib.escape(v) for v in victim_lines)
                     + '</div>')
    parts.append(
        f'<div style="margin-bottom:6px;">'
        f'<b>Electrical:</b> {htmllib.escape(elec)}'
        + (f'<br><i>{htmllib.escape(fault[:240])}</i>' if fault else '')
        + '</div>')
    parts.append(
        f'<div style="margin-bottom:4px;">'
        f'<b>Verification:</b> {htmllib.escape(vlevel)} &nbsp;|&nbsp; '
        f'<b>ESDPA-listed:</b> {esdpa}</div>')
    if src_lines:
        parts.append('<div style="margin-top:6px;"><b>Sources:</b> '
                     + ' &nbsp;·&nbsp; '.join(src_lines) + '</div>')
    parts.append(f'<div style="color:#8892A6;font-size:11px;'
                 f'margin-top:6px;">{htmllib.escape(incident_id)}</div>')
    parts.append('</div>')
    return ''.join(parts)


def main():
    # Load geocoded + frontmatter for popup content
    with IN_CSV.open("r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    m = folium.Map(
        location=[37.5, -95.5],
        zoom_start=5,
        tiles="CartoDB positron",
        control_scale=True,
    )

    # Title block
    title_html = '''
      <div style="position: fixed; top: 10px; left: 60px; z-index: 9999;
                  background: rgba(255,255,255,0.95); padding: 10px 16px;
                  border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.15);
                  font-family: system-ui, sans-serif; max-width: 480px;">
        <div style="font-size: 18px; font-weight: 700; color: #1F2A44;">
          Electric Shock Drowning &mdash; U.S. incidents 1981&ndash;2025
        </div>
        <div style="font-size: 12px; color: #55607A; margin-top: 2px;">
          201 independently-verified incidents. Toggle layers top-right.
          Click a pin for incident details.
        </div>
      </div>
    '''
    m.get_root().html.add_child(folium.Element(title_html))

    # Layer groups
    lg_marina = folium.FeatureGroup(name="Freshwater marina",
                                    show=True).add_to(m)
    lg_private = folium.FeatureGroup(name="Private freshwater dock",
                                     show=True).add_to(m)
    lg_other = folium.FeatureGroup(name="Other (pool, fountain, etc.)",
                                   show=True).add_to(m)

    # Use marker clusters per group so co-located incidents group
    mc_marina = plugins.MarkerCluster(disableClusteringAtZoom=9,
                                       spiderfyOnMaxZoom=True).add_to(lg_marina)
    mc_private = plugins.MarkerCluster(disableClusteringAtZoom=9,
                                        spiderfyOnMaxZoom=True).add_to(lg_private)
    mc_other = plugins.MarkerCluster(disableClusteringAtZoom=9,
                                      spiderfyOnMaxZoom=True).add_to(lg_other)

    heat_pts = []
    kept = 0

    for r in rows:
        if not r["lat"] or not r["lon"]:
            continue
        try:
            lat = float(r["lat"]); lon = float(r["lon"])
        except ValueError:
            continue

        fm_path = DATASET / r["file"]
        fm = load_frontmatter(fm_path)
        if not fm:
            continue

        is_priv = str(fm.get("is_freshwater_private_dock", "")).lower() == "true"
        is_mar  = str(fm.get("is_freshwater_marina", "")).lower() == "true"
        fat = int(r["fatality_count"] or "0") if str(r["fatality_count"]).strip().isdigit() else 0

        if is_mar:
            target_cluster = mc_marina
            color = C_MARINA
        elif is_priv:
            target_cluster = mc_private
            color = C_PRIVATE
        else:
            target_cluster = mc_other
            color = C_OTHER

        radius = 5 + 2 * min(fat, 4)

        popup = folium.Popup(build_popup(fm), max_width=380)
        folium.CircleMarker(
            location=[lat, lon],
            radius=radius,
            color="white",
            weight=1,
            fillColor=color,
            fillOpacity=0.85,
            popup=popup,
            tooltip=f"{fm.get('date', '')} — {fm.get('body_of_water', '')}",
        ).add_to(target_cluster)

        heat_pts.append([lat, lon, max(fat, 1)])
        kept += 1

    # Heatmap overlay (initially off)
    lg_heat = folium.FeatureGroup(name="Heatmap density", show=False).add_to(m)
    if heat_pts:
        plugins.HeatMap(heat_pts, radius=22, blur=28, min_opacity=0.3,
                        gradient={"0.3": "#FFF8D4", "0.5": "#FDAE61",
                                  "0.75": "#D73027", "1.0": "#7F0000"}
                        ).add_to(lg_heat)

    folium.LayerControl(collapsed=False, position="topright").add_to(m)

    # Legend (static DIV)
    legend_html = f'''
      <div style="position: fixed; bottom: 20px; left: 20px; z-index: 9999;
                  background: rgba(255,255,255,0.95); padding: 10px 14px;
                  border-radius: 6px; box-shadow: 0 1px 4px rgba(0,0,0,0.15);
                  font-family: system-ui, sans-serif; font-size: 12px;">
        <div style="font-weight:700;color:#1F2A44;margin-bottom:4px;">Legend</div>
        <div style="margin:2px 0;"><span style="display:inline-block;width:12px;
             height:12px;border-radius:50%;background:{C_MARINA};
             margin-right:6px;vertical-align:middle;"></span>Freshwater marina</div>
        <div style="margin:2px 0;"><span style="display:inline-block;width:12px;
             height:12px;border-radius:50%;background:{C_PRIVATE};
             margin-right:6px;vertical-align:middle;"></span>Private freshwater dock</div>
        <div style="margin:2px 0;"><span style="display:inline-block;width:12px;
             height:12px;border-radius:50%;background:{C_OTHER};
             margin-right:6px;vertical-align:middle;"></span>Other (pool, fountain, etc.)</div>
        <div style="margin-top:6px;color:#55607A;font-size:11px;">
          Dot size scales with fatality count.<br>
          {kept} incidents plotted (of 201 total).
        </div>
      </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))

    out_path = OUT / "esd_map.html"
    m.save(str(out_path))
    print(f"Wrote {out_path}")
    print(f"Plotted {kept} incidents.")


if __name__ == "__main__":
    main()
