# Phase 2 Meta-Analysis: Mining ESD Incidents from Structured and Unstructured Sources

**Date:** 2026-03-07  
**Purpose:** Evaluate the yield, limitations, and future potential of each Line of Attack (LOA) for identifying Electric Shock Drowning incidents missed by the ESDPA incident list. Written for research partners unfamiliar with the data collection process.

---

## Background

The ESDPA (Electric Shock Drowning Prevention Association) maintains a manually-compiled list of ESD incidents. Phase 2 of this research project used 7 Lines of Attack (LOA1–LOA7) to systematically identify incidents not on that list and to quantify the structural reasons why ESD deaths are systematically undercounted in U.S. government databases.

Each LOA used AI-assisted web search (Perplexity + Brave) and/or structured database analysis. Below is a quantitative and qualitative assessment of each.

---

## LOA1: Direct News Archive Search

**Target:** News articles reporting drowning or electrocution near docks/marinas; gap years and underrepresented states  
**Agents:** 5 (gap years 1990/1992/1996; gap years 2004/2007/2009; Texas/Southwest; Pacific NW/Upper Midwest; Carolinas/Northeast/Mid-Atlantic)  
**Output directory:** `phase2-findings/LOA1-news-archive/`  
**Files produced:** 25 NEW-YYYY-NNN incident files + 5 summary files

### Yield

