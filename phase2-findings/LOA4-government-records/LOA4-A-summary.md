# LOA4-A Research Summary — OSHA and CPSC Federal Agency Database Search

**Research Agent:** LOA4-A (OSHA and CPSC Records Search)
**Date Completed:** March 7, 2026
**Output Directory:** `/opt/repos/esd-research/phase2-findings/LOA4-government-records/`

---

## Overview

This summary documents all findings from a systematic search of OSHA fatality investigation records and CPSC product safety records for ESD-related incidents. Fifteen discrete searches were conducted across both agencies. Three new incident files were created; four are overhead-line incidents classified as non-ESD; one major CPSC statistical dataset was documented.

---

## Part 1: OSHA Searches

### 1.1 Searches Conducted

| Query | Description | Productive? |
|-------|-------------|-------------|
| 1 | site:osha.gov electrocution water drowning dock marina | Yes — GOV-2008-001 |
| 2 | OSHA fatality investigation "electrocution" marina OR dock water | Yes — GOV-2022-001 |
| 3 | OSHA "electric shock drowning" marina OR dock | Yes — GOV-2016-001 |
| 4 | OSHA inspection SIC 4493 marina electrical violation death | Partial — confirmed NAICS 713930 is correct code |
| 5 | OSHA fatality summary electrocution flooded water marina | No new incidents |
| 6 | "OSHA" "electrocuted" "swimming pool" OR "marina" OR "dock" death | No new incidents; confirmed GOV-2022-001 |
| 7 | OSHA "willful violation" OR "serious violation" marina electrical electrocution death | Confirmed citations in GOV-2008-001; no new incidents |
| 8 | OSHA fatality news release marina dock electrocution | No new incidents beyond above |

### 1.2 OSHA Incidents Found

#### GOV-2008-001 — Ocean Isle Beach Marina, NC (June 13, 2008)

**File:** `GOV-2008-001.md`

| Field | Value |
|-------|-------|
| OSHA Acc. Summary Nr | 200357044 |
| Inspection Nr | 311618052 |
| Employer | Coastal Carolina Construction & Development, Inc. |
| Industry | SIC 1751 / NAICS 238130 (Framing Contractors) |
| Victim | Worker, age/name not reported |
| Outcome | Fatality (electrocution) |
| Cause | Electric drill plugged into unprotected marina receptacle (no GFCI); feet in water |
| Citations | 3 serious violations; $3,360 total penalty after settlement |
| Key Citation | 29 CFR 1926.404(B)(1)(ii) — GFCI required in wet/damp locations |
| ESDPA Status | NOT in ESDPA |
| ESD Mechanism? | Occupational electrocution in water; marina receptacle lacked GFCI; analogous to ESD mechanism |

**Significance:** This is the most directly relevant OSHA record for ESD-adjacent regulatory action. A marina receptacle without GFCI caused a worker's electrocution while in water — precisely the infrastructure failure that causes civilian ESD. The GFCI citation (29 CFR 1926.404) is the occupational parallel to the NEC Article 555 standard requiring GFCI on marina dock receptacles.

---

#### GOV-2016-001 — Dock Construction Site (July 21, 2016)

**File:** `GOV-2016-001.md`

| Field | Value |
|-------|-------|
| OSHA Acc. Summary Nr | 87086.015 |
| Inspection Nr | 1164033.015 |
| Employer | LHC Construction Management, LLC |
| Industry | NAICS 236118 (New Single-Family Housing Construction) |
| Victim | Male, age 24 |
| Outcome | Fatality (drowned after electric shock) |
| Cause | Contacted energized source at boat lift; fell into water; drowned |
| ESDPA Status | NOT in ESDPA |
| ESD Mechanism? | Yes — electric shock from boat lift caused victim to fall into water and drown; identical mechanism to recreational ESD |

