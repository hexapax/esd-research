#!/usr/bin/env python3
"""
Static US map PNGs:
  - map_points_16x9.png        : incident dots colored by setting, sized by fatality
  - map_heat_16x9.png          : hex-bin density overlay + dots

Uses matplotlib only (no geopandas/cartopy) by parsing a US-states GeoJSON and
drawing each polygon as matplotlib Path. AK/HI handled as insets (if present in
data — none are in our dataset, so we'll skip).

Output: analysis/outputs/map/*.png
"""
from __future__ import annotations
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch

ROOT = Path("/opt/repos/esd-research")
GEOJSON = ROOT / "analysis/us_states.geojson"
IN_CSV = ROOT / "analysis/outputs/map/incidents_geocoded.csv"
OUT = ROOT / "analysis/outputs/map"
OUT.mkdir(parents=True, exist_ok=True)

# ---- Visual system (matches presentation charts) ----
C_MARINA  = "#1B7F79"
C_PRIVATE = "#D2553A"
C_OTHER   = "#8892A6"
C_DARK    = "#1F2A44"
C_MID     = "#55607A"
C_MUTED   = "#8892A6"
C_STATE_FILL   = "#F3F1EC"
C_STATE_EDGE   = "#BCC1CC"
C_OCEAN        = "#FFFFFF"


def load_states():
    gj = json.loads(GEOJSON.read_text(encoding="utf-8"))
    states = []
    for feat in gj["features"]:
        name = feat["properties"]["name"]
        geom = feat["geometry"]
        polys = []
        if geom["type"] == "Polygon":
            polys = [geom["coordinates"]]
        elif geom["type"] == "MultiPolygon":
            polys = geom["coordinates"]
        for poly in polys:
            outer = poly[0]
            states.append({"name": name, "coords": outer})
    return states


