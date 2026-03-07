# ACAD-045: CDC Drowning Surveillance Data — Baseline Context for ESD Proportion Calculations

## Source Metadata
- **Type**: Federal public health surveillance data
- **Publisher**: Centers for Disease Control and Prevention (CDC), National Center for Injury Prevention and Control
- **Key URLs**:
  - https://www.cdc.gov/drowning/data-research/facts/index.html
  - https://www.cdc.gov/media/releases/2024/s0514-vs-drowning.html
  - https://www.cdc.gov/nchs/products/databriefs/db149.htm
- **Credibility**: Highest — federal vital statistics data

## Annual U.S. Drowning Death Statistics

### Recent Totals
| Period | Annual Drowning Deaths | Notes |
|--------|----------------------|-------|
| 1999–2010 | ~3,868/year (avg) | CDC Data Brief 2014 |
| 2012–2021 | ~4,083/year (avg) | CDC MMWR 2024 |
| 2018–2021 | ~4,345/year (avg, age-adjusted rate 1.31/100k) | CDC |
| 2020–2022 | >4,500/year | CDC Vital Signs 2024 — post-2019 increase |
| 2019 baseline | ~4,000/year | Pre-pandemic reference point |

### Trend
After decades of decline, U.S. unintentional drowning deaths increased approximately 10% starting in 2020, driven by:
- COVID-19 pandemic disruptions to swim lesson access
- Pool closures reducing supervised swimming opportunities
- The increase is concentrated in children 1–4 years and adults 65+

## ICD-10 Coding and ESD Capture

### Relevant Codes
- **W65–W74**: Accidental drowning and submersion (primary drowning codes)
- **W86**: Unintentional exposure to electric current (electrocution codes)
- **V90, V92**: Watercraft-related drowning

### The Cross-Tabulation Problem
ESD deaths should ideally appear with both a drowning code (W65–W74) and an electrical exposure code (W86) on the death certificate (multiple cause of death). However:
- This cross-tabulation has never been published by CDC
- Medical examiners rarely identify the electrical etiology
- Most ESD deaths receive **only** a drowning code (W65–W74)
- The W86 code is applied only when electrical cause is identified at autopsy/investigation — which requires electrical testing of the water at the scene, rarely performed

### CDC Wonder Database
CDC Wonder allows custom queries of underlying cause and multiple causes of death by ICD-10 code. However:
- No pre-existing CDC analysis cross-tabulates W86 with drowning codes
- Custom queries would require researcher access and would still only capture cases where both codes appear
- Most ESD deaths receive no W86 code, so even a perfect query would undercount ESD

## Proportionality Analysis

### Documented ESD as Fraction of Total Drownings
Using documented ESD figures:
- CRLEA data: ~5.8 ESD deaths/year (2010–2014) out of ~3,900–4,000 drowning deaths
- That is approximately **0.15%** of all drowning deaths
- This represents only confirmed, documented ESD cases

### Adjusted for Underreporting
If BARD captures ~8% of known ESD cases (LOA7 finding), and if CRLEA's 5.8/year represents roughly 50% capture (given CRLEA's multi-source methodology is more thorough than BARD):
- True ESD rate could be 2–10x the documented rate
- Plausible range: **10–60 ESD deaths per year**
- As a fraction of total drownings: **0.2%–1.3%**

### Context: Total Electrical Deaths
- All electrical injuries in the U.S.: approximately 1,000 deaths/year (StatPearls, NCBI)
- Of these: ~400 high-voltage, ~50–300 lightning
- Remaining ~300–550: low-voltage residential/occupational
- ESD (low-voltage, water-assisted) is a subset of this remainder

## LOA Classification
LOA5-C: Epidemiological baseline data, government source
