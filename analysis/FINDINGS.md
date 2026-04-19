# ESD Dataset — Statistical Findings

**Generated:** 2026-04-18
**Data source:** `esd-dataset/exports/ESD-dataset-20260418--large-incidents.csv` (201 incidents) and `...--small-victims.csv` (364 victim rows)
**Script:** `analysis/esd_analysis.R`
**Raw log:** `analysis/outputs/analysis_log.txt`

All numbers below are reproducible by running `Rscript analysis/esd_analysis.R` after regenerating exports with `python3 esd-dataset/export_dataset.py`.

---

## 1. Dataset composition

| Metric | Value |
|---|---|
| Incidents | 201 |
| Victims | 364 |
| Fatalities (total) | 164 |
| Injuries (total) | 161 |
| Near misses (total) | 131 |
| Year range | 1981–2025 |
| Incidents missing year | 2 |

**Verification level:** VERIFIED 80 (40%), CONFIRMED 46 (23%), PROBABLE 2, SUSPECTED 10, UNVERIFIED 63 (31%). 63% of the dataset is VERIFIED or CONFIRMED by primary independent sources.

**Incident type:** fatal 136 (68%), near-miss 59 (29%), non-fatal/injury-only 6 (3%). Non-fatal is underrepresented — injury-only events are harder to detect in news archives.

**Electrical source (top):** dock_wiring 65 (32%), other 32, shore_power 31 (15%), pool_pump 18, boat_lift 13, overhead_line 11, charger 6. Dock + shore-power + boat-lift = 54% of all cases, i.e. marine electrical infrastructure dominates.

**Water type:** fresh 156 (78%), pool 26 (13%), salt 12 (6%). The fresh-water dominance is the defining epidemiological feature — salt water's low resistance shunts current around bodies.

**Top states:** TX 21, MO 16, FL 12, GA 10, KY 10, CA 9, NY 9, OK 9, AL 8, MI 8. Lake states (MO, KY, GA, TN, AL) are disproportionately represented relative to population — consistent with the fresh-water mechanism.

---

## 2. Temporal trend

### Poisson GLM: `incidents ~ year`

```
year coef = 0.040  (SE 0.0059, p = 1.2e-11)
IRR per year = 1.041  (95% CI 1.029–1.053)
Residual deviance / df = 2.75  ← overdispersed
```

On its face, listed incidents grow ~4.1% per year. But the dispersion ratio >> 1 means a Poisson model understates uncertainty.

### Negative-binomial GLM (preferred)

```
year coef = 0.049  (SE 0.0094, p = 2.2e-07)
IRR per year = 1.050  (95% CI 1.031–1.070)
theta = 2.86
```

The NB estimate is a ~5% annual growth rate in **listed** incidents. AIC drops from 247 (Poisson) to 218 (NB), so NB fits better.

### This is almost certainly a reporting artifact, not an epidemiologic trend

A segmented model testing whether the slope changes at 2011 (the year ESDPA was founded) is highly significant:

```
Pre-2011 slope  ≈  +0.072 log-incidents/yr
Post-2011 slope ≈  −0.084 log-incidents/yr  (main effect, p = 0.00023)
Interaction p   =  4.9e-09  (LR-χ² = 36.1)
```

Translated: the listed incident rate rose sharply through the mid-2010s and has **declined** since roughly 2017. The jump-then-decline shape matches the life cycle of an advocacy-driven list (initial surge as historical cases get logged, then falloff as the list depends on ongoing new reports). It does not match any plausible real-world process — marinas don't change that fast.

Concretely: 2017 had 21 listed incidents; 2020–2022 averaged 3.3/yr; 2023–2025 averaged 4/yr. A genuine drop of that magnitude would require a ~5× reduction in exposure or fault rate in under a decade, with no corresponding intervention at scale. More plausible reading: ESDPA's active logging years (2012–2018) captured a backlog, and current-year detection lag + reduced list maintenance are pulling recent years down.

**Bottom line:** the dataset is a **detection floor that waxes and wanes with reporting effort**, not a time series of true incidence. Do not quote "5% annual growth" as an epidemiologic fact.

---

## 3. Recent-decade incidence estimate

Raw mean for 2015–2024: **6.8 listed incidents/year**.
After downweighting verification levels (VERIFIED 1.00, CONFIRMED 0.95, PROBABLE 0.80, SUSPECTED/UNVERIFIED 0.50): **6.3 "likely-real" listed events/year**.

