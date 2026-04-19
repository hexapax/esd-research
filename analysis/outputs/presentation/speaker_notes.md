# Speaker Notes — NEC Trend Charts

Three charts, three talking points. Use the one that fits each audience.

Each chart is in `analysis/outputs/presentation/` at 16:9 and 4:3.

---

## Chart 1: `hero_nec_trend_16x9.png`

**Title on slide:** "Where the code reached, it worked."

### For general / HOA audience (Monday NCL, GA lakes HOAs)

> "What you're seeing is 45 years of Electric Shock Drowning incidents in
> the United States. The blue bars are incidents at commercial marinas.
> The red bars are incidents at private residential docks — people's
> homes.
>
> In 2011, the National Electrical Code added serious new protections
> for commercial marinas. A required safety device called GFPE that
> cuts power in 30 milliseconds when it senses current leaking into the
> water.
>
> Look at the blue bars after that dashed line. The marina rate holds
> flat — 1 per year, 0.67 per year — basically where it was.
>
> Now look at the red bars. Private docks. Nobody required those to
> change anything. Same houses, same grandfathered wiring. And the
> private-dock rate nearly tripled, from 0.47 per year before 2011 to
> 2.67 per year right after.
>
> The code worked where it reached. It didn't reach our homes."

### For NFPA / first responder audience

> "Per the ESDPA-plus-independent dataset, n=79 flag-classified incidents
> split marina vs private dock. Negative binomial regression on annual
> counts with interaction `flag × era × year` gives a likelihood-ratio
> χ² of 18.0, p=0.001 — the three-era segmented model is a significantly
> better fit than any model without that interaction.
>
> Within the marina cohort, the overall post-1981 IRR is 1.02 per year,
> CI 0.99 to 1.05, p=0.10 — indistinguishable from flat.
>
> Within the private-dock cohort, the post-1981 IRR is 1.09 per year,
> CI 1.05 to 1.14, p=1.5 × 10⁻⁵.
>
> The ratio of marina-to-private-dock mean incidence flipped from 1.71
> pre-NEC 2011 to roughly 0.4 after. We note reporting-effort
> confounding — the ESDPA formed in 2011, so absolute counts are
> inflated post-2011 — but the ratio shift is defensible because both
> cohorts are catalogued by the same organization under the same
> reporting conventions."

---

## Chart 2: `ratio_flip_16x9.png`

**Title on slide:** "The ratio flipped — and stayed flipped."

### For general / HOA audience

> "One number. The marina-to-private-dock ratio.
>
> Before 2011: marinas had 1.71 times the rate of private docks.
> Marinas were deadlier.
>
> After NEC 2011: private docks have over twice the rate of marinas.
>
> After NEC 2017 — same thing. Private docks are still roughly double.
>
> This is the single clearest piece of evidence that the National
> Electrical Code did what it was supposed to do for commercial marinas.
> And the single clearest evidence that nobody has done the same for us."

### For NFPA / first responder audience

> "Same data as the time-trend chart, collapsed to per-era means.
>
> 0.80 vs 0.47 per year pre-2011 — marinas 1.71× private-dock rate.
> 1.00 vs 2.67 per year 2011–2016 — inverted to 0.38.
> 0.67 vs 1.44 per year 2017–present — 0.46.
>
> This is the regulation-differential signal in its cleanest form.
> We have not corrected for reporting effort — but the reporting-effort
> confound acts roughly symmetrically across cohorts catalogued by the
> same organization, so the ratio is the part we trust more than the
> absolute levels."

---

## Chart 3: `era_bars_16x9.png`

**Title on slide:** "Marina ESD rate held flat. Private-dock rate nearly tripled."

### For general / HOA audience (probably the most readable chart)

> "Three pairs of bars. Each pair is one NEC era.
>
> In the first pair — before 2011 — marinas and private docks were at
> similar rates. Marinas slightly higher.
>
> In the second pair — right after NEC 2011 — marina rate ticked up a
> bit to 1 per year. But private dock rate went to 2.67 per year.
> That's nearly six times what it had been.
>
> In the third pair — the current NEC era, 2017 onward — marinas came
> back down. Private docks are still running at 1.44 per year,
> three times the pre-2011 rate.
>
> When we find the problem and we write the code, we can fix this.
> The marina numbers prove it. The private-dock numbers prove we
> haven't."

### For NFPA / first responder audience

> "Same numbers as before, visualized as per-era means for clarity.
>
> Marina rate 0.80 → 1.00 → 0.67 per year across the three eras.
> Effectively flat with some noise. n=24, n=6, n=6.
>
> Private-dock rate 0.47 → 2.67 → 1.44. A five-fold step change in era B,
> settling to about three times the pre-NEC baseline. n=14, n=16, n=13.
>
> The asymmetry is the story: marinas moved; private docks did not."

---

## Data caveats Nicole may be asked about

**'Where do the 201 incidents come from?'**
- 175 from the ESDPA compilation (which pre-dates our project)
- 26 found independently via our Phase 2 Lines of Attack (news archives,
  obituaries, court records, OSHA, etc.)

**'Have you verified the ESDPA entries or just copied them?'**
- 128 of 201 (63.7%) carry at least one non-ESDPA primary source
- 127 entries have documented corrections or additions to what ESDPA
  published — date fixes, location refinements, victim identification
- See `audit/AUDIT.md` for the full summary

**'Did you ever remove entries from the ESDPA list?'**
- No entries removed. Entries that did not match classic ESD (pool
  electrocutions, fountain, overhead line) are marked EXCLUDED and kept
  in the record with explanation. Transparency over trimming.

**'Why is the trend rising? Is it just better reporting?'**
- Partly. ESDPA formed in 2011, so both cohorts have inflated absolute
  counts post-2011. This is why we emphasize the ratio, not absolute levels.
- The ratio flip is harder to explain away by reporting effort, because
  both cohorts are catalogued by the same organization under the same
  reporting conventions.

**'What would close the private-dock gap?'**
- NEC-equivalent rules for private docks: required GFPE on dock branch
  circuits, mandatory shock-hazard signage, periodic inspection.
- Smith Mountain Lake, VA, counties adopted uniform dock-inspection code
  within 30 days of the July 2024 Jesse Hamric ESD death. Direct
  precedent that county-level response is feasible.

---

## Slide-drop instructions

1. Right-click → save the 16:9 PNG from `analysis/outputs/presentation/`.
2. In Google Slides, Insert → Image → Upload from computer.
3. Use the hero chart for dense audiences (NFPA); use the ratio-flip or
   era-bars chart for general audiences (NCL, HOA).
4. Paste one of the speaker-note blocks above into the slide's speaker
   notes area.