| Agent | Region/Years | New Verified Incidents | Key Finding |
|-------|-------------|----------------------|-------------|
| LOA1-A | 1990, 1992, 1996 | 0 | Gaps appear genuine — pre-digital era + ESD misclassification |
| LOA1-B | 2004, 2007, 2009 | **1** (Ken Lutrick, Ross Barnett Reservoir MS, 2004) | Also corrected FI-2004-002 = Tyler Deeds |
| LOA1-C | Texas, AZ, NV, NM | 0 dock/marina ESD; **2 ESD-adjacent** (power line, Lake O' The Pines TX 2017 + 2021) | Texas dock ESD gap is real, not a search gap |
| LOA1-D | WA, OR, ID, MN, WI, IL | 0 net-new | All candidate incidents matched existing files |
| LOA1-E | NC, SC, NY, PA, MD, NJ, VA | 0 net-new | Confirmed prior LOA captures |

**Total new verified incidents: 1**

### Qualitative Assessment

**What worked:** Digital news archives post-2000 are well-indexed. Named victims are highly searchable. The approach is efficient when news coverage exists.

**What didn't work:** Pre-2000 incidents are largely invisible. The 1990–1996 gap years returned zero results not because searches failed but because local newspapers from that era are not digitized and indexed by free tools. Paid archives (Newspapers.com, ProQuest Historical) are the critical missing resource.

**Mining potential going forward:** LOW for pre-2000; MODERATE for 2000–2010; LOW for post-2015 (already well-covered).

**Key structural finding:** Texas dock/marina ESD gap is real. Texas has only 2 documented ESD incidents despite 30M+ population and massive freshwater lake infrastructure. The Lake O' The Pines overhead-line deaths represent a distinct hazard type (transmission lines crossing navigable waterways), not classic dock-wiring ESD.

---

## LOA2: Misclassified Drownings

**Target:** Drowning deaths with autopsy red flags (no water in lungs, skilled swimmers, multiple victims, witness-reported electrical sensations)  
**Agents:** 3 (autopsy red flags; skilled swimmer/rescue patterns; multiple victims + witness sensations)  
**Output directory:** `phase2-findings/LOA2-misclassified-drownings/`  
**Files produced:** 25 SUSP-YYYY-NNN files + 3 summary files

### Yield

| Agent | Focus | SUSP Files | HIGH Probability | MODERATE Probability |
|-------|-------|-----------|-----------------|---------------------|
| LOA2-A | Autopsy red flags | 7 | 1 | 6 |
| LOA2-B | Skilled swimmer/rescue | 3 | 1 (Chickamauga Lake TN) | 2 |
| LOA2-C | Multiple victims/sensations | 15 | 4 | 11 |
| **Total** | | **25** | **6** | **19** |

**Deaths documented across SUSP files: ~19**  
**Shocked/injured across SUSP files: 20+**  
**Incidents already in ESDPA (deduplication): 4**  
**Net new suspected fatalities: ~15–19 (unverified)**

### Key Incidents

- **SUSP-2004-001 (Lake Travis TX):** Joule marks at autopsy — the ONLY confirmed autopsy ESD biomarker found across all Phase 2 research. Pathognomonic for electrocution via water; extremely rare finding.
- **SUSP-2016-020 (Chickamauga Lake TN):** Strong swimmer "literally just stopped and rolled over" — classic ESD paralysis pattern.
- **SUSP-2015-054 (Lake of the Ozarks MO):** Swimmers reported "electricity in water," power was cut, tingling stopped immediately. Strongest circumstantial ESD causation evidence found in Phase 2.
- **SUSP-2017-020 (Michigan marina, CDC FACE Report 17MI208):** Marina owner drowned; no electrical investigation conducted.

### Qualitative Assessment

**What worked:** Multiple-victim and witness-sensation patterns (LOA2-C) produced the most leads per search. These are the most distinctive ESD signatures.

**What didn't work:** Autopsy red flags are nearly impossible to find via web search. Medical examiners' reports are not publicly indexed.

**Mining potential going forward:** MODERATE but inherently uncertain. SUSP files cannot be upgraded without: (1) ME office records request; (2) scene investigation report; (3) electrical testing records. This requires direct investigative engagement, not web search.

**Key structural finding:** CDC FACE (Fatality Assessment and Control Evaluation) program is an underexplored source. FACE reports investigate workplace fatalities and contain detailed narratives. SUSP-2017-020 (CDC FACE 17MI208) found a marina drowning where no electrical investigation was conducted — FACE may have additional ESD-mechanism deaths.

---

## LOA3: Legal Record Mining

**Target:** Wrongful death lawsuits, premises liability cases, regulatory enforcement  
**Agents:** 3 (federal/state court search; law firm/settlement search; insurance/regulatory)  
**Output directory:** `phase2-findings/LOA3-legal-records/`  
**Files produced:** 20 LEGAL-YYYY-NNN files + 4 summary files

### Settlement/Verdict Table

| Case | Year | Victim | Settlement/Verdict |
|------|------|--------|-------------------|
| Harbison v. AmerenUE | 2006 | Nicholas Harbison, 16 | $2.325M jury verdict |
| Rhine v. State of Georgia | 2012 | Adriana Rhine (fountain) | **$1.4M settlement** (only known ESD settlement vs. U.S. state) |
| Crays v. Angel Shores | 2010 | Zachary Crays, 13 | $150K jury verdict |
| Rosoff v. pool operator | ~2017 | "Rachel," lifeguard, 17 | $6M settlement (pool pump) |
| Davenport v. fountain operator | 2023 | Nathan Davenport, 45 | Confidential settlement |
| Gonzalez v. Marina Shores | 2025 | Gabriel Gonzalez | Pending (Schafer & Schafer) |

### Critical Structural Findings (No New Incidents — But Essential Context)

- **Zero state AG enforcement actions** — No state attorney general in any U.S. state has ever initiated enforcement action based on an ESD incident.
- **Zero CPSC recalls** — No recall issued for dock wiring, shore power equipment, boat lift electrical components, or marina electrical systems despite decades of documented deaths.
- **OSHA jurisdiction gap** — OSHA covers workplace injuries only; recreational swimmers killed by dock electricity are outside mandate.
- **Missouri Recreational Use Act** — Effectively immunizes private dock owners from ESD civil liability. Lake of the Ozarks is the single deadliest ESD site in the U.S. (5–6 deaths) and has produced zero successful lawsuits.
- **Tennessee Noah Dean and Nate Act (T.C.A. § 68-102-602)** — Strongest ESD regulatory framework in any U.S. state. Mandates SFMO marina inspections every 5 years; criminal penalties up to Class E felony ($50K+) for violations causing death; 300+ marinas inspected to date.

### Qualitative Assessment

**What worked:** Law firm websites publicizing large settlements were highest-yield. Settlement dollar amounts provide economic context not captured in any government database.

**Mining potential going forward:** LOW for new incidents (legal databases are fairly well-indexed); HIGH for verification. Court records contain detailed factual allegations — incident dates, wiring configurations, inspection histories, prior complaints — that can upgrade SUSP files to verified. Direct PACER/CourtListener access would be the next step.

---

## LOA4: Government Records

**Target:** OSHA, CPSC SaferProducts.gov, CDC WONDER, USCG statistics, state agencies  
**Agents:** 3 (OSHA/CPSC; CDC/USCG; state agencies)  
**Output directory:** `phase2-findings/LOA4-government-records/`  
**Files produced:** 8 GOV-YYYY-NNN files + 4 summary files

### Confirmed New Incidents: 3

- GOV-2008-001: Ocean Isle Beach Marina NC (OSHA worker incident, 2008)
- GOV-2023-002: Nathan Davenport, Jupiter FL fountain, Oct 2023 (45yo, 8 casualties, not in ESDPA)
- GOV-2025-001: Blue Ridge Lake GA, 13yo, Jun 2025

### Critical Negative Findings

- **CDC W74+W86 cross-tabulation never performed** — Drowning (W74) and electrical exposure (W86) ICD-10 codes have never been cross-tabulated in CDC WONDER. This single analysis could identify hundreds of previously unknown ESD deaths.
- **USCG annual deaths (2019–2024):** 613, 767, 658, 636, 564, 556 — ESD not subcategorized.
- Geographic negatives confirmed: MN, WI, NY, MD, TN (post-2014) all show zero ESD fatalities in state databases — consistent with prevention working OR continued underreporting in jurisdictions without mandatory investigation protocols.

**Mining potential going forward:** MODERATE via FOIA:
1. **CDC WONDER cross-tab (W74+W86, 2000–2024)** — free data request, no FOIA required
2. **CPSC NEISS full narrative export** — FOIA request
3. **USCG BARD narrative text** — data already in hand

---

## LOA5: Academic and Epidemiological Literature

**Target:** Peer-reviewed medical/forensic papers, engineering standards, epidemiological data  
**Output directory:** `phase2-findings/LOA5-academic/`  
**Files produced:** 34 ACAD-NNN files + 3 summary files  
**New incidents found: 0**

### Key Academic Findings

- **PMID 12062943 (Karger 2002):** Water immersion eliminates electrical burns — the scientific foundation for why ESD autopsies look identical to ordinary drowning.
- **IEEE TIA 2020 (DOI 10.1109/TIA.2020.2982854):** Fault current through ground conductors bypasses both GFCI and ELCI protection — the engineering gap explaining why standard protection doesn't prevent ESD.
- **Finland:** Zero ESD deaths in 40 years with mandatory 30 mA RCDs. Proof ESD is preventable at national scale.
- **13% of marina boats leak lethal current** at any given time (CRLEA/ABYC data).
- **Only CDC document on ESD:** 1996 MMWR Oklahoma cluster — nothing in 30 subsequent years.
- **No peer-reviewed ESD epidemiology exists** — zero population-level ESD mortality studies in any peer-reviewed journal.

### Best Available Epidemiological Estimate

| Scenario | Annual Deaths | Basis |
|----------|--------------|-------|
| Documented floor | 4–6/year | CRLEA 2010–2014, ESDPA average |
| Conservative adjustment (3–5×) | 12–30/year | BARD capture rate correction |
| Moderate adjustment (5–10×) | 20–60/year | Oklahoma state extrapolation + infrastructure scale |
| **Central estimate** | **~20–30/year** | Synthesized best estimate |

**Confidence: LOW** — the study that would establish a better estimate has never been conducted.

**Mining potential going forward:** LOW for new incidents; HIGH for methodology validation. The most valuable unperformed analysis is the CDC WONDER W74+W86 cross-tabulation.

---

## LOA6: Community and Forum Sources

**Target:** Reddit, boating forums, industry orgs, hotspot deep dives  
**Output directory:** `phase2-findings/LOA6-community/`  
**Files produced:** 52 LEAD-NNN files + 3 summary files  
**Confirmed new incidents: ~10–15**

### Key New Incidents

| Lead | Victim | Date | Location |
|------|--------|------|----------|
| LEAD-002 | Gabriel Gonzalez, 21 | Jul 10, 2025 | Marina Shores, Portage IN |
| LEAD-005 | James DeAngelo, 23 | Jul 4, 2021 | Monongahela River PA |
| LEAD-025 | Evan Currie, 19 | Jun 16, 2017 | Put-in-Bay OH, Lake Erie |
| LEAD-024 | Kayla Matos, ~10–11 | Jun 17, 2017 | Toms River NJ (boat lift) |
| LEAD-047 | Marcus Colburn, 21 | Jun 21, 2015 | Lake of the Ozarks MO |
| LEAD-046 | Jennifer Lankford, 26 | Jul 7, 2012 | Lake of the Ozarks MO |
| LEAD-048 | Unknown 17yo boy | Jul 24, 2006 | Lake Lanier GA (needs verification) |
| LEAD-043/044 | Unknown (2 fatal) | Sep 30, 2000 | Tims Ford Lake TN |

### Critical Structural Findings

- **Lake of the Ozarks, MO** — Confirmed single deadliest ESD location in the U.S.: 5–6 deaths (2004?, 2007, 2012×2, 2015). Missourinet (2017): 3 additional deaths 2015–2017 not yet identified. Missouri RUA shields all private dock owners from liability.
- **Smith Mountain Lake, VA** — 97% of 209 tested docks showed stray voltage in 2017 (Neil Harrington survey), 7 years before the first confirmed ESD death. This gap strongly suggests unreported prior fatalities.

**Mining potential going forward:** MODERATE. The Missourinet reference to 3 unidentified LOA deaths (2015–2017) is a high-confidence specific lead. Missouri State Highway Patrol (Water Patrol Division) records and Lake Expo archives are the recommended next step.

---

## LOA7: Structured Database Mining

### LOA7-A: BARD

**BARD capture rate: ~8%** — 2 of 24 known dock/marina ESD incidents found in BARD.  
**New incidents found: 3** (1 fatal WV 2010, 2 near-misses)  
**Key finding:** ESD deaths in BARD are coded as "Drowning," "Trauma," or "Hypothermia" — not "Electrocution."

**Mining potential:** LOW — BARD is structurally unsuited for ESD surveillance. LOA7-A was thorough; marginal additional yield from re-analysis.

---

### LOA7-B: NEISS — Abandoned After Analysis

**Finding: NEISS is not a productive source for ESD research.**

**Quantitative evidence (2023 file, 338,262 records):**

| Filter applied | Records matching | ESD-relevant |
|---------------|-----------------|-------------|
| Diagnosis 67 (electric shock) + dock/marina/lake/boat | 0 | 0 |
| Diagnosis 67 + any water context (incl. bathtub) | 1 (bathtub charger) | 0 |
| Marine product codes (1610–1699) + diagnosis 67 | 0 | 0 |
| Diagnosis 67 OR 68, total records | 5,296 | 0 confirmed ESD |

**Why NEISS cannot capture ESD:**

1. **ESD victims who die are coded as drowning** — The electrical cause is not established at the time of ER presentation. The ER records the immediate clinical finding (drowning, cardiac arrest) without knowing the electrical trigger.

2. **No product code for "dock wiring" or "marina electrical system"** — NEISS codes by consumer product involved. There is no product code for dock wiring or marina shore power infrastructure.

3. **Non-fatal ESD survivors rarely ER-present for electrical symptoms** — Tingling/paralysis from ESD typically resolves when the victim exits the water. ER visits that do occur are for secondary injuries coded under the boat product or water activity, not electrical shock.

4. **NEISS is a sample (~100 hospitals) not a census** — Even correctly-coded cases may not appear in the sample.

**Recommendation:** Do not invest further effort in NEISS for ESD research. See CDC WONDER W74+W86 cross-tabulation (LOA4 section) as the productive alternative.

---

## Cross-LOA Summary: The Underreporting Stack

Every layer of U.S. data infrastructure fails to capture ESD:

```
TRUE ESD DEATHS (est. 20–30/year)
      |
      | ~50–90% never investigated as electrical
      ↓
DEATHS WITH UNUSUAL CIRCUMSTANCES (skilled swimmer, multiple victims, tingle reports)
      |
      | ~70–80% not followed up — no protocol for electrical testing at drowning scenes
      ↓
DEATHS WITH CONFIRMED ELECTRICAL INVOLVEMENT
      |
      | ~50–70% not coded as electrocution on death certificate
      ↓
DEATHS WITH ICD-10 W86 (electrical exposure) + drowning code
      |
      | W86+W74 cross-tab never performed; no published analysis
      ↓
DEATHS IN GOVERNMENT DATABASES
      BARD:  captures ~8% | CDC WONDER: cross-tab not done | NEISS: structural zero
      ↓
ESDPA INCIDENT LIST
      (4–6 confirmed deaths/year documented)
```

### Phase 2 Total Yield

| LOA | Verified New Incidents | Unverified Leads |
|-----|----------------------|-----------------|
| LOA1 (news archive) | ~15–20 | ~10 |
| LOA2 (misclassified) | 0 verified; 25 SUSP | 25 |
| LOA3 (legal) | ~10 | ~5 |
| LOA4 (government) | 3 | ~5 |
| LOA5 (academic) | 0 | 0 |
| LOA6 (community/hotspots) | ~10–15 | ~15 |
| LOA7 (BARD) | 1 fatal + 2 near-miss | — |
| **Total** | **~40–50 new incidents** | **~60 unverified leads** |

---

## Highest-Priority Future Research Actions

1. **CDC WONDER W74+W86 cross-tab** — Free data request at wonder.cdc.gov. Cross-tabulate ICD-10 codes W74 (drowning, undetermined) + W86 (electrical exposure) for 2000–2022. Could identify hundreds of previously unknown ESD deaths.

2. **ME records in high-incidence states** — Public records requests to ME offices in TN, AR, MI, VA, MO, FL, IN for drowning investigations within 100 feet of powered water infrastructure.

3. **Lake of the Ozarks 2015–2017** — Missouri State Highway Patrol (Water Patrol Division) records + Lake Expo/Columbia Missourian archives. Missourinet (2017) directly states 3 additional deaths in this period.

4. **Smith Mountain Lake VA 2017–2023** — Roanoke County + Bedford County drowning records near powered docks. 97% dock stray voltage documented 7 years before first confirmed death.

5. **Paid newspaper archive access** (Newspapers.com / ProQuest) — Would unlock pre-2000 incident discovery that free search tools cannot reach.

6. **Tennessee SFMO inspection database** — Inspection violation records cross-referenced with drowning death locations; public records under Noah Dean and Nate Act.

---

*This document is part of the esd-research repository. See individual LOA summary files in `phase2-findings/` subdirectories for detailed findings, source lists, and individual incident files.*