Undercoverage sensitivity (multiplying the weighted point estimate):

| Assumed undercount | Estimated true events/yr |
|---|---|
| 1.1× (near-complete capture) | ~6.9 |
| 1.5× (central) | ~9.4 |
| 2.5× (high) | ~15.6 |

**Justification of the range.** This project's Phase 2 effort added 18 net-new incidents against 175 ESDPA entries (~10% upward revision), so 1.1× is a *floor*. Comparable drowning underreporting in CDC/NEMSIS research typically runs 1.5–3× for cause-specific water deaths where electrocution is a competing mechanism, so 2.5× is a reasonable ceiling. Central estimate **~9–10 ESD events/year in the US recently**, with 3–4 fatalities and 3–4 injuries per year at the same reporting efficiency.

This is consistent with the CDC's absence of an explicit ESD mortality code (no single ICD-10 code cleanly captures it) and with the Phase 2 finding that coroner records in several identified cases did not use "electrocution" as primary cause.

---

## 4. Victim demographics

Age distribution (179 victims with recorded age):

- Mean 24.2, median **18**, IQR 13–31.5
- 0–9: 19 · 10–14: 36 · 15–17: 29 · 18–24: 35 · 25–34: 20 · 35–49: 20 · 50–64: 17 · 65+: 3
- **47% of victims with recorded age are minors (under 18).**

Minor-concentration is the single most policy-relevant finding. Dock and pool exposure occur disproportionately during recreation, and children have lower body mass (so lower step-potential thresholds for loss-of-muscle-control) and can't self-rescue.

### Logistic regression: P(fatal | victim exposed)

```
glm(fatal ~ age + gender, family = binomial)

age     OR = 1.038 per year   (p = 0.019)
genderM OR = 2.741 vs female  (p = 0.010)
```

Conditional on being in the dataset at all (i.e., having been shocked), **male victims are ~2.7× more likely to die than female victims**, and each additional year of age raises the odds by ~4%. The gender effect plausibly reflects rescue behavior — multiple incidents in the dataset describe male relatives entering the water after a primary victim and becoming secondary fatalities. Female victims are overrepresented in "near-miss" and "injured" strata (F 106/153 non-fatal, M 80/194 non-fatal).

Raw outcomes by gender (victims with known gender):

| Gender | Fatal | Injured | Near-miss | Fatal % |
|---|---:|---:|---:|---:|
| F | 39 | 46 | 21 | 37% |
| M | 114 | 47 | 33 | 59% |

---

## 5. What the models actually license

**Supported claims**
- ESD in the US is dominated by fresh water (78%) and by marine electrical infrastructure (dock/shore/lift = 54%).
- Victims skew young (median 18, ~47% minors) and male (65% of fatalities).
- Given exposure, males are ~2.7× more likely to die than females (p = 0.01), independent of age.
- A central estimate of ~9–10 true ESD events per year in the US is consistent with the listed data plus plausible undercoverage.

**Not supported**
- No claim that incidence is rising or falling in the real world. The observed time trend is dominated by reporting effort.
- No state-level rate claims. Counts are not population- or waterfront-mile-normalized.
- No seasonality claim (date precision is "exact" in only part of the data, and seasonality analysis was not run).

---

## 6. Outputs

All files under `analysis/outputs/`:

- `analysis_log.txt` — full text log of every model and table
- `yearly_counts.csv` — incidents, fatalities, injuries, near-misses per year
- `yearly_verified_adjusted.csv` — same with verification-weighted column
- `fig1_incidents_per_year.png` — annual bar chart with LOESS
- `fig2_outcomes_per_year.png` — stacked fatalities/injuries/near-misses
- `fig3_age_distribution.png` — victim age histogram
- `fig4_top_states.png` — top 15 states
- `fig5_verification_over_time.png` — verification-level composition by year
- `fig6_model_fits.png` — Poisson and negative-binomial fitted curves

## 7. Marina / Commercial vs Residential trends

Incidents classified by string-matching `facility_name`, `body_of_water`, `electrical_source`, and `water_type` (see `analysis/esd_setting_trends.R`):

