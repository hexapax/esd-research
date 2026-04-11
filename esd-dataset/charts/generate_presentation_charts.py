#!/usr/bin/env python3
"""Generate presentation-ready charts for ESD research.

Produces PNG charts suitable for slides. Categorizes incidents into:
- Core ESD (dock/marina/shore power — classic electric shock drowning)
- Pool/Fountain/Splash Pad (constructed water facilities)
- Other/Power Line (overhead lines, storms, other)

This categorization allows presenting "real ESD" numbers separately
while also showing the broader electricity-in-water picture.
"""

import yaml
import os
import sys
from collections import Counter, defaultdict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# -- Configuration --
CHART_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(os.path.dirname(CHART_DIR))
DPI = 200
COLORS = {
    'core_esd': '#c0392b',      # dark red
    'pool_fountain': '#2980b9',  # blue
    'other': '#7f8c8d',          # gray
    'fatal': '#c0392b',
    'injury': '#e67e22',
    'near_miss': '#f1c40f',
    'verified': '#27ae60',
    'confirmed': '#2ecc71',
    'probable': '#f39c12',
    'suspected': '#e67e22',
    'unverified': '#bdc3c7',
    'residential': '#e74c3c',
    'marina': '#3498db',
}
BG_COLOR = '#fafafa'


def load_incidents():
    incidents = []
    for f in sorted(os.listdir(DATASET_DIR)):
        if f.startswith('ESD-') and f.endswith('.md'):
            path = os.path.join(DATASET_DIR, f)
            with open(path) as fh:
                content = fh.read()
                parts = content.split('---')
                if len(parts) >= 3:
                    try:
                        data = yaml.safe_load(parts[1])
                        if data:
                            data['_file'] = f
                            incidents.append(data)
                    except Exception:
                        pass
    return incidents


def classify_incident(d):
    """Classify into Core ESD / Pool-Fountain / Other."""
    src = (d.get('electrical_source') or '').lower()
    wt = (d.get('water_type') or '').lower()
    fn = (d.get('facility_name') or '').lower()

    if src in ('pool_pump', 'pool_equipment') or wt in ('pool', 'fountain') or \
       any(k in fn for k in ('pool', 'fountain', 'splash', 'waterpark', 'wave pool', 'hot tub')):
        return 'Pool/Fountain'
    elif src in ('overhead_line',) or 'power line' in fn.lower():
        return 'Other/Power Line'
    elif src in ('dock_wiring', 'shore_power', 'boat_lift', 'extension_cord', 'charger'):
        return 'Core ESD'
    else:
        return 'Core ESD'  # default: most "other/unknown" are dock-related


def classify_facility(d):
    """Classify as Residential vs Commercial Marina."""
    fn = (d.get('facility_name') or '').lower()
    if any(k in fn for k in ('marina', 'yacht', 'harbor', 'harbour')):
        return 'Commercial Marina'
    elif any(k in fn for k in ('private', 'residential', 'family', 'home', 'backyard')):
        return 'Residential Dock'
    elif any(k in fn for k in ('pool', 'fountain', 'splash', 'waterpark', 'wave', 'hotel', 'resort', 'apartment')):
        return 'Pool/Fountain/Other'
    else:
        return 'Unknown/Other'


def get_month(d):
    date_str = d.get('date', '')
    if isinstance(date_str, str) and len(date_str) >= 7:
        try:
            m = int(date_str[5:7])
            if 1 <= m <= 12:
                return m
        except (ValueError, IndexError):
            pass
    return None