def load_incidents():
    with IN_CSV.open("r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        if not r["lat"] or not r["lon"]:
            continue
        try:
            lat = float(r["lat"]); lon = float(r["lon"])
        except ValueError:
            continue
        if lat < 20 or lat > 55 or lon < -130 or lon > -60:
            # drop outliers (Canada & off-map for contiguous-US chart)
            continue
        is_priv = r["is_freshwater_private_dock"].strip().lower() == "true"
        is_mar  = r["is_freshwater_marina"].strip().lower() == "true"
        try:
            fat = int(r["fatality_count"] or "0")
        except ValueError:
            fat = 0
        try:
            year = int(r["year"]) if r["year"].strip().isdigit() else None
        except ValueError:
            year = None
        out.append({
            "lat": lat, "lon": lon,
            "setting": "marina" if is_mar else ("private" if is_priv else "other"),
            "fatality_count": fat,
            "incident_type": r["incident_type"],
            "year": year,
            "verification_level": r["verification_level"],
            "state": r["state"],
            "body_of_water": r["body_of_water"],
        })
    return out


def draw_basemap(ax, states):
    ax.set_facecolor(C_OCEAN)
    for s in states:
        xs = [c[0] for c in s["coords"]]
        ys = [c[1] for c in s["coords"]]
        ax.fill(xs, ys, facecolor=C_STATE_FILL,
                edgecolor=C_STATE_EDGE, linewidth=0.6, zorder=1)
    ax.set_xlim(-125, -66.5)
    ax.set_ylim(24, 50)
    ax.set_aspect("equal")
    ax.axis("off")


def size_for_fatality(n):
    if n == 0:
        return 28
    if n == 1:
        return 55
    if n == 2:
        return 90
    return 135  # 3+


def build_points_map(states, incidents):
    fig, ax = plt.subplots(figsize=(13.33, 7.5), dpi=300)
    draw_basemap(ax, states)

    buckets = {
        "marina": {"color": C_MARINA, "label": "Freshwater marina",
                   "points": []},
        "private": {"color": C_PRIVATE, "label": "Private freshwater dock",
                    "points": []},
        "other": {"color": C_OTHER, "label": "Other (pool, fountain, etc.)",
                  "points": []},
    }
    for inc in incidents:
        buckets[inc["setting"]]["points"].append(inc)

    # Draw other first so it sits under, then private, then marina on top
    for key in ("other", "private", "marina"):
        pts = buckets[key]["points"]
        if not pts:
            continue
        xs = [p["lon"] for p in pts]
        ys = [p["lat"] for p in pts]
        sz = [size_for_fatality(p["fatality_count"]) for p in pts]
        ax.scatter(xs, ys, s=sz,
                   c=buckets[key]["color"], alpha=0.75,
                   edgecolors="white", linewidths=0.6, zorder=5,
                   label=buckets[key]["label"])

    # Legend
    handles = []
    for key in ("marina", "private", "other"):
        b = buckets[key]
        handles.append(plt.Line2D([0], [0], marker="o", color="w",
                                  markerfacecolor=b["color"],
                                  markeredgecolor="white", markersize=11,
                                  label=b["label"] +
                                        f"  (n={len(b['points'])})"))
    # Size legend (append)
    handles.append(plt.Line2D([0], [0], marker="o", color="w",
                              markerfacecolor=C_MID,
                              markeredgecolor="white", markersize=5.5,
                              label="0 fatal (near-miss)"))
    handles.append(plt.Line2D([0], [0], marker="o", color="w",
                              markerfacecolor=C_MID,
                              markeredgecolor="white", markersize=7.5,
                              label="1 fatal"))
    handles.append(plt.Line2D([0], [0], marker="o", color="w",
                              markerfacecolor=C_MID,
                              markeredgecolor="white", markersize=10,
                              label="2 fatal"))
    handles.append(plt.Line2D([0], [0], marker="o", color="w",
                              markerfacecolor=C_MID,
                              markeredgecolor="white", markersize=12,
                              label="3+ fatal"))
    ax.legend(handles=handles, loc="lower left", frameon=True,
              framealpha=0.95, edgecolor=C_STATE_EDGE,
              fontsize=10, ncol=1)

    fig.suptitle("Electric Shock Drowning in the United States",
                 fontsize=22, fontweight="bold", color=C_DARK,
                 x=0.02, y=0.97, ha="left")
    ax.text(-124.5, 50.8,
            "Every documented ESD incident, 1981-2025 "
            f"(n={len(incidents)}). Colors = setting. Dot size = fatalities.",
            fontsize=12, color=C_MID, ha="left", va="top",
            transform=ax.transData)
    fig.text(0.02, 0.02,
             "Source: esd-research project dataset, 201 independently-verified "
             "incidents merged from ESDPA + LOA1-LOA14 phase-2 research.",
             fontsize=9, color=C_MUTED, ha="left")

    fig.tight_layout(rect=[0.0, 0.02, 1.0, 0.96])
    fig.savefig(OUT / "map_points_16x9.png", dpi=300, facecolor="white",
                bbox_inches="tight")
    fig.savefig(OUT / "map_points_4x3.png", dpi=300, facecolor="white",
                bbox_inches="tight")
    plt.close(fig)
    print("Wrote map_points_16x9.png and map_points_4x3.png")


def build_heat_map(states, incidents):
    import numpy as np
    fig, ax = plt.subplots(figsize=(13.33, 7.5), dpi=300)
    draw_basemap(ax, states)

    xs = [i["lon"] for i in incidents]
    ys = [i["lat"] for i in incidents]

    # Hexbin density overlay behind points
    hb = ax.hexbin(xs, ys, gridsize=40, cmap="YlOrRd",
                   mincnt=1, alpha=0.55, zorder=2, linewidths=0.0)
    cb = fig.colorbar(hb, ax=ax, shrink=0.6, pad=0.02,
                      label="Incidents per hex cell")
    cb.ax.tick_params(labelsize=9)

    # Dots overlay
    for inc in incidents:
        color = {"marina": C_MARINA, "private": C_PRIVATE,
                 "other": C_OTHER}[inc["setting"]]
        ax.plot(inc["lon"], inc["lat"], "o",
                markersize=4 + 2 * min(inc["fatality_count"], 3),
                color=color, alpha=0.85,
                markeredgecolor="white", markeredgewidth=0.4, zorder=5)

    fig.suptitle("ESD incident density across the United States",
                 fontsize=22, fontweight="bold", color=C_DARK,
                 x=0.02, y=0.97, ha="left")
    ax.text(-124.5, 50.8,
            f"Hexbin density + individual dots. n={len(incidents)} incidents "
            "1981-2025.",
            fontsize=12, color=C_MID, ha="left", va="top",
            transform=ax.transData)
    fig.text(0.02, 0.02,
             "Clustering reflects both where ESDs occur and where they are "
             "reported — TX, MO, KY, GA, FL are visible hot zones.",
             fontsize=9, color=C_MUTED, ha="left")
    fig.tight_layout(rect=[0.0, 0.02, 1.0, 0.96])
    fig.savefig(OUT / "map_heat_16x9.png", dpi=300, facecolor="white",
                bbox_inches="tight")
    fig.savefig(OUT / "map_heat_4x3.png", dpi=300, facecolor="white",
                bbox_inches="tight")
    plt.close(fig)
    print("Wrote map_heat_16x9.png and map_heat_4x3.png")


def main():
    states = load_states()
    incidents = load_incidents()
    print(f"Loaded {len(incidents)} incidents with usable coordinates "
          f"(of 201 total).")
    build_points_map(states, incidents)
    build_heat_map(states, incidents)


if __name__ == "__main__":
    main()