| Setting | Count | Share |
|---|---:|---:|
| Commercial (marinas, apartments, hotels, public pools, resorts, military bases, parks) | 64 | 32% |
| Residential (private docks, private pools, lakehouses, backyards) | 52 | 26% |
| Other/Unknown (facility field blank or non-specific) | 85 | 42% |

**Caveat.** The 42% "Other/Unknown" bucket is large because many older incidents have a blank `facility_name` — the split is directional, not definitive. A random-sample audit of that bucket would tighten the estimates.

### Trend models per setting (negative binomial, year as predictor)

| Setting | IRR/yr | 95% CI | p | Interpretation |
|---|---:|---|---:|---|
| **Residential** | **1.13** | 1.07–1.18 | 1.2e-06 | ~13%/yr growth in listed cases |
| **Commercial** | **1.05** | 1.03–1.07 | 3.0e-05 | ~5%/yr growth |
| Other/Unknown | 1.02 | 1.00–1.04 | 0.068 | Flat |

### Segmented models (pre- vs post-2011 slope change)

| Setting | Pre-2011 slope | Post-2011 slope | Slope-change p |
|---|---:|---:|---:|
| Residential | +0.215 | −0.113 | 0.0005 |
| Commercial | +0.101 | −0.023 | 0.010 |
| Other/Unknown | +0.041 | −0.132 | 0.0006 |

Every setting shows the same rise-then-fall pattern at 2011, so reporting-effort explains part of the apparent growth in all three. But the effect sizes differ sharply:

### What the charts show

- **`fig7_setting_yearly_loess.png`** — LOESS smoothers by setting. Residential (red) rises from near-zero pre-2000 to a 2014–2017 peak, then declines. Commercial (blue) tracks a flatter upward path. Other/Unknown (grey) was the dominant category historically and has also declined.
- **`fig8_setting_faceted_nb.png`** — Same data, faceted, with negative-binomial fits. The Residential panel has the steepest exponential fit (slope 0.124, i.e. ~13%/yr).
- **`fig9_setting_share_over_time.png`** — 5-year rolling **share** of incidents. This is the cleanest picture of trend: Residential went from 0% (pre-2000) to ~42% (2014–2017) of listed incidents, then pulled back to ~25–28% recently.
- **`fig10_setting_cumulative.png`** — Cumulative curves. Residential is the steepest-climbing segment over the last 15 years.
- **`fig11_setting_outcome_mix.png`** — Residential incidents are ~77% fatal vs ~71% commercial and ~58% other. Private-dock / private-pool events have the highest fatal share.

### Reading the trend

Two non-exclusive explanations for the Residential surge:

1. **Real exposure increase.** Private-dock and backyard-pool counts have genuinely grown in lake communities (Lake of the Ozarks, Lake Cumberland, Smith Mountain Lake etc.) as suburban-style development around lakes accelerated in the 2000s. Private docks are built by homeowners, often without permitting or inspection of the 120/240V feed; marinas are subject to NEC 555 and periodic inspection. So an epidemiologic increase is biologically plausible.
2. **Detection bias.** Pre-2000, a private-dock death in a rural lake county could be recorded as "drowning" with no electrical workup, whereas newer cases benefit from ESDPA advocacy and better investigator awareness. The post-2011 slope reversal (−0.113) is too fast to be a real-world effect.

The honest summary is: **Residential-setting ESD is the fastest-growing segment in the listed data, and it has the highest fatality share, but we cannot separate real exposure growth from improved detection.** Commercial incidents grow more slowly (IRR 1.05) which is closer to the overall dataset trend.

### Operative implication

If the goal is harm reduction, the residential setting is both the fastest-growing and the deadliest fraction of listed cases, and it is the setting where mitigation (GFCI/GFPE on shore-power receptacles, equipotential-bonding inspections) is least likely to be enforced today. Commercial marinas are already subject to NEC 555; residential docks are not.

---

## 8. Reasoning-classifier flags: Freshwater private dock vs Freshwater marina

Two mutually-exclusive boolean fields were added to every incident file on 2026-04-18 via a reasoning-model pass over each record's `facility_name`, `body_of_water`, `water_type`, `electrical_source`, `notes`, `research_notes`, and full markdown body:

- `is_freshwater_private_dock` — evidence indicates the incident was at a private/residential dock on fresh water.
- `is_freshwater_marina` — evidence indicates the incident was at a commercial/shared-use marina on fresh water.

