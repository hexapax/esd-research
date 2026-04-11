#!/usr/bin/env python3
"""Generate presentation charts for PURE ESD incidents only.

Pure ESD = electricity leaking into a natural water body from dock/marina/boat
infrastructure causing paralysis and/or drowning. Excludes:
- Pool/fountain/splash pad (different regulatory context)
- Overhead power lines (different mechanism)
- Flood/storm water (different mechanism)
- On-land electrocution near water
"""

import yaml
import os
from collections import Counter, defaultdict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

CHART_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(os.path.dirname(CHART_DIR))
DPI = 200
BG_COLOR = '#fafafa'


def load_incidents():
    incidents = []
    for f in sorted(os.listdir(DATASET_DIR)):
        if f.startswith('ESD-') and f.endswith('.md'):
            with open(os.path.join(DATASET_DIR, f)) as fh:
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


def is_pure_esd(d):
    src = (d.get('electrical_source') or '').lower()
    wt = (d.get('water_type') or '').lower()
    fn = (d.get('facility_name') or '').lower()
    detail = (d.get('electrical_source_detail') or '').lower()
    fault = (d.get('fault_description') or '').lower()

    if wt in ('pool', 'fountain'):
        return False
    if src in ('pool_pump', 'pool_equipment'):
        return False
    if any(k in fn for k in ('pool', 'fountain', 'splash', 'waterpark', 'wave pool', 'hot tub')):
        return False
    if src == 'overhead_line':
        return False
    if 'downed' in detail or 'downed' in fault:
        return False
    if 'mast' in detail or 'sailboat' in detail:
        return False
    if 'flood' in fn or 'puddle' in fn or 'standing water' in fn:
        return False
    return True


def classify_facility(d):
    fn = (d.get('facility_name') or '').lower()
    if any(k in fn for k in ('marina', 'yacht', 'harbor', 'harbour')):
        return 'Commercial Marina'
    elif any(k in fn for k in ('private', 'residential', 'family', 'home', 'backyard')):
        return 'Residential Dock'
    else:
        return 'Unknown/Other'


def get_month(d):
    ds = d.get('date', '')
    if isinstance(ds, str) and len(ds) >= 7:
        try:
            m = int(ds[5:7])
            if 1 <= m <= 12:
                return m
        except (ValueError, IndexError):
            pass
    return None