**Significance:** This is the clearest mechanistic match to ESD in OSHA records. The victim touched an energized boat lift, received a shock, fell into water, and drowned — the same sequence documented in dozens of recreational ESD deaths. The fact that this occurred in a construction context (not recreation) placed it under OSHA jurisdiction rather than public safety jurisdiction, but the physics are identical.

---

#### GOV-2022-001 — Marina Boat Lift (Mobile), Overhead Power Line (August 3, 2022)

**File:** `GOV-2022-001.md`

| Field | Value |
|-------|-------|
| OSHA Acc. Summary Nr | 148483.015 |
| Employer | Marina (NAICS 713930) |
| Industry | NAICS 713930 (Marinas) |
| Victim | Marina employee, boat lift operator |
| Outcome | Fatality (electrocution from overhead power line) |
| Cause | Mobile boat lift boom contacted overhead high-voltage power lines |
| ESDPA Status | NOT in ESDPA |
| ESD Mechanism? | No — overhead power line, not dock/shore-power wiring; victim not in water |

**Significance for research:** This is the only OSHA accident record explicitly coded NAICS 713930 (Marinas) found in searches. It confirms OSHA uses this code for marina workforce incidents. A direct search of OSHA's IMIS database filtered to NAICS 713930 would surface all fatalities at marina workplaces in the OSHA record.

---

#### Additional OSHA Incident — Suntex Marina, December 6, 2024 (NOT ESD)

OSHA Accident Summary Nr 172498.015 was surfaced during searches:

- Date: December 6, 2024
- Employer: Suntex Marina Investors LLC
- NAICS: 713930
- Event: 75-year-old male employee became disoriented while walking along dock, fell into water, drowned
- Keywords: Dock, Drown, Drowning, Fall, Fall From Elevation
- Cause of death: Drowning (no electrical component)
- **ESD? No.** No electrical element reported. Classic slipping/fall hazard.
- **Not filed as new GOV record** — irrelevant to ESD research.

---

### 1.3 Key OSHA Institutional Finding

OSHA's jurisdiction is limited to **workers**. The overwhelming majority of ESD fatalities are recreational users (swimmers, boat owners, vacationers). This creates a fundamental gap: OSHA has documented only the small subset of ESD-adjacent incidents where the victim was an employee working at a dock or marina. The body of recreational ESD deaths — which is approximately 95%+ of all ESD fatalities — falls entirely outside OSHA's enforcement scope.

**The OSHA IMIS database is therefore not a useful primary source for recreational ESD incident research.** It is useful for:
- Documenting occupational ESD-mechanism deaths (GOV-2008-001, GOV-2016-001)
- Identifying regulatory enforcement action around dock/marina electrical infrastructure (citations for lack of GFCI)
- Establishing which NAICS code covers marina workplaces (713930) for targeted database searches

**Noteworthy gap:** No OSHA records were found documenting a post-ESD-death inspection of a marina's dock electrical system under SIC 4493 or NAICS 713930 where the hazard that killed the victim was stray current in the water (as opposed to direct contact with energized equipment). This likely reflects: (a) most ESD victims are not workers; (b) OSHA rarely responds to recreational drowning deaths; (c) even when marina workers are electrocuted by dock wiring, the mechanism may not be coded as "electric shock in water."

---

## Part 2: CPSC Searches

### 2.1 Searches Conducted

| Query | Description | Productive? |
|-------|-------------|-------------|
| 9 | site:cpsc.gov "electric shock drowning" | Yes — confirmed "Don't Swim with Shocks" page |
| 10 | site:cpsc.gov electrocution dock marina shore power boat lift | Yes — CPSC pool/spa data page |
| 11 | CPSC recall "shore power cord" OR "dock wiring" OR "boat lift" electrocution | No relevant recalls found |
| 12 | CPSC SaferProducts.gov "electric shock drowning" OR "dock electrocution" | No individual case reports surfaced |
| 13 | CPSC NEISS "electrocution" "dock" OR "marina" OR "shore power" | No structured NEISS data found |
| 14 | CPSC "pool electrocution" deaths statistics annual 2000–2020 | Yes — year-by-year table confirmed |
| 15 | CPSC death certificates electrocution near water dock marina | CPSC 2011–2020 report identified |