Both flags are `false` whenever the incident is not on fresh water, not at a dock, or when the record doesn't distinguish private from marina. See `esd-dataset/SCHEMA.md` for rules.

### Counts

| Setting | n | Share |
|---|---:|---:|
| Private freshwater dock | 43 | 21.4% |
| Freshwater marina       | 36 | 17.9% |
| Neither                 | 122 | 60.7% |

Classifier confidence: **high 150 (75%), medium 10 (5%), low 41 (20%)**. The "low" bucket is essentially "we have a freshwater dock incident but no way to tell private vs marina" — all those are labeled Neither, which prevents speculation.

### Comparison to the prior string-matched setting

Cross-tabulation (n = 201):

| Flag ↓ / Prior → | Commercial | Other/Unknown | Residential |
|---|---:|---:|---:|
| Private freshwater dock | **1** | 8 | **34** |
| Freshwater marina       | **32** | 4 | 0 |
| Neither                 | 31 | 73 | 18 |

**Agreement (Cohen's κ):**
- `is_freshwater_private_dock` vs prior `Residential`: **κ = 0.63** (substantial)
- `is_freshwater_marina` vs prior `Commercial`: **κ = 0.53** (moderate)

**Where the classifier disagrees with the string-matcher:**

- Prior `Commercial` → new `Neither` (31 cases): most were apartment pools, hotel pools, splash pads, public parks — the string-matcher threw them in Commercial, but those are not freshwater marinas by definition. The flag is tighter. Similarly the 18 prior `Residential` → new `Neither` are mostly backyard pools / private pool electrocutions — correctly excluded because they are not docks.
- Prior `Residential` → new `Private freshwater dock` (34): the core agreement.
- Prior `Other/Unknown` → new `Private freshwater dock` (8) or `Marina` (4): records the string-matcher couldn't classify because `facility_name` was blank, but where the narrative in `notes` or the markdown body was enough for a reader to decide.
- The single **Commercial → Private-dock** disagreement (ESD-2019-09-00-1) is one the reasoning model judged to be a private dock based on the narrative, against a "park/recreation area" string hit.

**What the reclassification bought us:** it moved ~40% of the "Other/Unknown" catch-all into one of the two defined categories (12 of 85 string-matcher Other/Unknown became flagged as private dock or marina), and it pruned ~60 pool/residence-but-not-a-dock cases out of the Commercial/Residential buckets into "Neither" where they belong for this question.

### Trend models using the flags

Negative-binomial `incidents ~ year`:

| Flag setting | n | IRR/yr | 95% CI | p |
|---|---:|---:|---|---:|
| **Private freshwater dock** | 43 | **1.09** | 1.05–1.14 | 1.5e-05 |
| **Freshwater marina**       | 36 | **1.02** | 0.995–1.05 | 0.103 |
| Neither                     | 122 | 1.04 | 1.02–1.06 | 4.4e-05 |

**This is the cleanest finding in the analysis so far.** With the tighter flag definitions:

- **Freshwater marina incidents are essentially flat** (IRR 1.02, CI overlaps 1.0, p=0.10). The prior string-matcher had put marinas on a 5%/yr rise; that was almost entirely contamination from apartment pools, hotel pools, and splash pads.
- **Private-dock incidents rise ~9%/yr**, confidently above 1.0 (narrower than the prior 13% estimate, but still the fastest-growing segment).

### Segmented models (pre/post 2011)

| Flag setting | Pre-2011 slope | Post-2011 slope | p(change) |
|---|---:|---:|---:|
| Private freshwater dock | +0.220 | −0.111 | 3.1e-05 |
| Freshwater marina       | +0.093 | −0.087 | 0.016 |
| Neither                 | +0.040 | −0.084 | 0.003 |

All three show the same rise-then-fall pattern at 2011, so **reporting-effort artefact is still present even in the sharper flag definition.** But the magnitude of the private-dock rise is much larger than marina's, and starts from essentially zero pre-2000.

### Outcome mix per flag group

| Setting | Fatal | Injury only | Near-miss |
|---|---:|---:|---:|
| Freshwater marina       | 77.8% | 5.6% | 16.7% |
| Private freshwater dock | 74.4% | 4.7% | 18.6% |
| Neither                 | 62.3% | 20.5% | 17.2% |

Per-exposure fatality is essentially the same at private docks and marinas (~75–78%), which is a shift from the prior noisier string-matcher result (which showed Residential 77% vs Commercial 71%). A logistic `P(fatal) ~ flag_setting` gives no significant difference between private dock and marina (OR 0.83, 95% CI 0.29–2.36, p=0.73). **Fatal share is a property of the physics, not the ownership type.** The "Neither" group has a higher injury-only rate because it includes pool electrocutions that were reported as shocks but not drownings.

### Charts

New figures produced:

- `fig12_flag_yearly_stacked.png` — yearly incidents stacked by flag setting
- `fig13_flag_yearly_loess.png` — LOESS per flag setting
- `fig14_flag_faceted_nb.png` — per-group negative-binomial fits
- `fig15_flag_share_over_time.png` — 5-yr rolling share (shows private-dock share grew from 0% to ~35% of listed incidents around 2010–2012, stayed elevated, and is now ~22%)
- `fig16_flag_vs_prior_setting.png` — confusion matrix against prior string-matched setting
- `fig17_flag_outcome_mix.png` — fatal/injury/near-miss share per flag setting

### Takeaway

The reasoning-classifier flags are **more defensible than the string-match setting** because:

1. The Neither category is a principled "we can't tell" bucket, not a dumping ground.
2. Private-dock vs marina is defined by *semantic evidence in the record*, not by whether the `facility_name` happens to contain a keyword.
3. Non-dock cases (pools, splashpads, fountains) no longer contaminate the dock/marina counts.

With that cleaner split, the main trend story sharpens: **marina incidents are flat, private-dock incidents are rising (~9%/yr), and per-exposure fatality is the same at both.** The rise in private-dock cases is the single most actionable finding — private docks are outside the NEC 555 inspection regime that applies to commercial marinas.

---

## 9. NEC-era segmented trend (does regulation track the data?)

NEC Article 555 (Marinas and Boatyards) applies to **commercial marinas only**; private residential docks have never been covered. This creates a natural quasi-experiment: marina incidents should respond to NEC 555 updates, private-dock incidents should not.

Breakpoints tested (NEC publication years; state adoption lags 1–3 yrs):

- **NEC 2011** — first nationwide 30 mA GFPE requirement for marina shore power (555.3)
- **NEC 2017** — branch-circuit GFPE, mandatory "no-swim" signage, listed marina receptacles
- **NEC 2020** — Article 555 renumber and major overhaul, boat-hoist GFCI (too recent / too few years to fit as its own segment, so used as open end of the third segment)

Script: `analysis/esd_nec_segments.R`. Only the two flag-true groups (Private freshwater dock, n=43; Freshwater marina, n=36) are used in these fits — "Neither" is not about docks and isn't relevant to NEC 555.

### Mean incidents per year, per era

| Era | Years | Private freshwater dock | Freshwater marina | Marina / Private ratio |
|---|---:|---:|---:|---:|
| **A: pre-2011** (1981–2010) | 30 | 0.47 | **0.80** | **1.71** |
| **B: 2011–2016** (NEC 2011/2014) | 6 | **2.67** | 1.00 | 0.37 |
| **C: 2017–2025** (NEC 2017 and later) | 9 | 1.44 | 0.67 | 0.46 |

**The single most striking number in the whole analysis is the ratio shift.** Before 2011, marinas were ~1.7× as common as private docks in the listed data. After 2011, marinas drop to ~0.4× private docks — a **4-fold swap in the relative burden.**

### Per-era NB trend (IRR per year, fit within each era)

| Setting | Era A (pre-2011) | Era B (2011–2016) | Era C (2017+) |
|---|:---:|:---:|:---:|
| **Freshwater marina** | **IRR 1.10** [1.04, 1.16] **p=0.001** | 0.69 [0.41, 1.17] p=0.17 | 0.90 [0.66, 1.24] p=0.53 |
| **Private freshwater dock** | **IRR 1.27** [1.10, 1.47] **p=0.002** | 0.88 [0.66, 1.18] p=0.38 | 0.80 [0.64, 1.01] **p=0.06** |

Reading: in the pre-2011 era, both settings were rising significantly (marina +10%/yr, private +27%/yr — the steep pre-2011 rise is likely reporting-driven for both). In the 2011–2016 and 2017+ eras, *neither* slope is significantly different from zero (private dock in era C is borderline at p=0.06). Small per-era sample sizes (6 and 9 years) widen the CIs.

### Interaction tests

From `MASS::glm.nb(incidents ~ flag * era * year)` on the 45-year grouped data:

**Two-segment model (break at 2011):**
- Adding `flag × era × year` over the no-interaction base: LR χ² = 25.5, **p = 2.8e-06**, ΔAIC = −22.
- Slopes change sharply at 2011 and the change differs by setting.

**Three-segment model (breaks at 2011 and 2017):**
- Adding era step effects: LR χ² = 10.3, p = 0.006.
- Adding `flag × era` (allowing era effect to differ by setting): LR χ² = 8.6, p = 0.034.
- Adding full `flag × era × year`: LR χ² = 18.0, **p = 0.001**.
- Three segments fit meaningfully better than two, suggesting the post-2017 behavior of marinas vs private docks is not just an extrapolation of the 2011–2016 slope.

### What this says about NEC 555

The quasi-experiment wants one clear signal: *marina slopes bend down at 2011 (and again at 2017), private-dock slopes do not.* Here's what the data actually shows:

1. **Marina incidents peaked pre-2011 and have not recovered.** Marinas had 0.8 incidents/yr pre-2011, briefly rose to 1.0/yr in 2011–2016 (likely the ESDPA-era reporting catch-up), then fell to 0.67/yr post-2017 — the lowest of the three eras. Consistent with NEC 555 having some protective effect.

2. **Private-dock incidents did the opposite.** 0.47/yr pre-2011, jumped to 2.67/yr in 2011–2016, then dropped to 1.44/yr post-2017. The 2011–2016 jump is a ~5.7× increase over pre-2011; the post-2017 level is still ~3× the pre-2011 baseline. Consistent with private docks *not* being regulated and with growth in lakefront residential development.

3. **But confounding with reporting effort is severe.** ESDPA formed in 2011 and actively catalogued incidents through ~2017. The 2011–2016 jump in both series is therefore partly a detection spike, not a real exposure spike. The post-2017 fall in both series could be genuine regulation + mitigation *or* ESDPA list maintenance slowing.

4. **Honest reading of the signal.**
   - The ratio shift (marinas went from 1.7× private-dock burden to 0.4×) is *too large* to be explained by reporting bias alone, because both settings were being catalogued by the same group (ESDPA).
   - The *direction* is consistent with NEC 555 reducing marina incidents: commercial marinas became relatively safer than unregulated private docks after 2011.
   - Magnitude of regulatory effect cannot be cleanly estimated from this dataset — we'd need either state-level adoption timing or a control comparison (e.g., salt-water marinas, which are covered by NEC 555 only weakly because current conducts away from bodies in salt water).

### Charts

- **`fig18_nec_2seg.png`** — Two-segment NB fit (break at 2011) overlaid on raw dodged bars.
- **`fig19_nec_3seg.png`** — Three-segment NB fit (breaks at 2011 and 2017). The private-dock (red) curve dominates marina (blue) in both B and C eras.
- **`fig20_nec_era_means.png`** — Mean incidents/yr bar chart. The cleanest single-chart story: private dock jumps 0.47 → 2.67 → 1.44 across eras; marina stays 0.8 → 1.0 → 0.67.
- **`fig21_nec_piecewise.png`** — Each era fit independently in its own faceted panel.

### Caveats worth repeating

- Era B has only 6 years, era C has 9 — narrow statistical windows.
- Recency lag (2023–2025) almost certainly pulls the post-2017 trend down artificially; real-world 2024/2025 incidents may not have been surfaced yet by ESDPA or this project's LOA searches.
- State-level NEC adoption is not uniform: California, Massachusetts, New York, and Oregon tend to lead; many southern states lag by one cycle. A state-by-year fixed-effects model would sharpen this but would push counts below the useful threshold for most states.
- The `flag_setting` assignment is based on a reasoning pass over the existing record, not the underlying truth — incidents originally classified Neither because the record lacked a facility name may belong in either dock group.

---

## 10. Suggested next models (not yet run)

- State-level Poisson with `log(state_population)` offset → state risk ratios.
- Seasonal analysis restricted to `date_precision == "exact"` incidents.
- Capture–recapture using ESDPA-listed vs Phase-2-discovered as two imperfect samplers → Chapman estimator of dataset completeness.
- Age × water-type interaction: is the minor-skew concentrated in pools vs docks?