# ============================================================
# CHART 1: Pure ESD Fatalities by Year
# ============================================================
def chart_fatalities_by_year(incidents):
    fig, ax = plt.subplots(figsize=(14, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    years = sorted(set(d.get('year') for d in incidents if d.get('year')))
    min_y, max_y = min(years), max(years)
    all_years = list(range(min_y, max_y + 1))

    fatal_vals = [0] * len(all_years)
    for d in incidents:
        y = d.get('year')
        fc = d.get('fatality_count', 0) or 0
        if y and fc > 0:
            fatal_vals[y - min_y] += fc

    x = np.arange(len(all_years))
    ax.bar(x, fatal_vals, 0.8, color='#c0392b')

    # 5-year moving average
    window = 5
    if len(fatal_vals) >= window:
        ma = []
        for i in range(len(fatal_vals)):
            start = max(0, i - window + 1)
            ma.append(sum(fatal_vals[start:i+1]) / (i - start + 1))
        ax.plot(x, ma, color='#2c3e50', linewidth=2.5, label=f'{window}-year moving average', zorder=5)

    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Fatalities', fontsize=12)
    ax.set_title('Pure ESD Fatalities by Year (Dock/Marina/Shore Power Only)\n'
                 f'151 incidents, 120 fatalities — Pool, fountain, power line incidents excluded',
                 fontsize=13, fontweight='bold')
    ax.set_xticks(x[::2])
    ax.set_xticklabels([str(y) for y in all_years[::2]], rotation=45, ha='right', fontsize=9)
    ax.legend(fontsize=10, loc='upper left')
    ax.set_xlim(-0.5, len(all_years) - 0.5)

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'pure_esd_fatalities_by_year.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 2: Pure ESD Residential vs Marina (the key divergence)
# ============================================================
def chart_residential_vs_marina(incidents):
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    bins = [(1981, 1999), (2000, 2005), (2006, 2010), (2011, 2015), (2016, 2020), (2021, 2025)]
    bin_labels = ['1981-1999', '2000-2005', '2006-2010', '2011-2015', '2016-2020', '2021-2025']

    res_binned = []
    mar_binned = []
    unk_binned = []
    for start, end in bins:
        period = [d for d in incidents if d.get('year') and start <= d['year'] <= end]
        res = sum(1 for d in period if classify_facility(d) == 'Residential Dock')
        mar = sum(1 for d in period if classify_facility(d) == 'Commercial Marina')
        unk = len(period) - res - mar
        res_binned.append(res)
        mar_binned.append(mar)
        unk_binned.append(unk)

    x = np.arange(len(bin_labels))
    width = 0.25

    bars_r = ax.bar(x - width, res_binned, width, color='#e74c3c', label='Residential/Private Dock', edgecolor='white')
    bars_m = ax.bar(x, mar_binned, width, color='#3498db', label='Commercial Marina/Yacht Club', edgecolor='white')
    bars_u = ax.bar(x + width, unk_binned, width, color='#bdc3c7', label='Unknown/Other', edgecolor='white')

    ax.set_xlabel('Time Period', fontsize=12)
    ax.set_ylabel('Number of Pure ESD Incidents', fontsize=12)
    ax.set_title('Pure ESD: Residential Dock vs Commercial Marina Incidents\n'
                 'Marina incidents declining after NEC 555 reforms; residential docks unregulated',
                 fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(bin_labels, fontsize=11)
    ax.legend(fontsize=10, loc='upper left')

    # NEC markers
    ax.axvline(x=2.7, color='green', linestyle='--', alpha=0.6, linewidth=2)
    ax.text(2.75, max(max(res_binned), max(mar_binned), max(unk_binned)) * 0.95,
            'NEC 555\n100mA GFPE\n(2011)', fontsize=8, color='green', va='top')
    ax.axvline(x=3.7, color='darkgreen', linestyle=':', alpha=0.6, linewidth=2)
    ax.text(3.75, max(max(res_binned), max(mar_binned), max(unk_binned)) * 0.85,
            'NEC 555\n30mA GFPE\n(2017)', fontsize=8, color='darkgreen', va='top')

    # Value labels
    for bars in [bars_r, bars_m, bars_u]:
        for bar in bars:
            h = bar.get_height()
            if h > 0:
                ax.text(bar.get_x() + bar.get_width()/2, h + 0.2, str(int(h)),
                        ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'pure_esd_residential_vs_marina.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 3: Pure ESD Monthly Distribution
# ============================================================
def chart_monthly(incidents):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    months_fatal = Counter()
    months_nonfatal = Counter()
    for d in incidents:
        m = get_month(d)
        if m:
            if (d.get('fatality_count', 0) or 0) > 0:
                months_fatal[m] += 1
            else:
                months_nonfatal[m] += 1

    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    x = np.arange(12)
    fatal_vals = [months_fatal.get(m + 1, 0) for m in range(12)]
    nonfatal_vals = [months_nonfatal.get(m + 1, 0) for m in range(12)]

    ax.bar(x, fatal_vals, 0.8, color='#c0392b', label='Fatal')
    ax.bar(x, nonfatal_vals, 0.8, bottom=fatal_vals, color='#f1c40f', label='Non-fatal/near-miss')

    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Number of Pure ESD Incidents', fontsize=12)
    ax.set_title('Pure ESD: Seasonal Distribution\n'
                 f'July = {fatal_vals[6] + nonfatal_vals[6]} of {len(incidents)} incidents '
                 f'({(fatal_vals[6] + nonfatal_vals[6]) * 100 // len(incidents)}%)',
                 fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(month_names, fontsize=11)
    ax.legend(fontsize=10)
    ax.axvspan(3.5, 7.5, alpha=0.08, color='red')

    # July annotation
    jul_total = fatal_vals[6] + nonfatal_vals[6]
    ax.annotate(f'July: {jul_total} incidents\n(34% of all ESD)',
                xy=(6, jul_total), xytext=(8, jul_total * 0.8),
                fontsize=10, fontweight='bold', color='#c0392b',
                arrowprops=dict(arrowstyle='->', color='#c0392b'))

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'pure_esd_monthly.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 4: Pure ESD Key Stats Hero Slide
# ============================================================
def chart_key_stats(incidents):
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    ax.axis('off')

    total = len(incidents)
    fatal = sum(d.get('fatality_count', 0) or 0 for d in incidents)
    fatal_incidents = sum(1 for d in incidents if d.get('incident_type') == 'fatal')
    states_count = len(set(d.get('state') for d in incidents if d.get('state')))

    # Residential vs marina
    res = sum(1 for d in incidents if classify_facility(d) == 'Residential Dock')
    mar = sum(1 for d in incidents if classify_facility(d) == 'Commercial Marina')

    stats = [
        ('151', 'Pure ESD\nIncidents'),
        ('120', 'Dock/Marina\nFatalities'),
        (f'{res}', 'At Residential\nDocks'),
        (f'{mar}', 'At Commercial\nMarinas'),
        ('0', 'States Require\nResidential Dock\nInspections'),
    ]

    for i, (num, label) in enumerate(stats):
        x = 0.1 + i * 0.19
        color = '#e74c3c' if i == 4 else 'white'
        ax.text(x, 0.62, num, transform=ax.transAxes, fontsize=38,
                fontweight='bold', color=color, ha='center', va='center')
        ax.text(x, 0.33, label, transform=ax.transAxes, fontsize=11,
                color='#8899aa', ha='center', va='center', linespacing=1.3)

    ax.text(0.5, 0.92, 'Electric Shock Drowning: Pure Dock/Marina Incidents', transform=ax.transAxes,
            fontsize=20, fontweight='bold', color='white', ha='center')
    ax.text(0.5, 0.82, 'Excludes pools, fountains, splash pads, overhead power lines, and flood/storm incidents',
            transform=ax.transAxes, fontsize=10, color='#667788', ha='center')

    ax.text(0.5, 0.12, 'Marina incidents declining after NEC 555 reforms (2011-2017)',
            transform=ax.transAxes, fontsize=10, color='#3498db', ha='center')
    ax.text(0.5, 0.05, 'Residential dock incidents are NOT declining — no state requires inspection of private docks',
            transform=ax.transAxes, fontsize=10, color='#e74c3c', ha='center')

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'pure_esd_key_stats.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 5: Electrical Source for Pure ESD
# ============================================================
def chart_electrical_source(incidents):
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    sources = Counter(d.get('electrical_source', 'unknown') for d in incidents)
    labels_map = {
        'dock_wiring': 'Dock Wiring', 'shore_power': 'Shore Power',
        'boat_lift': 'Boat Lift', 'extension_cord': 'Extension Cord',
        'charger': 'Battery Charger', 'other': 'Other', 'unknown': 'Unknown',
    }
    colors_list = ['#c0392b', '#e74c3c', '#e67e22', '#f39c12', '#f1c40f', '#95a5a6', '#bdc3c7']

    sorted_src = sorted(sources.items(), key=lambda x: -x[1])
    labels = [labels_map.get(s, s) for s, _ in sorted_src]
    vals = [c for _, c in sorted_src]

    bars = ax.barh(range(len(labels)), vals, color=colors_list[:len(labels)])
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=11)
    ax.set_xlabel('Number of Incidents', fontsize=12)
    ax.set_title('Pure ESD: Electrical Source\n'
                 'Dock wiring faults are the #1 cause',
                 fontsize=13, fontweight='bold')
    ax.invert_yaxis()

    for bar, v in zip(bars, vals):
        pct = v * 100 // len(incidents)
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                f'{v} ({pct}%)', va='center', fontsize=10)

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'pure_esd_electrical_source.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
# CHART 6: Pure ESD Incidents by Period (trend line)
# ============================================================
def chart_period_trend(incidents):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor(BG_COLOR)

    bins = [(2000, 2005), (2006, 2010), (2011, 2015), (2016, 2020), (2021, 2025)]
    bin_labels = ['2000-\n2005', '2006-\n2010', '2011-\n2015', '2016-\n2020', '2021-\n2025*']

    # Per-period incident rate (normalized to per-year)
    inc_rate = []
    death_rate = []
    for start, end in bins:
        period = [d for d in incidents if d.get('year') and start <= d['year'] <= end]
        years_in_bin = end - start + 1
        if end == 2025:
            years_in_bin = 4.3  # partial year
        inc_rate.append(len(period) / years_in_bin)
        deaths = sum(d.get('fatality_count', 0) or 0 for d in period)
        death_rate.append(deaths / years_in_bin)

    x = np.arange(len(bin_labels))

    ax1.set_facecolor(BG_COLOR)
    ax1.bar(x, inc_rate, 0.6, color='#2980b9')
    ax1.plot(x, inc_rate, 'o-', color='#2c3e50', linewidth=2, markersize=8, zorder=5)
    ax1.set_xticks(x)
    ax1.set_xticklabels(bin_labels, fontsize=10)
    ax1.set_ylabel('Incidents per Year', fontsize=12)
    ax1.set_title('Pure ESD: Incident Rate\n(incidents per year by period)', fontsize=13, fontweight='bold')
    for i, v in enumerate(inc_rate):
        ax1.text(i, v + 0.1, f'{v:.1f}', ha='center', fontsize=10, fontweight='bold')

    ax2.set_facecolor(BG_COLOR)
    ax2.bar(x, death_rate, 0.6, color='#c0392b')
    ax2.plot(x, death_rate, 'o-', color='#2c3e50', linewidth=2, markersize=8, zorder=5)
    ax2.set_xticks(x)
    ax2.set_xticklabels(bin_labels, fontsize=10)
    ax2.set_ylabel('Deaths per Year', fontsize=12)
    ax2.set_title('Pure ESD: Fatality Rate\n(deaths per year by period)', fontsize=13, fontweight='bold')
    for i, v in enumerate(death_rate):
        ax2.text(i, v + 0.1, f'{v:.1f}', ha='center', fontsize=10, fontweight='bold')

    ax2.text(4, death_rate[-1] + 0.8, '* 2021-2025\npartial data', fontsize=8, color='gray', ha='center')

    plt.tight_layout()
    path = os.path.join(CHART_DIR, 'pure_esd_period_trend.png')
    fig.savefig(path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {path}')


# ============================================================
if __name__ == '__main__':
    print('Loading incidents...')
    all_incidents = load_incidents()
    incidents = [d for d in all_incidents if is_pure_esd(d)]
    excluded = len(all_incidents) - len(incidents)
    print(f'Loaded {len(all_incidents)} total, {len(incidents)} pure ESD ({excluded} excluded)\n')

    print('Generating pure ESD charts...')
    chart_fatalities_by_year(incidents)
    chart_residential_vs_marina(incidents)
    chart_monthly(incidents)
    chart_key_stats(incidents)
    chart_electrical_source(incidents)
    chart_period_trend(incidents)

    print(f'\nDone! 6 pure ESD charts saved to {CHART_DIR}/')