### 2.2 CPSC "Don't Swim With Shocks" Statistical Data

**Source:** CPSC Consumer Product Safety Guide — Pools and Spas
**URL:** https://www.cpsc.gov/safety-education/safety-guides/pools-and-spas/dont-swim-shocks-electrical-safety-and-around-pools

**Scope:** Electrocutions in swimming pools and spas only. Does not include marina/dock incidents. Covers pool/spa electrical equipment (underwater lighting, pumps, heaters).

**Cumulative statistics:**
- 60 deaths and nearly 50 serious shocks from 1990–2003 (from pools/spas)
- 33 fatalities from 2002–2018 (from pools/spas)

**Year-by-year table (2002–2018), pool/spa electrocutions:**

| Year | Incidents w/Injury or Death | Injuries | Deaths |
|------|-----------------------------|----------|--------|
| 2002 | 4 | 2 | 2 |
| 2003 | 3 | 1 | 2 |
| 2004 | 2 | 0 | 2 |
| 2005 | 3 | 0 | 3 |
| 2006 | 2 | 1 | 1 |
| 2007 | 4 | 4 | 2 |
| 2008 | 1 | 0 | 1 |
| 2009 | 2 | 1 | 1 |
| 2010 | 3 | 1 | 2 |
| 2011 | 2 | 1 | 1 |
| 2012 | 2 | 1 | 2 |
| 2013 | 3 | 5 | 2 |
| 2014 | 4 | 4 | 2 |
| 2015 | 3 | 2 | 1 |
| 2016 | 5 | 9 | 2 |
| 2017 | 4 | 1 | 7 |
| 2018 | 0 | 0 | 0 |
| **Total 2010–2018** | **47** | **33** | **33** |

**Critical note:** The CPSC "Don't Swim With Shocks" data covers pools and spas only, not marinas and docks. Pool electrocution incidents typically involve underwater lighting, pump motors, and heater wiring — not shore power or boat lift motors. Mechanistically, these are the same hazard class as ESD (energized water from faulty electrical infrastructure), but the setting and regulatory framework differ. CPSC has jurisdiction over consumer products (pool lights, pumps) but generally not over marina electrical infrastructure.

**Cross-reference to known incidents:**
- The FI-2002-001 entry in ESDPA (Cape Coral FL, pool) likely corresponds to the 2002 Arlington TX CPSC-documented incident referenced in the 2003 press release. However: the CPSC 2003 press release identifies Arlington, TX, not Cape Coral, FL — these may be two separate incidents in the same year.
- Several ESDPA pool incidents (FI-2012-003 Americus GA, FI-2013-001 North Miami Beach FL, FI-2015-001 Palm Springs FL, FI-2016-003 Raleigh NC, FI-2019-003 Citrus Heights CA, FI-2020-003 Harris County TX) may be captured in CPSC pool/spa data but without individual case identifiers being publicly accessible.

### 2.3 CPSC "Electrocutions Associated with Consumer Products: 2011–2020" Report

**Source:** CPSC staff report, November 2023
**URL:** https://www.cpsc.gov/s3fs-public/Electrocutions-2011-to-2020.pdf

**Key findings:**
- Estimated average of 100 electrocution fatalities associated with consumer products per year (2018–2020)
- Estimated 110 in 2018, 100 in 2019, approximately 90 in 2020
- Total 2011–2020: approximately 716–720 estimated consumer product electrocution deaths
- **Scope exclusion relevant to ESD:** The report explicitly states that incidents involving "boats, direct contact with power lines, direct contact with installed wiring (excluding outlets, light switches, electrical boxes, etc.)" are considered **out of scope** for the report
- This means marina shore power cords, dock wiring, and boat electrical systems are largely excluded from CPSC electrocution counts
- ESD deaths would only appear in CPSC data if the death certificate identified a consumer product (e.g., a specific pump, light fixture, or extension cord) as the hazard — and even then, the victim must have been in a non-work context