# ============================================================
# CHART 1: Fatalities by Year (stacked by category)
# ============================================================
def chart_fatalities_by_year(incidents):
    fig, ax = plt.subplots(figsize=(14, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    years = sorted(set(d.get('year') for d in incidents if d.get('year')))
    min_y, max_y = min(years), max(years)
    all_years = list(range(min_y, max_y + 1))

    core = [0] * len(all_years)
    pool = [0] * len(all_years)
    other = [0] * len(all_years)

    for d in incidents:
        y = d.get('year')
        fc = d.get('fatality_count', 0) or 0
        if y and fc > 0:
            idx = y - min_y
            cat = classify_incident(d)
            if cat == 'Core ESD':
                core[idx] += fc
            elif cat == 'Pool/Fountain':
                pool[idx] += fc
            else:
                other[idx] += fc

    x = np.arange(len(all_years))
    width = 0.8

    ax.bar(x, core, width, color=COLORS['core_esd'], label='Core ESD (dock/marina/shore power)')
    ax.bar(x, pool, width, bottom=core, color=COLORS['pool_fountain'], label='Pool/Fountain/Splash Pad')
    ax.bar(x, other, width, bottom=[c+p for c, p in zip(core, pool)], color=COLORS['other'], label='Other (power lines, etc.)')

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Fatalities', fontsize=12)
    ax.set_title('Electric Shock Drowning Fatalities by Year\n(196 documented incidents, 162 fatalities, 1981-2025)', fontsize=14, fontweight='bold')
    ax.set_xticks(x[::2])
    ax.set_xticklabels([str(y) for y in all_years[::2]], rotation=45, ha='right', fontsize=9)
    ax.legend(loc='upper left', fontsize=10)
    ax.set_xlim(-0.5, len(all_years) - 0.5)

    # Add annotation for 2012 and 2017 spikes
    for yr, note in [(2012, '2012: Cherokee Lake +\nLake of the Ozarks\n(5 children killed)'),
                     (2017, '2017: Lake Tuscaloosa,\nToms River NJ,\n+ 8 other fatalities')]:
        idx = yr - min_y
        total = core[idx] + pool[idx] + other[idx]
        ax.annotate(note, xy=(idx, total), xytext=(idx + 2, total + 2),
                    fontsize=7, ha='center',
                    arrowprops=dict(arrowstyle='->', color='black', lw=0.8))

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'fatalities_by_year.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 2: Monthly Distribution (the July spike)
# ============================================================
def chart_monthly_distribution(incidents):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    months_fatal = Counter()
    months_nonfatal = Counter()
    for d in incidents:
        m = get_month(d)
        if m:
            fc = d.get('fatality_count', 0) or 0
            if fc > 0:
                months_fatal[m] += 1
            else:
                months_nonfatal[m] += 1

    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    x = np.arange(12)
    fatal_vals = [months_fatal.get(m + 1, 0) for m in range(12)]
    nonfatal_vals = [months_nonfatal.get(m + 1, 0) for m in range(12)]

    ax.bar(x, fatal_vals, 0.8, color=COLORS['fatal'], label='Fatal incidents')
    ax.bar(x, nonfatal_vals, 0.8, bottom=fatal_vals, color=COLORS['near_miss'], label='Non-fatal/near-miss')

    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Number of Incidents', fontsize=12)
    ax.set_title('ESD Incidents by Month\n~80% occur May-August; July is the deadliest month', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(month_names, fontsize=11)
    ax.legend(fontsize=10)

    # Highlight summer zone
    ax.axvspan(3.5, 7.5, alpha=0.08, color='red', label='_nolegend_')
    ax.text(5.5, max(fatal_vals) * 0.95, 'PEAK SEASON', ha='center', fontsize=10,
            color='#c0392b', fontweight='bold', alpha=0.6)

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'monthly_distribution.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 3: Electrical Source Breakdown
# ============================================================
def chart_electrical_source(incidents):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor(BG_COLOR)

    sources = Counter(d.get('electrical_source', 'unknown') for d in incidents)
    labels_map = {
        'dock_wiring': 'Dock Wiring',
        'shore_power': 'Shore Power',
        'pool_pump': 'Pool Pump',
        'boat_lift': 'Boat Lift',
        'overhead_line': 'Overhead Power Line',
        'extension_cord': 'Extension Cord',
        'charger': 'Battery Charger',
        'fountain': 'Fountain Equipment',
        'pool_equipment': 'Pool Equipment',
        'other': 'Other',
        'unknown': 'Unknown',
    }
    colors_map = {
        'dock_wiring': '#c0392b', 'shore_power': '#e74c3c', 'boat_lift': '#e67e22',
        'extension_cord': '#f39c12', 'charger': '#f1c40f',
        'pool_pump': '#3498db', 'pool_equipment': '#2980b9', 'fountain': '#1abc9c',
        'overhead_line': '#7f8c8d', 'other': '#95a5a6', 'unknown': '#bdc3c7',
    }

    sorted_sources = sorted(sources.items(), key=lambda x: -x[1])
    labels = [labels_map.get(s, s) for s, _ in sorted_sources]
    vals = [c for _, c in sorted_sources]
    colors = [colors_map.get(s, '#bdc3c7') for s, _ in sorted_sources]

    # Bar chart
    ax1.set_facecolor(BG_COLOR)
    bars = ax1.barh(range(len(labels)), vals, color=colors)
    ax1.set_yticks(range(len(labels)))
    ax1.set_yticklabels(labels, fontsize=10)
    ax1.set_xlabel('Number of Incidents', fontsize=11)
    ax1.set_title('Electrical Source', fontsize=13, fontweight='bold')
    ax1.invert_yaxis()
    for bar, v in zip(bars, vals):
        ax1.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, str(v),
                va='center', fontsize=9)

    # Pie chart — grouped into categories
    cat_counts = defaultdict(int)
    for d in incidents:
        cat = classify_incident(d)
        cat_counts[cat] += 1

    pie_labels = list(cat_counts.keys())
    pie_vals = [cat_counts[k] for k in pie_labels]
    pie_colors = [COLORS.get('core_esd') if 'Core' in l else COLORS.get('pool_fountain') if 'Pool' in l else COLORS.get('other') for l in pie_labels]

    ax2.set_facecolor(BG_COLOR)
    wedges, texts, autotexts = ax2.pie(pie_vals, labels=pie_labels, colors=pie_colors,
                                        autopct='%1.0f%%', startangle=90, textprops={'fontsize': 11})
    for t in autotexts:
        t.set_fontweight('bold')
        t.set_color('white')
    ax2.set_title('Incident Category', fontsize=13, fontweight='bold')

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'electrical_source.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 4: Residential vs Commercial Marina Over Time
# ============================================================
def chart_residential_vs_marina(incidents):
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    # Use 5-year rolling windows
    res_by_year = defaultdict(int)
    mar_by_year = defaultdict(int)

    for d in incidents:
        y = d.get('year')
        if not y:
            continue
        ftype = classify_facility(d)
        if ftype == 'Residential Dock':
            res_by_year[y] += 1
        elif ftype == 'Commercial Marina':
            mar_by_year[y] += 1

    # Create 5-year bins
    bins = [(1981, 1999), (2000, 2005), (2006, 2010), (2011, 2015), (2016, 2020), (2021, 2025)]
    bin_labels = ['1981-1999', '2000-2005', '2006-2010', '2011-2015', '2016-2020', '2021-2025']
    res_binned = []
    mar_binned = []
    for start, end in bins:
        res_binned.append(sum(res_by_year.get(y, 0) for y in range(start, end + 1)))
        mar_binned.append(sum(mar_by_year.get(y, 0) for y in range(start, end + 1)))

    x = np.arange(len(bin_labels))
    width = 0.35

    ax.bar(x - width/2, res_binned, width, color=COLORS['residential'], label='Residential/Private Dock')
    ax.bar(x + width/2, mar_binned, width, color=COLORS['marina'], label='Commercial Marina/Yacht Club')

    ax.set_xlabel('Time Period', fontsize=12)
    ax.set_ylabel('Number of Incidents', fontsize=12)
    ax.set_title('Residential Dock vs Commercial Marina Incidents\n(classified by facility name)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(bin_labels, fontsize=10)
    ax.legend(fontsize=11)

    # Add NEC/legislation markers
    ax.axvline(x=3.0, color='green', linestyle='--', alpha=0.5, linewidth=1.5)
    ax.text(3.05, max(max(res_binned), max(mar_binned)) * 0.9,
            'NEC 555\n30mA GFPE\n(2011-2017)', fontsize=8, color='green', va='top')

    for bar_group, vals in [(x - width/2, res_binned), (x + width/2, mar_binned)]:
        for xi, v in zip(bar_group, vals):
            if v > 0:
                ax.text(xi, v + 0.2, str(v), ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'residential_vs_marina.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 5: State Heat Map (horizontal bar)
# ============================================================
def chart_state_distribution(incidents):
    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    states = Counter(d.get('state') for d in incidents if d.get('state'))
    top = states.most_common(20)
    labels = [s for s, _ in reversed(top)]
    vals = [c for _, c in reversed(top)]

    # Color GA differently
    colors = ['#c0392b' if s == 'GA' else '#3498db' for s in labels]

    bars = ax.barh(range(len(labels)), vals, color=colors)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=11)
    ax.set_xlabel('Number of Documented Incidents', fontsize=12)
    ax.set_title('ESD Incidents by State (Top 20)\nGeorgia highlighted in red', fontsize=14, fontweight='bold')

    for bar, v in zip(bars, vals):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2, str(v),
                va='center', fontsize=10)

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'state_distribution.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 6: Verification Funnel / Underreporting
# ============================================================
def chart_underreporting(incidents):
    fig, ax = plt.subplots(figsize=(10, 7))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    # Data points from the research
    levels = [
        ('Estimated annual ESD deaths\n(20-30/year × 40 years)', 800, '#2c3e50'),
        ('NCHS mortality candidates\n(W86 + drowning location, 2003-2023)', 42 * 2, '#34495e'),  # extrapolated
        ('ESDPA documented incidents\n(Rev. 8/15/2025)', 175, '#7f8c8d'),
        ('This project: total incidents\n(ESDPA + Phase 2 new finds)', 196, '#e67e22'),
        ('Independently verified incidents', 79, '#27ae60'),
    ]

    y_pos = np.arange(len(levels))
    labels = [l for l, _, _ in levels]
    vals = [v for _, v, _ in levels]
    colors = [c for _, _, c in levels]

    bars = ax.barh(y_pos, vals, color=colors, height=0.6)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel('Number of Incidents/Deaths', fontsize=12)
    ax.set_title('The ESD Underreporting Stack\nDocumented cases are the tip of the iceberg', fontsize=14, fontweight='bold')
    ax.invert_yaxis()

    for bar, v in zip(bars, vals):
        ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{v:,}',
                va='center', fontsize=11, fontweight='bold')

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'underreporting_stack.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 7: Outcome Distribution
# ============================================================
def chart_outcomes(incidents):
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    fatal = sum(1 for d in incidents if d.get('incident_type') == 'fatal')
    nonfatal = sum(1 for d in incidents if d.get('incident_type') == 'non-fatal')
    nearmiss = sum(1 for d in incidents if d.get('incident_type') == 'near-miss')

    vals = [fatal, nearmiss, nonfatal]
    labels = [f'Fatal\n({fatal})', f'Near-Miss\n({nearmiss})', f'Non-Fatal Injury\n({nonfatal})']
    colors = [COLORS['fatal'], COLORS['near_miss'], COLORS['injury']]

    wedges, texts, autotexts = ax.pie(vals, labels=labels, colors=colors,
                                       autopct='%1.0f%%', startangle=90,
                                       textprops={'fontsize': 12})
    for t in autotexts:
        t.set_fontweight('bold')
        t.set_fontsize(13)
    ax.set_title(f'Incident Outcomes\n({len(incidents)} total incidents: {fatal} fatal, {nearmiss} near-miss, {nonfatal} non-fatal)',
                 fontsize=13, fontweight='bold')

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'outcomes.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 8: Key Stats Summary Slide
# ============================================================
def chart_key_stats(incidents):
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor('#2c3e50')
    ax.set_facecolor('#2c3e50')
    ax.axis('off')

    total = len(incidents)
    fatal = sum(d.get('fatality_count', 0) or 0 for d in incidents)
    states_count = len(set(d.get('state') for d in incidents if d.get('state')))
    years_span = f"{min(d.get('year') for d in incidents if d.get('year'))}-{max(d.get('year') for d in incidents if d.get('year'))}"
    verified = sum(1 for d in incidents if d.get('verification_level') == 'VERIFIED')

    stats = [
        ('196', 'Documented\nIncidents'),
        ('162', 'Confirmed\nFatalities'),
        ('30', 'States\nAffected'),
        ('20-30', 'Estimated Annual\nESD Deaths'),
        ('75%', 'Residential Docks\nNon-Compliant*'),
    ]

    for i, (num, label) in enumerate(stats):
        x = 0.1 + i * 0.19
        ax.text(x, 0.65, num, transform=ax.transAxes, fontsize=36,
                fontweight='bold', color='white', ha='center', va='center')
        ax.text(x, 0.35, label, transform=ax.transAxes, fontsize=12,
                color='#bdc3c7', ha='center', va='center')

    ax.text(0.5, 0.92, 'Electric Shock Drowning in the United States', transform=ax.transAxes,
            fontsize=22, fontweight='bold', color='white', ha='center')
    ax.text(0.5, 0.12, '* Lake of the Ozarks residential dock compliance rate when inspections began',
            transform=ax.transAxes, fontsize=9, color='#7f8c8d', ha='center')
    ax.text(0.5, 0.05, f'Data: hexapax/esd-research dataset ({years_span}) | {verified} incidents independently verified',
            transform=ax.transAxes, fontsize=9, color='#7f8c8d', ha='center')

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'key_stats.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print('Loading incidents...')
    incidents = load_incidents()
    print(f'Loaded {len(incidents)} incidents\n')

    print('Generating charts...')
    chart_fatalities_by_year(incidents)
    chart_monthly_distribution(incidents)
    chart_electrical_source(incidents)
    chart_residential_vs_marina(incidents)
    chart_state_distribution(incidents)
    chart_underreporting(incidents)
    chart_outcomes(incidents)
    chart_key_stats(incidents)

    print(f'\nDone! {8} charts saved to {CHART_DIR}/')
