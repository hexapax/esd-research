# ESD Dataset Audit Inventory

_Generated across **201** incident files in `esd-dataset/`._

## 1. Provenance

| Group | Count | % |
|---|---:|---:|
| From ESDPA list | 175 | 87.1% |
| Novel (not in ESDPA) | 26 | 12.9% |

## 2. Discovery source (where we first found it)

| Source | Count |
|---|---:|
| ESDPA | 170 |
| LOA1 | 17 |
| LOA4 | 6 |
| LOA2 | 5 |
| LOA11 | 2 |
| LOA3 | 1 |

## 3. Verification level

| Level | Count | % |
|---|---:|---:|
| VERIFIED | 80 | 39.8% |
| CONFIRMED | 46 | 22.9% |
| PROBABLE | 2 | 1.0% |
| SUSPECTED | 10 | 5.0% |
| UNVERIFIED | 63 | 31.3% |

## 4. Incident type

| Type | Count |
|---|---:|
| fatal | 136 |
| near-miss | 59 |
| non-fatal | 6 |

## 5. ESDPA-vs-ours deviations

- Incidents with at least one deviation logged: **127**
- Incidents where `esdpa_date_correct = false`: **86**

## 6. Source strength

- Files with **zero** sources in `sources:` list: **61**
- ESDPA-listed with 0 independent sources: **63**
- Novel (non-ESDPA) with ≤1 independent sources: **13**
- Mean sources per incident: **1.87**
- Max sources on a single incident: **10**

## 7. Audit-flag totals

| Flag | Count |
|---|---:|
| ESDPA_ONLY_NO_INDEP | 61 |
| NOVEL_LOW_SOURCES | 13 |
| NO_SOURCES_LIST | 61 |
| NO_VICTIM_NAMED | 54 |
| DATE_WEAK | 7 |
| ESDPA_DEVIATION | 127 |
| ESDPA_DATE_DEV_UNDOCUMENTED | 3 |
| PARSE_ERROR | 0 |

Total files with ≥1 audit flag: **181** (90.0%)

## 8. Geographic spread (top 15 states)

| State | Count |
|---|---:|
| TX | 21 |
| MO | 16 |
| FL | 12 |
| KY | 10 |
| GA | 10 |
| OK | 9 |
| NY | 9 |
| CA | 9 |
| MI | 8 |
| AL | 8 |
| TN | 7 |
| NC | 7 |
| SC | 6 |
| AZ | 6 |
| MN | 5 |

## 9. Year span

- Earliest: **1981**
- Latest: **2025**
- Span: **45 years**
- Incidents with a usable year: **199 / 201**