**Implication:** CPSC's own consumer product electrocution statistics systematically exclude the majority of ESD incidents because:
1. Shore power cords and dock wiring are "installed wiring" (out of scope)
2. Boats are explicitly out of scope
3. Power lines are out of scope
4. Many ESD victims die with "drowning" on their death certificate, which the CPSC electrocution database would not capture

### 2.4 CPSC Recall Search — No Relevant Recalls Found

Searches for CPSC recalls of shore power cords, dock wiring systems, or boat lift electrical components returned no relevant results. CPSC has issued recalls of:
- Hair dryers lacking immersion protection
- Extension cords with undersized wiring
- Power strips with ungrounded enclosures

No recalls were found for marina-specific shore power equipment, dock wiring pedestals, or boat lift electrical components. This absence is consistent with CPSC's limited jurisdiction over marine infrastructure.

### 2.5 CPSC SaferProducts.gov — No Structured Marina/ESD Data Found

SaferProducts.gov accepts consumer incident reports, but no structured search of dock/marina/shore-power electrocution reports was accessible. Individual reports would require manual review within the database. CPSC's incident files for pool electrocutions are maintained in the Consumer Product Safety Risk Management System (CPSRMS) database, which is not publicly searchable at the individual case level.

---

## Part 3: OSHA-CPSC Interaction — Shared Regulatory Gap

The two agencies collectively cover very little of the ESD problem space:

| ESD Setting | OSHA Jurisdiction? | CPSC Jurisdiction? | Covered? |
|-------------|--------------------|--------------------|----------|
| Marina swimmer killed by dock wiring | No (not a worker) | Marginal (dock wiring = installed wiring, excluded) | Mostly no |
| Marina worker killed by dock wiring | Yes | No | Partial (OSHA) |
| Pool swimmer electrocuted by pool pump/light | No (not a worker) | Yes (consumer product) | Yes (CPSC) |
| Boat owner killed by shore power fault | No (not a worker) | Marginal (boat electrical = out of scope) | Mostly no |
| Construction worker on dock, killed by boat lift | Yes | No | Yes (OSHA) |
| Recreational swimmer killed by boat lift stray current | No | Marginal | Mostly no |

The table illustrates a systematic coverage gap: **recreational ESD at marina/dock settings is effectively unregulated at the federal product safety level.** CPSC covers pool equipment but not marina infrastructure. OSHA covers workers but not recreational users. No federal consumer product safety authority has direct jurisdiction over the shore power / dock wiring / boat lift systems that cause the majority of ESD deaths.

This is not a new finding — it has been noted by ESD advocates — but the OSHA and CPSC database searches confirm it from the regulatory record.

---

## Part 4: New Incident Files Created

| File | Date | Location | Classification | ESDPA Status | Notes |
|------|------|----------|----------------|--------------|-------|
| GOV-2008-001.md | June 13, 2008 | Ocean Isle Beach Marina, NC | Fatal — ESD-adjacent (occupational) | NOT in ESDPA | Worker drilled into dock with no-GFCI receptacle; feet in water |
| GOV-2016-001.md | July 21, 2016 | New dock construction site | Fatal — ESD mechanism (occupational) | NOT in ESDPA | Worker contacted energized boat lift, fell in water, drowned |
| GOV-2022-001.md | August 3, 2022 | Marina (NAICS 713930) | Fatal — overhead power line (not ESD) | NOT in ESDPA | Mobile boat lift contacted overhead power lines; operator fell from cab |

**Total new incident files created by LOA4-A:** 3

---

## Part 5: Incidents Checked Against ESDPA and Found Not to Be New

| Incident Found in Search | ESDPA Check | Result |
|--------------------------|-------------|--------|
| Suntex Marina, Dec 6, 2024 — employee fell into water, drowned | No electrical component; ordinary fall | Not ESD; not filed |
| OSHA farmworker electrocution (irrigation system) | Not water-immersion ESD; direct metal contact | Not ESD; not filed |
| Red Stag vessel engine room electrocution (Oct 14, 2023) | High-voltage panel on ship; not stray current in water | Not ESD; USCG report |
| CPSC pool/spa statistics (2002–2018) | Aggregate statistics; no individual cases newly identified | Statistical record documented |

---

## Part 6: Key Regulatory Citations Relevant to ESD

From OSHA citation records in GOV-2008-001, the following standards are directly relevant to ESD prevention in dock/marina contexts:

- **29 CFR 1926.404(B)(1)(ii)** — GFCI protection required for all 120V, 15/20A electrical equipment used in construction in wet or damp locations. This is the occupational equivalent of NEC Article 555's marina GFCI requirement.
- **29 CFR 1926.106(A) and (C)** — Working over or near water; workers shall wear U.S. Coast Guard-approved life preservers. Also requires ring buoys and safety skiffs for water work.
- **29 CFR 1926.020(B)(2)** — Accident prevention responsibilities.

These OSHA construction standards apply when workers are performing dock construction or repair. They do not apply to the marina's ongoing operations (which would be covered by 29 CFR Part 1917 — Marine Terminals — or general industry standards).

---

## Part 7: Recommendations for Further Research

1. **Direct OSHA IMIS Database Query:** Filter accident summaries by NAICS 713930 (Marinas) to find all OSHA-investigated marina worker fatalities. The web interface at https://www.osha.gov/ords/imis/accidentsearch.html supports NAICS filtering. This search was not directly executed due to web interface limitations; it should be a priority for any follow-up OSHA research.

2. **CPSC In-Depth Investigation (INDP) File:** The CPSC maintains an in-depth investigation file for death certificate cases. A FOIA request for all INDP records where product involvement includes pool/spa electrical equipment, marina equipment, or shore power cords (1990–2025) would surface individual case narratives not publicly visible.

3. **CPSC CPSRMS Database:** The Consumer Product Safety Risk Management System contains individual incident reports for pool/spa electrocutions. FOIA request for all CPSRMS records coded as electrocution + water/aquatic setting would identify specific incidents (with victim names, locations, and product identification) that would allow cross-matching with the ESDPA list.

4. **OSHA News Release Archive:** Search https://www.osha.gov/news/newsreleases/enforcement for all news releases mentioning "marina," "dock," or "boat lift" electrocution. The search surfaces results referencing a diver's fatality at Manns Harbor bridge and several construction electrocutions, but a focused marina/dock filter was not achievable through web searches alone.

5. **State OSHA Plans:** Twenty-eight states operate their own OSHA-approved state plans. Cal/OSHA, NC DOL, TN OSHA, and TX OSHA all have independent databases. Several of the most documented ESD hotspots (California, North Carolina, Tennessee, Texas) are in state-plan states. State plan records would add significant additional occupational ESD-adjacent incident data.

---

## Summary Statistics

| Category | Count |
|----------|-------|
| Searches executed | 15 |
| New incident files created | 3 |
| ESD-mechanism incidents (occupational) | 2 (GOV-2008-001, GOV-2016-001) |
| Marina-setting but non-ESD incidents | 1 (GOV-2022-001) |
| CPSC statistical datasets documented | 2 |
| CPSC individual incidents newly identified | 0 |
| Incidents confirmed already in ESDPA | 0 (no overlap found) |

---

*Research completed: March 7, 2026*
*Agent: LOA4-A (OSHA and CPSC Federal Agency Database Search)*
*Phase 2 Line of Attack 4: Regulatory and Government Records*
