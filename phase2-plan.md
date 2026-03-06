# Phase 2 Research Plan: Finding Unlisted ESD Incidents

**Date:** March 6, 2026
**Purpose:** Systematic plan to discover Electric Shock Drowning incidents in the United States that are NOT in the ESDPA list (Shafer & Rifkin, Quality Marine Services LLC).
**Working Directory:** `/opt/repos/esd-research/`

---

## Executive Summary

### What We're Looking For

ESD incidents — deaths and near-misses caused by electrical current leaking into fresh water from docks, marinas, boat lifts, shore power systems, and similar infrastructure — that are absent from the ESDPA's list of ~175 incidents spanning 1981-2025.

### Why It Matters

Phase 1 research revealed that the ESDPA list, which is the most widely cited ESD incident database, has significant data quality problems:

- **Only 39% of incidents** could be verified by independent (non-ESDPA) sources in the initial pass
- **42% of files contain serious flaws** — wrong dates, wrong locations, wrong classifications, phantom duplicates
- **55% had zero independent sources** — all information traces back solely to the ESDPA list
- Date errors average 6-14 months off; one entry (FI-2022-001) is almost certainly a phantom duplicate
- Geographic coverage is severely uneven — Texas (30M+ people, massive boating culture) has only 2 entries; Minnesota ("10,000 Lakes") has 1; entire Pacific Northwest has 1

**Phase 1.5 (MCP Search Campaign, March 2026)** re-searched 58 incidents using Perplexity AI and Brave Web Search, achieving a **43% hit rate** — finding new independent sources for 25 incidents that the initial pass missed. Key outcomes:

- **25 incidents gained new sources** (victim names, news articles, court records, obituaries)
- **15+ date corrections confirmed** via independent sources (ESDPA dates frequently wrong by 6-18 months)
- **1 state correction** — FI-2016-002 listed as South Bend, Iowa; actually South Bend, Indiana
- **Multiple lawsuit/legislation records found** — Samantha Chipley Act (KY), Ameren $2.3M verdict (MO), Silverleaf Resorts suit (TX), Marina Shores suit (IN)
- **Pattern confirmed:** MCP tools most effective when incident has specific searchable details (victim names, lawsuit names, legislation). Victim names are the single most powerful search lever — once identified, obituaries and follow-up coverage cascade.
- **See:** `mcp-search-tracker.md` for full results of the Phase 1.5 campaign

This means the ESDPA list both **overcounts** (phantom duplicates, unverified entries, possible misclassifications) and **undercounts** (vast geographic and temporal gaps). Building an independently verified incident database is essential for any credible epidemiological claim about ESD prevalence.

### Estimated Scale of What's Missing

Based on gap analysis:

- **Gap years** (1990, 1992, 1996, 2004, 2007, 2009) during otherwise active periods suggest **15-30 missing incidents** in documented hotspot regions alone
- **Underrepresented states** (TX, MN, WI, WA, OR, AZ, NV, NC, SC, NY, PA, MD) collectively have far more boating activity than heavily represented states — conservatively **25-75 additional incidents** likely exist
- **Misclassified drownings** — experts estimate ESD may account for an unknown percentage of "unexplained drownings" near docks/marinas. Even a tiny fraction of the ~4,000 annual U.S. drowning deaths would dwarf the ESDPA list
- **Legal records** from wrongful death lawsuits likely contain **10-20 incidents** that never made news
- **Total estimate:** Phase 2 should find **30-100 new verified incidents** and identify **50-200 additional suspected cases** warranting investigation

---

## Source Independence Rules

All Phase 2 research must follow these rules:

1. **NO ESDPA derivatives** — Do not use the ESDPA list, ESDPA website, or any source that simply reproduces the ESDPA list as a primary source. These are what we're trying to independently verify or supplement.
2. **NO mikeholt.com as primary source** — Jim Shafer (ESDPA author) is active on Mike Holt forums. Forum posts may be used for leads but are NOT independent verification.
3. **Minimum 2 independent sources** for any incident to be classified as "verified"
4. **Primary sources preferred:** News articles, court records, coroner/ME reports, government investigations
5. **Secondary sources acceptable:** Obituaries, industry publications, government statistical reports
6. **Tertiary sources (leads only):** Forum posts, social media, blog posts — must be verified against primary sources

---

## Deduplication Protocol

Before creating a new incident file, agents MUST check whether the incident is already in the ESDPA list:

1. **Check by date ± 2 years** — ESDPA dates are frequently wrong by 6-18 months
2. **Check by location** — ESDPA locations are sometimes wrong (Cape Coral vs. North Fort Myers, Lexington vs. Louisville)
3. **Check by victim name** if available
4. **Check by water body name**
5. **If uncertain**, flag as "POSSIBLE MATCH: [FI/NM-YYYY-NNN]" and include in findings for manual review

Cross-reference files:
- `/opt/repos/esd-research/incidents-raw/` — all ESDPA entries as extracted
- `/opt/repos/esd-research/incident-research/` — all Phase 1 research files

---

## Output Format for New Incidents

All new incidents should be written as markdown files in the specified output directory, following this template:

```markdown
# [ID] — Phase 2 Research File

## Incident Summary

| Field | Value |
|-------|-------|
| **Date** | [exact or approximate] |
| **Location** | [city, state, water body, marina if applicable] |
| **Classification** | Fatal Incident / Near Miss / Suspected ESD |
| **Outcome** | Dead: N, Injured: N, Near-miss: N |

**Description:** [narrative summary]

## Sources

1. **[Source Name]** — [title] ([date])
   - URL: [url]
   - Key details: [relevant facts]

2. **[Source Name]** — [title] ([date])
   - URL: [url]
   - Key details: [relevant facts]

## ESDPA Status

- [ ] NOT in ESDPA list (new incident)
- [ ] Possible match: [FI/NM-YYYY-NNN] — [explain why]

## Verification Level

- [ ] Verified (2+ independent sources confirm ESD)
- [ ] Probable (strong circumstantial evidence of ESD)
- [ ] Suspected (pattern matches ESD but not confirmed)

## Details

- **Victim(s):** [name, age, gender if available]
- **Electrical cause:** [if determined]
- **Witnesses:** [relevant testimony]
- **Investigation outcome:** [if known]
- **Legal proceedings:** [if any]

---

*Research completed: [date]*
*Found by: Phase 2, [Line of Attack N]*
```

---

## Line of Attack 1: Direct News Archive Search for Unlisted ESD Incidents

### Strategy

Search news archives systematically for ESD incidents using the established search terms from `search-strategy.md`, targeting:
1. **Gap years** with zero or few documented incidents
2. **Underrepresented geographic regions** with significant boating activity
3. **Known hotspot lakes** where additional unreported incidents likely exist

### Search Platforms

| Platform | Coverage | Cost | Best For |
|----------|----------|------|----------|
| **Perplexity AI** (`perplexity_ask`) | Web-grounded AI search | Free (MCP) | **PRIMARY TOOL.** Best for synthesizing multiple sources. 43% hit rate in Phase 1.5. Use for initial searches. |
| **Brave Web Search** (`brave_web_search`) | Current web index | Free (MCP) | **PRIMARY TOOL.** Best for finding specific URLs, news articles, obituaries. Complements Perplexity. |
| Google News Archive | 1880s-present | Free | Broad initial searches (via web search tools) |
| Newspapers.com | 1700s-present, 870M+ pages | $$ | Deep historical searches (paywalled; snippets sometimes visible) |
| Chronicling America (LOC) | 1777-1963 | Free | Pre-digital era |
| Google Scholar | Academic papers | Free | Peer-reviewed sources |

**Phase 1.5 Lessons for Tool Usage:**
- Start with `perplexity_ask` for a synthesized overview, then use `brave_web_search` to find specific URLs
- Victim names are the strongest search lever — search for name + "obituary" and name + "electrocution" once identified
- Lawsuit/legislation names are the second strongest lever — search for bill numbers, case names, law firm names
- Pre-2000 incidents rarely yield results unless they involved notable victims or spawned legislation
- Local newspaper archives (pre-2005) are often not indexed — results skew toward incidents with TV or wire service coverage

### Priority Targets

#### Tier 1: Gap Years in Hotspot States (Highest Expected Yield)

Search these year-state combinations first:

| Year | States to Search | Rationale |
|------|-----------------|-----------|
| 1990 | OK, TN, AR, MI, FL | Zero incidents documented; surrounded by active years |
| 1992 | OK, TN, AR, MI, FL | Zero incidents; OK cluster was 1989-1993 |
| 1996 | All hotspot states | Zero incidents; mid-1990s gap |
| 2004 | TN, AR, MI, FL, OH | Only 1-2 incidents despite 6+ in 2003 and 2006 |
| 2007 | All hotspot states | Minimal incidents |
| 2009 | All hotspot states | Zero incidents despite active 2008 and 2010 |

#### Tier 2: Underrepresented States (Highest Geographic Gap)

| State | Population | Known Incidents | Major Water Bodies | Expected Gap |
|-------|-----------|----------------|-------------------|-------------|
| Texas | 30M+ | 2 | Travis, Texoma, Toledo Bend, Conroe, Sam Rayburn, Canyon, Possum Kingdom, Lewisville | SEVERE |
| Minnesota | 5.7M | 1 | Minnetonka, Mille Lacs, Vermillion, 10,000+ lakes | SEVERE |
| Wisconsin | 5.9M | 1-2 | Geneva, Winnebago, Mendota, Minocqua chain | SEVERE |
| New York | 19M+ | 1-2 | Finger Lakes, George, Champlain, Erie | MAJOR |
| N. Carolina | 10M+ | 1-2 | Norman, Wylie, High Rock, Jordan | MAJOR |
| S. Carolina | 5.2M | 1 | Murray, Hartwell, Keowee, Santee Cooper | MAJOR |
| Washington | 7.7M | 0-1 | Washington, Chelan, Sammamish, Union | MAJOR |
| Oregon | 4.2M | 1 | Columbia River marinas, Willamette | MODERATE |
| Arizona | 7.3M | 0 | Mead, Havasu, Powell, Saguaro | MODERATE |
| Maryland | 6.2M | 0 | Chesapeake Bay marinas | MODERATE |

#### Tier 3: Known Hotspot Lakes (Search for Additional Unreported Incidents)

| Location | Known Incidents | Search Target |
|----------|----------------|---------------|
| Lake Hamilton, AR | 3 deaths (1991, 2001, 2008) | KATV says "5 ESD deaths in AR" — find the other 2 |
| NE Oklahoma "Lake A" | 5 deaths (1989-1993) | CDC documented; search for post-1993 incidents |
| Tims Ford Lake, TN | 2+ documented | "~2013" incident referenced but undocumented |
| Smith Mountain Lake, VA | Multiple | First death was 2024; any earlier near-misses? |
| Put-in-Bay, OH | Contradictory data | Was there really a 2000 incident? |

### Evaluating Whether a Found Incident Is Already in the ESDPA List

When an agent finds an ESD incident in news archives:

1. Extract: date, location, victim name/age, water body, outcome
2. Search ESDPA files in `incidents-raw/` for matches on ANY of those fields
3. Allow ±2 years on dates, ±100 miles on location (ESDPA errors are large)
4. If possible match found, note it in the file as "POSSIBLE MATCH" with reasoning
5. If NO match found on any field, classify as NEW INCIDENT
6. When in doubt, include it — manual deduplication is better than missing incidents

### Output

- **Directory:** `/opt/repos/esd-research/phase2-findings/LOA1-news-archive/`
- **File naming:** `NEW-YYYY-NNN.md` (e.g., `NEW-2007-001.md`)
- **Summary file:** `LOA1-summary.md` listing all incidents found with status

---

## Line of Attack 2: Misclassified Drownings

### Strategy

ESD victims drown. The electrical cause is often invisible — no sparks, no burns, no obvious equipment failure. First responders see a drowning victim; the coroner writes "accidental drowning." The electrical fault may be intermittent, resolved by the time investigators arrive, or simply never tested for.

**Proven precedent:** Lucas Ritz (1999), Bryan Higgins (1988), Michael Cunningham (2010), Glen Howard (2003) were ALL initially classified as drownings, later reclassified as electrocutions. This means the reclassification pipeline exists but is triggered only when someone — usually a family member — pushes for further investigation.

### Red Flags That a Drowning May Be ESD

**Strongest indicators (any ONE of these warrants investigation):**

1. **"No water in lungs" / dry drowning at a dock** — Victim died before submersion (electrical cause)
2. **Multiple simultaneous victims** at same dock/marina — Normal drowning rarely takes 2+ people at once
3. **Rescue attempt death** — Skilled adult enters water to save someone, immediately drowns too
4. **Witnesses report "tingling," "shock," "paralysis"** in the water
5. **Electrical burns** found on autopsy
6. **Death certificate later amended** from drowning to electrocution

**Moderate indicators (2+ of these together warrant investigation):**

7. **"Exceptional swimmer" / "strong swimmer" drowned** near dock infrastructure
8. **Child drowned despite adult supervision** near dock, in shallow water, or wearing life jacket
9. **"Went rigid" / "froze up" / "couldn't move"** descriptions from witnesses
10. **Toxicology negative, no medical conditions** — rules out drugs, seizure, heart attack
11. **Drowning near boats connected to shore power**
12. **Drowning during/after electrical storm** (damaged dock wiring)
13. **Multiple unexplained drownings at same location** over years

### Search Queries

**Autopsy red flags:**
```
"no water in lungs" drowning dock OR marina [YEAR]
"autopsy" "no water in lungs" drowning
"dry drowning" dock [LOCATION]
"electrical burns" drowning [LOCATION]
"cause of death" "electrocution" drowning [COUNTY] [STATE]
"death certificate amended" drowning electrocution
"initially ruled drowning" electrocution
```

**Witness language:**
```
"paralyzed in water" drowning
"couldn't move" drowning dock
"felt shock" drowning marina
"tingling in water" drowning
"strong swimmer" drowned dock unexplained
"exceptional swimmer" drowned dock marina
```

**Multiple victims / rescue deaths:**
```
"two drowned" dock OR marina [LOCATION]
"double drowning" marina
"tried to save" drowned dock
"jumped in to help" drowned marina
"father drowned" rescuing child dock
"mother drowned" saving dock
```

**Unexplained drownings near infrastructure:**
```
"unexplained drowning" marina [YEAR]
"mysterious drowning" dock
"cause of death unknown" drowning dock marina
"investigation ongoing" drowning marina
"manner of death: undetermined" drowning dock
```

**Post-investigation electrical findings:**
```
"GFCI tested" after drowning
"electrical inspection" drowning marina
"dock wiring" drowning investigation
"shore power inspected" drowning
"stray voltage" drowning [LAKE]
```

### Coroner/ME Report Sources

- **County coroner websites** — Many now publish annual reports online
- **CDC WONDER** — ICD-10 codes W74 (unspecified drowning) and W86 (electric current exposure)
- **State vital statistics offices** — Death certificate data (may require FOIA)
- **CPSC National Electronic Injury Surveillance System (NEISS)** — Hospital ER data

### Probability Assessment Framework

For each drowning found, rate ESD probability:

| Level | Criteria | Action |
|-------|----------|--------|
| **HIGH** (>70%) | 2+ strongest indicators present | Create incident file as "Probable ESD" |
| **MODERATE** (30-70%) | 1 strongest OR 3+ moderate indicators | Create incident file as "Suspected ESD" |
| **LOW** (10-30%) | 1-2 moderate indicators only | Note in summary; do not create file |
| **UNLIKELY** (<10%) | No ESD indicators; plausible alternative cause | Skip |

### Output

- **Directory:** `/opt/repos/esd-research/phase2-findings/LOA2-misclassified-drownings/`
- **File naming:** `SUSP-YYYY-NNN.md`
- **Summary file:** `LOA2-summary.md`

---

## Line of Attack 3: Legal Record Mining

### Strategy

Wrongful death lawsuits, premises liability cases, and utility company settlements often surface ESD incidents that received minimal or no news coverage. Legal filings contain detailed factual allegations, expert testimony, and specific electrical fault descriptions. The FI-2025-001 (Marina Shores) case demonstrated this: the Schafer & Schafer lawsuit revealed a prior incident 4 days before the fatal event that had received no news coverage.

### Federal Court Records (PACER / CourtListener)

**CourtListener (free):**
```
"electric shock drowning" wrongful death
"electrocution" "marina" wrongful death
"electrocution" "dock" wrongful death
"shore power" electrocution death
"stray voltage" drowning death
"boat lift" electrocution death
"dock" "electrocution" "negligence"
"marina" "electrocution" "premises liability"
"reverse polarity" electrocution death water
"ground fault" drowning death dock
"GFCI" failure drowning death
```

**PACER (federal courts, $0.10/page):**
- Search nature of suit codes: 360 (Personal Injury), 365 (Product Liability)
- Keywords: electrocution + marina, dock, shore power, boat lift
- Wrongful death + electrocution + water/drowning/marina
- Time range: 1990-2025

### State Court Records

Many states have online case search systems. Priority states:

| State | Court System URL | Priority |
|-------|-----------------|----------|
| Tennessee | `courts.tn.gov` | HIGH — 8+ documented incidents |
| Arkansas | `caseinfo.arcourts.gov` | HIGH — Lake Hamilton cluster |
| Michigan | `courts.michigan.gov` | HIGH — 5+ incidents, $50M Clinch Marina suit |
| Oklahoma | `www.oscn.net` | HIGH — 1989-1993 cluster |
| Florida | `myflcourtaccess.com` | MODERATE — 3+ incidents |
| Virginia | `courts.state.va.us` | MODERATE — SML, Lake Montclair |
| Ohio | `ohiocourtrecords.org` | MODERATE — Put-in-Bay |
| Indiana | `mycase.in.gov` | MODERATE — Marina Shores |
| Kentucky | `courts.ky.gov` | MODERATE — Lake Cumberland |
| Texas | `re.search.txcourts.gov` | HIGH (geographic gap) |

Search terms for state courts:
```
"wrongful death" electrocution marina
"wrongful death" electrocution dock
"wrongful death" "electric shock drowning"
"wrongful death" electrocution lake
"premises liability" marina electrocution
"product liability" "shore power"
```

### Law Firm Press Releases and Blog Posts

Law firms publicize large settlements. Search for:
```
site:*.com/blog "electric shock drowning" wrongful death
site:*.com/blog marina electrocution lawsuit
site:*.com/blog dock electrocution wrongful death settlement
"law firm" "electric shock drowning" settlement OR verdict
"wrongful death" marina electrocution settlement million
"jury verdict" dock electrocution drowning
```

**Known law firms involved in ESD cases:**
- Schafer & Schafer LLP (Indiana — Marina Shores)
- Firms involved in Clinch Marina $50M case (Michigan)
- Firms involved in Lake Montclair case (Virginia)
- Search for ESD-specific practice areas

### Insurance and Settlement Databases

- **VerdictSearch** / **JuryVerdictReview** — searchable verdict/settlement databases
- **Westlaw / LexisNexis** — comprehensive case law (subscription required)
- **Google Scholar** case law search — free, covers many published opinions
  ```
  "electric shock drowning" site:scholar.google.com
  "electrocution" "marina" "wrongful death" site:scholar.google.com
  "stray voltage" "drowning" site:scholar.google.com
  ```

### Output

- **Directory:** `/opt/repos/esd-research/phase2-findings/LOA3-legal-records/`
- **File naming:** `LEGAL-YYYY-NNN.md`
- **Summary file:** `LOA3-summary.md`

---

## Line of Attack 4: Regulatory and Government Records

### Strategy

Federal and state agencies investigate deaths in their jurisdictions. Their records often contain detailed technical findings unavailable in news coverage. Key agencies:

### OSHA (Occupational Safety and Health Administration)

**OSHA Fatality and Catastrophe Investigation Summaries:**
- URL: `https://www.osha.gov/fatalities`
- Searchable by keyword, date, state, SIC code
- Covers workplace electrocutions including at marinas and docks

Search terms:
```
electrocution water drowning
electrocution dock marina
electrocution flooded basement
"electric shock" water death
electrocution pool spa
```

**OSHA Inspection Database:**
- URL: `https://www.osha.gov/ords/imis/establishment.html`
- Search by establishment name (marina names)
- Search by SIC code 4493 (Marinas) + violation type

### CPSC (Consumer Product Safety Commission)

**SaferProducts.gov:**
- URL: `https://www.saferproducts.gov/`
- Search: "electric shock drowning," "dock electrocution," "marina electrocution," "shore power cord," "boat lift electrocution," "pool electrocution"

**CPSC Incident Reports / Death Certificates Database:**
- CPSC collects death certificate data for product-related deaths
- May require FOIA request for ESD-related entries
- Search for product categories: shore power cords, boat lifts, dock wiring, pool pumps

**NEISS (National Electronic Injury Surveillance System):**
- URL: `https://www.cpsc.gov/cgibin/NEISSQuery/home.aspx`
- Tracks ER visits; can search for electrocution + water/pool/dock codes

### CDC (Centers for Disease Control and Prevention)

**CDC MMWR (Morbidity and Mortality Weekly Report):**
- Already found: 1989-1993 Oklahoma cluster documented in MMWR
- Search MMWR archives for additional ESD-related reports:
  ```
  site:cdc.gov/mmwr electrocution drowning
  site:cdc.gov/mmwr "electric shock" water
  site:cdc.gov/mmwr "submersible pump" electrocution
  site:cdc.gov/mmwr marina electrocution
  ```

**CDC WONDER:**
- URL: `https://wonder.cdc.gov/`
- Search underlying cause of death data
- ICD-10 codes: W86 (Exposure to electric current), W74 (Unspecified drowning)
- Cross-reference: deaths coded W86 near water bodies

**CDC WISQARS (Web-based Injury Statistics Query and Reporting System):**
- URL: `https://wisqars.cdc.gov/`
- Electrocution fatality data by year, state, age, gender
- Can identify states with elevated electrocution + drowning deaths

### USCG (U.S. Coast Guard)

**Recreational Boating Statistics:**
- URL: `https://uscgboating.org/statistics/accident_statistics.php`
- Annual reports categorize boating fatalities
- Search for "electrocution" as cause of death in boating accidents
- BARD (Boating Accident Report Database) — may require FOIA

### NTSB (National Transportation Safety Board)

**Marine Accident Reports:**
- URL: `https://www.ntsb.gov/investigations/AccidentReports/Pages/marine.aspx`
- Search for recreational boat electrocution incidents
- NTSB investigates some marine casualties

### State-Level Agencies

| Agency Type | Search Target |
|-------------|--------------|
| State DNR / Wildlife agencies | Drowning investigation reports near docks/marinas |
| State electrical inspector boards | Violations at marinas, post-incident inspection reports |
| State fire marshal offices | Electrical fire/electrocution investigations |
| State health departments | Death certificate data, vital statistics |
| Army Corps of Engineers | Deaths at USACE reservoirs (Center Hill, Tims Ford, etc.) |

**FOIA Request Targets (if needed):**
1. USCG — BARD data for all boating electrocution deaths 1980-2025
2. CPSC — Death certificate database entries for electrocution + water/drowning
3. CDC — WONDER data for W86 deaths cross-referenced with W74 (drowning)
4. OSHA — All fatality investigations involving electrocution at marinas or docks

### Output

- **Directory:** `/opt/repos/esd-research/phase2-findings/LOA4-government-records/`
- **File naming:** `GOV-YYYY-NNN.md`
- **Summary file:** `LOA4-summary.md`

---

## Line of Attack 5: Academic and Epidemiological Research

### Strategy

Find peer-reviewed research that (a) documents specific ESD incidents, (b) estimates the prevalence of ESD among drowning deaths, or (c) describes forensic markers of in-water electrocution. Academic papers are high-quality, independently reviewed sources.

### Key Databases

| Database | URL | Coverage |
|----------|-----|----------|
| PubMed / MEDLINE | `pubmed.ncbi.nlm.nih.gov` | Biomedical literature |
| Google Scholar | `scholar.google.com` | Broad academic coverage |
| IEEE Xplore | `ieeexplore.ieee.org` | Electrical engineering |
| NFPA Journal | `nfpa.org/journal` | Fire/electrical safety |
| ProQuest Dissertations | `proquest.com` | Theses and dissertations |
| Scopus | `scopus.com` | Multi-disciplinary |

### Search Terms by Discipline

**Forensic pathology / forensic medicine:**
```
"electric shock drowning" forensic
"electrocution" "freshwater" autopsy
"in-water electrocution" pathology
"electrical" "drowning" "forensic"
"electrocution" "autopsy findings" water
"submerged" "electrocution" forensic pathology
"electrical injury" "immersion" death
```

**Epidemiology / public health:**
```
"electric shock drowning" epidemiology
"electric shock drowning" incidence prevalence
"drowning" "electrocution" "United States" statistics
"drowning" "electrical" cause proportion
"unintentional drowning" "electrocution" underreporting
"marina safety" drowning prevention
"dock electrical safety" public health
```

**Electrical engineering / safety:**
```
"electric shock drowning" IEEE
"stray voltage" "fresh water" marina
"ground fault" marina dock drowning
"GFCI" freshwater effectiveness
"shore power" safety fault current
"electrical safety" marina dock NEC
"leakage current" fresh water electrocution
"equipotential bonding" marina dock
```

**Emergency medicine / EMS:**
```
"electric shock drowning" emergency medicine
"in-water" electrocution rescue
"electrical injury" drowning treatment
"freshwater" electrocution clinical
```

### Key Researchers to Identify

Search for authors who have published on ESD or related topics:
- Authors of the CDC MMWR report on the Oklahoma cluster
- Forensic pathologists who have published on in-water electrocution
- Electrical engineers who have studied marina electrical safety
- Public health researchers studying drowning prevention
- NFPA researchers involved in NEC Article 555 (Marinas and Boatyards)
- ABYC (American Boat and Yacht Council) safety standards authors

### Specific Journals to Check

| Journal | Relevance |
|---------|-----------|
| American Journal of Forensic Medicine and Pathology | Autopsy findings, electrocution diagnosis |
| Journal of Forensic Sciences | Forensic investigation of ESD |
| Forensic Science International | International case reports |
| Injury Prevention | Drowning prevention, ESD awareness |
| IEEE Transactions on Industry Applications | Electrical safety standards |
| NFPA Journal | Fire/electrical safety reporting |
| Journal of the American Medical Association (JAMA) | Major public health findings |
| New England Journal of Medicine | Major case reports |
| Annals of Emergency Medicine | ER-reported cases |

### Output

- **Directory:** `/opt/repos/esd-research/phase2-findings/LOA5-academic/`
- **File naming:** `ACAD-NNN.md` (not date-based; organized by topic)
- **Summary file:** `LOA5-summary.md` — bibliography of all relevant papers found

---

## Line of Attack 6: Community and Forum Sources

### Strategy

ESD survivor communities, marina owner forums, and electrical inspector groups often discuss incidents that never made mainstream news. These are LEAD GENERATION sources — every claim must be verified against primary sources before creating an incident file.

### Reddit Communities

```
site:reddit.com "electric shock drowning"
site:reddit.com electrocuted marina dock
site:reddit.com/r/boating electrocution dock
site:reddit.com/r/boating "electric shock"
site:reddit.com/r/electricians dock drowning electrocution
site:reddit.com/r/electricians marina electrocution
site:reddit.com/r/sailing electrocution dock marina
site:reddit.com/r/liveaboard electrocution shore power
site:reddit.com/r/HomeImprovement dock wiring electrocution
site:reddit.com/r/legaladvice electrocution dock marina
```

### Boating / Marina Forums

| Forum | URL | Search Terms |
|-------|-----|-------------|
| The Hull Truth | `thehulltruth.com` | "electric shock drowning," electrocution dock |
| iBoats | `iboats.com/forums` | shore power electrocution, dock shock |
| Cruisers Forum | `cruisersforum.com` | electrocution marina, shore power death |
| SailNet | `sailnet.com/forums` | electrocution dock, shore power |
| Trawler Forum | `trawlerforum.com` | marina electrocution, shore power |

### Electrical Inspector / Trade Forums

| Forum | Search Terms | Notes |
|-------|-------------|-------|
| IAEI (International Association of Electrical Inspectors) | marina electrocution, dock ESD | Professional group; may have incident reports |
| EC&M (Electrical Construction & Maintenance) | electric shock drowning, dock electrocution | Industry publication; Shafer has published here |
| Reddit r/electricians | dock electrocution, marina wiring | Active community |
| Electrical-Contractor.net | marina electrocution | Contractor forums |

**NOTE:** Mike Holt Forum (forums.mikeholt.com) is EXCLUDED as an independent source because ESDPA author Jim Shafer is active there. It may be used for leads only, and any incident found there must be verified through completely independent sources.

### Facebook Groups

Search Facebook for:
```
"electric shock drowning" group
"ESD awareness"
"marina safety" group
"dock safety" group
"boating safety" group
[specific lake names] + "safety" group
```

**Known ESD awareness organizations:**
- Electric Shock Drowning Prevention Association (ESDPA itself — not independent, but may reference incidents we haven't found)
- BoatUS Foundation — boating safety education
- ABYC Foundation — marine industry safety

### Professional Organizations

| Organization | Relevance | URL |
|-------------|-----------|-----|
| BoatUS | Safety alerts, incident reporting | `boatus.com` |
| Sea Tow Foundation | Boating safety statistics | `boatingsafety.com` |
| ABYC | Marine electrical standards | `abycinc.org` |
| NFPA | NEC Article 555 (Marinas) | `nfpa.org` |
| NASBLA | State boating law administrators | `nasbla.org` |
| ESFI | Electrical Safety Foundation | `esfi.org` |

### Output

- **Directory:** `/opt/repos/esd-research/phase2-findings/LOA6-community/`
- **File naming:** `LEAD-NNN.md` (lead files, pending verification)
- **Summary file:** `LOA6-summary.md`

---

## Implementation Plan for Sonnet Subagents

### General Agent Instructions (include in all prompts)

All agents receive these baseline instructions:

```
## Tools Available
You have access to two primary search tools:
- `perplexity_ask` — AI-powered web search. Use for initial broad queries and synthesis. Best first step.
- `brave_web_search` — Direct web search. Use for finding specific URLs, verifying sources, and targeted queries.

Use BOTH tools for each search task. Start with perplexity_ask for overview, then brave_web_search for specific source URLs.

## Source Rules
- Do NOT use the ESDPA list, ESDPA website, or any source that reproduces the ESDPA list as a primary source
- Do NOT use mikeholt.com as a primary source (ESDPA author is active there)
- Other ESDPA-derivative sites to EXCLUDE: electricshockdrowning.org, ontime59.com, augresmaritimemuseum.org, americanboating.com, 2CoolFishing forum reposts
- Minimum 2 independent sources required to classify an incident as "verified"
- Primary sources preferred: news articles, court records, coroner/ME reports
- If you find only 1 source, still document the incident as "unverified lead"

## Search Strategy (from Phase 1.5 experience)
- Victim names are the #1 search lever. Once you find a name, search: "[name] obituary", "[name] electrocution", "[name] drowning [location]"
- Lawsuit/legislation names are #2: search for bill numbers, case names, law firm names
- For pre-2000 incidents, try: wire service coverage (AP, UPI), legislation/safety campaigns triggered by the death, memorial/park naming
- For 2000+ incidents, local TV station archives (WHAS, WAVE, KATV, etc.) are often the best sources
- When searching, allow ±2 years on dates — ESDPA dates are frequently wrong

## Deduplication
Before concluding an incident is new, check if it could match any known ESDPA incident with wrong dates/locations. ESDPA dates are frequently off by 6-18 months. ESDPA locations are sometimes wrong by city, county, or even STATE (e.g., South Bend Iowa vs Indiana). If uncertain, flag as "POSSIBLE MATCH" and include your reasoning.

## Output Format
Write each incident as a separate .md file using the template in phase2-plan.md. Name files according to the convention for your Line of Attack. Also maintain a summary file listing all incidents found. Write files using `sudo tee /path/to/file` since the repo is owned by devuser.

## What Counts as ESD
Electric Shock Drowning = death or injury caused by electrical current leaking into water from infrastructure (docks, marinas, boat lifts, shore power, pumps, pool equipment, etc.) while the victim is IN the water.

EXCLUDE: direct contact electrocution (touching live wire on land), lightning strikes, electrocution on land where body fell into water, bathtub electrocutions, international incidents.

INCLUDE: freshwater dock/marina electrocutions, boat lift electrocutions, pool/spa equipment electrocutions where victim was in water, houseboat shore power electrocutions, flooded basement electrocutions.
```

---

### LOA1 Agents: Direct News Archive Search

#### Agent LOA1-A: Gap Years Search (1990, 1992, 1996)

```
You are researching Electric Shock Drowning (ESD) incidents in the United States. Your task is to find ESD incidents that occurred in 1990, 1992, and 1996 — years with ZERO documented incidents in the existing database despite surrounding years having multiple incidents.

## Instructions
Search for each year in combination with known hotspot states (Oklahoma, Tennessee, Arkansas, Michigan, Florida, Kentucky, Virginia, Ohio) and generic national searches.

## Search Queries to Run
For EACH of the three years (1990, 1992, 1996), run these searches:

1. "electrocuted" OR "electric shock" drowning dock [YEAR]
2. "electrocuted" OR "electric shock" drowning marina [YEAR]
3. electrocution drowning dock [YEAR]
4. "electrocuted swimming" [YEAR]
5. "electrocuted" dock drowning Oklahoma [YEAR]
6. "electrocuted" dock drowning Tennessee [YEAR]
7. "electrocuted" dock drowning Arkansas [YEAR]
8. "electrocuted" dock drowning Michigan [YEAR]
9. "electrocuted" dock drowning Florida [YEAR]
10. "drowning" "electric" dock [YEAR]

For any incident found, search for additional sources to verify:
- "[victim name] obituary [city] [year]"
- "[location] drowning electrocution [year]"
- "[lake/marina name] electrocution"

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA1-news-archive/
File naming: NEW-[YEAR]-NNN.md
Summary: LOA1-A-summary.md

[Include general agent instructions from above]
```

#### Agent LOA1-B: Gap Years Search (2004, 2007, 2009)

```
You are researching Electric Shock Drowning (ESD) incidents in the United States. Your task is to find ESD incidents that occurred in 2004, 2007, and 2009 — years with very few or zero documented incidents despite surrounding years having multiple incidents.

## Instructions
Search for each year in combination with known hotspot states and generic national searches. These years have better digital news coverage than 1990s, so expect more results.

## Search Queries to Run
For EACH of the three years (2004, 2007, 2009), run these searches:

1. "electric shock drowning" [YEAR]
2. "electrocuted" drowning dock marina [YEAR]
3. electrocution drowning dock [YEAR]
4. "electrocuted while swimming" [YEAR]
5. "electrocuted in water" [YEAR]
6. drowning electrocution marina [YEAR] Tennessee OR Arkansas OR Michigan OR Florida OR Oklahoma
7. "dock electrocution" [YEAR]
8. "houseboat" electrocution [YEAR]
9. "boat lift" electrocution [YEAR]
10. "shore power" electrocution drowning [YEAR]

For any incident found, search for additional sources to verify.

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA1-news-archive/
File naming: NEW-[YEAR]-NNN.md
Summary: LOA1-B-summary.md

[Include general agent instructions from above]
```

#### Agent LOA1-C: Texas and Southwest Search (1980-2025)

```
You are researching Electric Shock Drowning (ESD) incidents in Texas, Arizona, Nevada, and New Mexico. Texas is a SEVERE gap — only 2 incidents documented for a state with 30M+ people and massive lake recreation. Arizona/Nevada have major boating destinations (Lake Mead, Havasu, Powell) with zero documented incidents.

## Search Queries to Run

### Texas (priority — allocate 60% of your searches here)
1. "electrocuted" OR "electric shock" drowning "Lake Travis" Texas
2. "electrocuted" OR "electric shock" drowning "Lake Texoma"
3. "electrocuted" OR "electric shock" drowning "Toledo Bend"
4. "electrocuted" OR "electric shock" drowning "Lake Conroe" Texas
5. "electrocuted" OR "electric shock" drowning "Canyon Lake" Texas
6. "electrocuted" OR "electric shock" drowning "Possum Kingdom Lake"
7. "electrocuted" OR "electric shock" drowning dock marina Texas
8. "electrocuted" OR "electric shock" drowning "Sam Rayburn"
9. "electrocuted" OR "electric shock" drowning "Lake Lewisville"
10. "dock electrocution" Texas lake

### Arizona / Nevada
11. "electrocuted" OR "electric shock" drowning "Lake Mead"
12. "electrocuted" OR "electric shock" drowning "Lake Havasu"
13. "electrocuted" OR "electric shock" drowning "Lake Powell"
14. "electrocuted" OR "electric shock" drowning "Saguaro Lake"
15. drowning marina electrocution Arizona OR Nevada

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA1-news-archive/
File naming: NEW-[YEAR]-NNN.md
Summary: LOA1-C-summary.md

[Include general agent instructions from above]
```

#### Agent LOA1-D: Pacific Northwest and Upper Midwest Search (1980-2025)

```
You are researching Electric Shock Drowning (ESD) incidents in the Pacific Northwest (Washington, Oregon, Idaho) and Upper Midwest (Minnesota, Wisconsin, Illinois). These regions have extensive lake recreation and marina infrastructure but near-zero documented ESD incidents — a pattern suggesting underreporting rather than absence.

## Search Queries to Run

### Pacific Northwest
1. "electrocuted" OR "electric shock" drowning "Lake Washington" Washington
2. "electrocuted" OR "electric shock" drowning "Lake Chelan"
3. "electrocuted" OR "electric shock" drowning marina Washington state
4. "electrocuted" OR "electric shock" drowning marina Oregon
5. "electrocuted" OR "electric shock" drowning "Coeur d'Alene" Idaho

### Upper Midwest
6. "electrocuted" OR "electric shock" drowning "Lake Minnetonka" Minnesota
7. "electrocuted" OR "electric shock" drowning Minnesota lake dock
8. "electrocuted" OR "electric shock" drowning "Lake Geneva" Wisconsin
9. "electrocuted" OR "electric shock" drowning Wisconsin lake dock marina
10. "electrocuted" OR "electric shock" drowning Illinois lake dock marina
11. "electrocuted" OR "electric shock" drowning "Chain O'Lakes" Illinois
12. dock electrocution drowning Minnesota OR Wisconsin OR Illinois

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA1-news-archive/
File naming: NEW-[YEAR]-NNN.md
Summary: LOA1-D-summary.md

[Include general agent instructions from above]
```

#### Agent LOA1-E: Carolinas, Northeast, and Mid-Atlantic Search (1980-2025)

```
You are researching Electric Shock Drowning (ESD) incidents in the Carolinas (NC, SC, GA), Northeast (NY, PA, New England), and Mid-Atlantic (MD, DE, NJ). These regions have numerous large lakes and extensive coastal marina infrastructure with minimal documented ESD incidents.

## Search Queries to Run

### Carolinas
1. "electrocuted" OR "electric shock" drowning "Lake Norman" North Carolina
2. "electrocuted" OR "electric shock" drowning "Lake Murray" South Carolina
3. "electrocuted" OR "electric shock" drowning "Lake Hartwell"
4. "electrocuted" OR "electric shock" drowning "Lake Keowee"
5. dock electrocution drowning North Carolina OR South Carolina OR Georgia

### Northeast
6. "electrocuted" OR "electric shock" drowning "Finger Lakes" OR "Seneca Lake" OR "Cayuga Lake"
7. "electrocuted" OR "electric shock" drowning "Lake Champlain"
8. "electrocuted" OR "electric shock" drowning "Lake George" New York
9. dock electrocution drowning New York OR Pennsylvania

### Mid-Atlantic
10. "electrocuted" OR "electric shock" drowning "Chesapeake Bay" marina Maryland
11. dock electrocution drowning Maryland OR Delaware OR New Jersey
12. marina electrocution drowning New England OR Maine OR Massachusetts OR Connecticut

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA1-news-archive/
File naming: NEW-[YEAR]-NNN.md
Summary: LOA1-E-summary.md

[Include general agent instructions from above]
```

---

### LOA2 Agents: Misclassified Drownings

#### Agent LOA2-A: Autopsy Red Flags Search

```
You are searching for drownings near docks, marinas, and boats that show autopsy red flags for Electric Shock Drowning — particularly "no water in lungs" findings, electrical burns, or death certificates later amended from drowning to electrocution.

## Search Queries to Run

1. "no water in lungs" drowning dock OR marina
2. "autopsy" "no water in lungs" drowning
3. "death certificate amended" drowning electrocution
4. "initially ruled drowning" later electrocution
5. "cause of death changed" drowning electrocution
6. "electrical burns" drowning dock OR marina
7. "coroner" "revised ruling" drowning electrocution
8. "dry drowning" dock OR marina
9. "manner of death: undetermined" drowning dock marina
10. "autopsy" drowning "instantaneous death" dock
11. "later determined" electrocution drowning
12. "reclassified" drowning electrocution

For each case found, assess ESD probability using the criteria in the phase2-plan.md probability assessment framework.

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA2-misclassified-drownings/
File naming: SUSP-[YEAR]-NNN.md
Summary: LOA2-A-summary.md

[Include general agent instructions from above]
```

#### Agent LOA2-B: Skilled Swimmer and Rescue Attempt Drownings

```
You are searching for drownings near docks and marinas where the victim was described as a "strong swimmer," "exceptional swimmer," or where a rescuer drowned trying to save someone — both are classic ESD patterns because electrical paralysis explains why capable swimmers drown in familiar water.

## Search Queries to Run

1. "strong swimmer" drowned dock OR marina
2. "exceptional swimmer" drowned dock OR marina
3. "swim team" member drowned dock OR marina unexplained
4. "competitive swimmer" drowned dock OR marina
5. "lifeguard" drowned dock (off-duty lifeguard drowning is highly suspicious)
6. "tried to save" drowned dock OR marina
7. "jumped in to help" drowned dock OR marina
8. "rescue attempt" drowned dock marina
9. "father drowned" rescuing child dock OR marina OR lake
10. "double drowning" dock OR marina
11. "two drowned" dock OR marina same day
12. "couldn't move" drowning dock OR marina

For each case found, look for additional details: Was electricity later found? Were other witnesses affected? Was the dock/marina later inspected?

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA2-misclassified-drownings/
File naming: SUSP-[YEAR]-NNN.md
Summary: LOA2-B-summary.md

[Include general agent instructions from above]
```

#### Agent LOA2-C: Multiple Victims and Witness Electrical Sensations

```
You are searching for drowning incidents near docks and marinas where multiple people were affected simultaneously or where witnesses reported feeling electrical sensations (tingling, shock, numbness) in the water. These are among the strongest indicators that a drowning was actually ESD.

## Search Queries to Run

1. "felt shock" drowning marina OR dock
2. "tingling in water" drowning
3. "numbness" drowning dock OR marina witness
4. "felt like being tased" water
5. "paralyzed in water" drowning
6. "froze up" drowning dock OR marina OR lake
7. "went rigid" water drowning
8. "others treated" drowning marina OR dock
9. "multiple victims" drowning dock OR marina
10. "three drowned" dock OR marina
11. "mysterious drowning" dock OR marina
12. "unexplained drowning" marina investigation

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA2-misclassified-drownings/
File naming: SUSP-[YEAR]-NNN.md
Summary: LOA2-C-summary.md

[Include general agent instructions from above]
```

---

### LOA3 Agents: Legal Record Mining

#### Agent LOA3-A: Federal and State Court Search

```
You are mining court records for wrongful death lawsuits and premises liability cases related to Electric Shock Drowning. Legal filings often surface incidents that received minimal news coverage and contain detailed factual allegations.

## Search Queries to Run

### Google Scholar Case Law
1. "electric shock drowning" site:scholar.google.com
2. "electrocution" "marina" "wrongful death" site:scholar.google.com
3. "stray voltage" "drowning" site:scholar.google.com
4. "dock" "electrocution" "wrongful death" site:scholar.google.com
5. "shore power" electrocution death site:scholar.google.com
6. "boat lift" electrocution death site:scholar.google.com

### CourtListener / General Web
7. "wrongful death" "electric shock drowning"
8. "wrongful death" electrocution marina dock
9. "premises liability" electrocution marina
10. "negligence" electrocution marina drowning settlement OR verdict
11. "marina" electrocution lawsuit OR suit OR complaint
12. "dock" electrocution wrongful death settlement million

## For each case found:
- Extract the incident date, location, victim name, and outcome from the case
- Search for the underlying incident in news archives
- Determine if the incident is already in the ESDPA list

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA3-legal-records/
File naming: LEGAL-[YEAR]-NNN.md
Summary: LOA3-A-summary.md

[Include general agent instructions from above]
```

#### Agent LOA3-B: Law Firm and Settlement Search

```
You are searching law firm websites, press releases, and verdict databases for ESD-related wrongful death cases. Law firms publicize large settlements and verdicts, and their case descriptions often contain detailed incident narratives.

## Search Queries to Run

1. "electric shock drowning" lawyer OR attorney OR "law firm"
2. marina electrocution wrongful death lawyer OR attorney
3. dock electrocution drowning settlement verdict
4. "wrongful death" marina electrocution settlement million
5. "jury verdict" dock electrocution drowning
6. "shore power" wrongful death lawsuit
7. marina liability electrocution death settlement
8. "boat lift" electrocution wrongful death lawsuit
9. "stray voltage" drowning lawyer OR attorney
10. pool electrocution wrongful death settlement verdict

## Also search for known case firms:
11. "Schafer and Schafer" electrocution (Indiana firm from Marina Shores case)
12. "Clinch Marina" lawsuit OR settlement (Michigan $50M case)

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA3-legal-records/
File naming: LEGAL-[YEAR]-NNN.md
Summary: LOA3-B-summary.md

[Include general agent instructions from above]
```

#### Agent LOA3-C: Insurance and Regulatory Settlement Search

```
You are searching for ESD incidents documented in insurance industry publications, regulatory enforcement actions, and state attorney general records. These sources capture incidents that may not appear in news or court records.

## Search Queries to Run

1. "marina insurance" electrocution liability claim
2. "marina liability" electrocution drowning
3. OSHA citation marina electrocution
4. OSHA fatality investigation marina OR dock electrocution
5. "state attorney general" marina electrocution
6. "building code violation" marina electrocution
7. "electrical code violation" dock drowning death
8. "NEC" violation marina electrocution death
9. "electrical inspection" marina death after drowning
10. CPSC recall "shore power" OR "dock" OR "boat lift" electrocution

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA3-legal-records/
File naming: LEGAL-[YEAR]-NNN.md
Summary: LOA3-C-summary.md

[Include general agent instructions from above]
```

---

### LOA4 Agents: Regulatory and Government Records

#### Agent LOA4-A: OSHA and CPSC Records Search

```
You are searching federal safety agency databases for ESD-related incidents.

## Search Targets

### OSHA
1. Search OSHA fatality reports (osha.gov/fatalities) for: electrocution water, electrocution dock, electrocution marina, electrocution pool, electrocution flooded
2. Search OSHA inspection database for SIC 4493 (Marinas) + electrocution
3. Search for OSHA news releases about marina/dock electrocutions

### CPSC
4. Search SaferProducts.gov for: "electric shock drowning," "dock electrocution," "marina electrocution," "shore power," "boat lift electrocution," "pool electrocution"
5. Search for CPSC recalls: shore power cord, dock wiring, boat lift, pool pump
6. Search for CPSC staff reports or special studies on electrocution near water

### General searches
7. site:osha.gov electrocution water drowning
8. site:osha.gov electrocution dock marina
9. site:cpsc.gov "electric shock drowning"
10. site:cpsc.gov electrocution dock OR marina OR pool

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA4-government-records/
File naming: GOV-[YEAR]-NNN.md
Summary: LOA4-A-summary.md

[Include general agent instructions from above]
```

#### Agent LOA4-B: CDC and Coast Guard Records Search

```
You are searching CDC databases and U.S. Coast Guard records for ESD-related data.

## Search Targets

### CDC
1. Search MMWR archives: site:cdc.gov/mmwr electrocution drowning
2. Search MMWR: site:cdc.gov/mmwr "electric shock" water
3. Search MMWR: site:cdc.gov/mmwr marina electrocution
4. Search MMWR: "submersible pump" electrocution
5. Search CDC WISQARS for electrocution fatality data by state/year
6. Search for CDC publications on drowning that mention electrical causes

### Coast Guard
7. Search USCG recreational boating statistics: site:uscgboating.org electrocution
8. Search for USCG boating accident reports involving electrocution
9. "Coast Guard" recreational boating fatality electrocution
10. "Coast Guard" marine casualty report electrocution drowning

### Army Corps of Engineers (manages many reservoirs where ESD occurs)
11. site:usace.army.mil drowning electrocution
12. "Corps of Engineers" reservoir drowning electrocution

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA4-government-records/
File naming: GOV-[YEAR]-NNN.md
Summary: LOA4-B-summary.md

[Include general agent instructions from above]
```

#### Agent LOA4-C: State Agency Records Search

```
You are searching state-level agency records for ESD incidents. Focus on hotspot states and underrepresented states with major boating infrastructure.

## Search Targets

### State DNR / Wildlife Agencies
1. site:tn.gov drowning electrocution dock marina (Tennessee — 8+ known incidents)
2. site:michigan.gov drowning electrocution dock marina (Michigan — 5+ known)
3. "Texas Parks and Wildlife" drowning electrocution dock
4. "Minnesota DNR" drowning electrocution dock
5. "Wisconsin DNR" drowning electrocution dock

### State Electrical Inspector Records
6. "[state] electrical inspector" marina electrocution violation
7. "[state] building code" marina dock electrocution death

### General state searches for underrepresented states
8. drowning electrocution dock OR marina Texas
9. drowning electrocution dock OR marina Minnesota
10. drowning electrocution dock OR marina Wisconsin
11. drowning electrocution dock OR marina North Carolina
12. drowning electrocution dock OR marina Arizona

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA4-government-records/
File naming: GOV-[YEAR]-NNN.md
Summary: LOA4-C-summary.md

[Include general agent instructions from above]
```

---

### LOA5 Agents: Academic and Epidemiological Research

#### Agent LOA5-A: Medical and Forensic Literature

```
You are searching medical and forensic science literature for publications about Electric Shock Drowning, in-water electrocution, and the forensic diagnosis of electrocution in drowning victims.

## Search Queries to Run

### PubMed
1. Search PubMed for: "electric shock drowning"
2. Search PubMed for: electrocution freshwater drowning
3. Search PubMed for: "in-water electrocution"
4. Search PubMed for: electrocution drowning forensic
5. Search PubMed for: "electrical injury" drowning immersion
6. Search PubMed for: electrocution autopsy water submersion

### Google Scholar
7. "electric shock drowning" epidemiology
8. "electric shock drowning" incidence United States
9. "in-water electrocution" forensic pathology
10. "drowning" "electrocution" misclassification underreporting
11. "stray voltage" freshwater drowning death
12. "marina" "dock" electrical safety drowning death

## For each paper found:
- Record authors, title, journal, year, DOI
- Note whether it documents specific incidents (and if so, are they in the ESDPA list?)
- Note any prevalence/incidence estimates
- Note key forensic markers for diagnosing ESD
- Identify the key researchers and their institutional affiliations

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA5-academic/
File naming: ACAD-NNN.md (numbered sequentially)
Summary: LOA5-A-summary.md — full bibliography

[Include general agent instructions from above]
```

#### Agent LOA5-B: Engineering and Safety Standards Literature

```
You are searching electrical engineering, safety standards, and industry publications for research on Electric Shock Drowning, marina electrical safety, and dock electrical hazards.

## Search Queries to Run

### IEEE Xplore / Engineering
1. "electric shock drowning" IEEE
2. "stray voltage" marina dock freshwater
3. "ground fault" marina dock drowning
4. "GFCI" freshwater effectiveness marina
5. "shore power" safety fault current marina
6. "equipotential bonding" marina dock

### NFPA / Safety Standards
7. site:nfpa.org "electric shock drowning"
8. site:nfpa.org marina electrical safety statistics
9. "NEC Article 555" marina safety electrocution
10. "NFPA 303" marina fire protection

### Industry Publications
11. "Marina Dock Age" electrocution OR "electric shock drowning"
12. "Soundings Trade Only" electrocution drowning
13. "Boating Industry" "electric shock drowning"
14. BoatUS "electric shock drowning" OR electrocution dock
15. ABYC "electric shock drowning" OR dock electrocution

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA5-academic/
File naming: ACAD-NNN.md
Summary: LOA5-B-summary.md

[Include general agent instructions from above]
```

#### Agent LOA5-C: Epidemiological and Public Health Data

```
You are searching for epidemiological data that quantifies ESD's share of drowning deaths in the United States, and for public health research on drowning prevention that addresses electrical hazards.

## Search Queries to Run

1. "electric shock drowning" prevalence OR incidence OR statistics OR epidemiology
2. "drowning" "electrocution" percentage OR proportion OR "how many"
3. "underreported" "electric shock drowning"
4. "undiagnosed" electrocution drowning
5. "misclassified drowning" electrocution
6. CDC WONDER drowning electrocution ICD-10 W86 W74
7. "drowning prevention" electrical hazard dock marina
8. "recreational boating fatalities" electrocution statistics
9. USCG boating statistics electrocution percentage
10. "drowning investigation" protocol electrical testing
11. "coroner" OR "medical examiner" training electrocution drowning detection
12. Congressional testimony OR hearing "electric shock drowning"

## For each source found:
- Record any specific incident counts or prevalence estimates
- Note the methodology used
- Assess the quality/reliability of the estimate
- Identify the key researchers and organizations

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA5-academic/
File naming: ACAD-NNN.md
Summary: LOA5-C-summary.md

[Include general agent instructions from above]
```

---

### LOA6 Agents: Community and Forum Sources

#### Agent LOA6-A: Reddit and Boating Forum Search

```
You are searching Reddit and boating forums for firsthand accounts or discussions of ESD incidents that may not appear in mainstream news coverage. These are LEAD GENERATION searches — every incident found must be flagged for verification against primary sources.

## Search Queries to Run

### Reddit
1. site:reddit.com "electric shock drowning"
2. site:reddit.com electrocuted dock OR marina swimming
3. site:reddit.com/r/boating electrocution OR "electric shock"
4. site:reddit.com/r/electricians dock drowning electrocution
5. site:reddit.com/r/sailing electrocution dock marina
6. site:reddit.com/r/liveaboard electrocution shore power
7. site:reddit.com/r/legaladvice electrocution dock marina drowning

### Boating Forums
8. site:thehulltruth.com "electric shock drowning" OR electrocution dock
9. site:cruisersforum.com electrocution marina OR dock OR "shore power"
10. site:iboats.com electrocution dock OR marina

## For each incident mentioned:
- Extract date, location, victim info if available
- Search for primary sources (news articles, coroner reports) to verify
- Flag as "LEAD — NEEDS VERIFICATION" if only forum source

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA6-community/
File naming: LEAD-NNN.md
Summary: LOA6-A-summary.md

[Include general agent instructions from above]
```

#### Agent LOA6-B: Industry Organizations and Safety Alert Search

```
You are searching industry organizations, safety foundations, and professional groups for ESD incident reports, safety alerts, and awareness campaigns that may reference specific incidents not in the ESDPA list.

## Search Queries to Run

1. site:boatus.com "electric shock drowning" OR electrocution dock marina
2. site:boatus.org "electric shock drowning"
3. site:abycinc.org "electric shock drowning" OR electrocution
4. site:esfi.org "electric shock drowning" OR dock electrocution
5. site:nasbla.org "electric shock drowning" OR electrocution
6. "BoatUS Foundation" "electric shock drowning" safety alert
7. "ABYC" "electric shock drowning" safety bulletin
8. "Electrical Safety Foundation International" drowning electrocution
9. "National Association of State Boating Law Administrators" electrocution
10. "marina safety" "electric shock drowning" webinar OR presentation OR conference

## Also search for:
11. "electric shock drowning" awareness campaign [YEAR] (may reference local incidents)
12. "ESD prevention" marina OR dock incident report

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA6-community/
File naming: LEAD-NNN.md
Summary: LOA6-B-summary.md

[Include general agent instructions from above]
```

#### Agent LOA6-C: Known Hotspot Deep Dive

```
You are doing deep searches at known ESD hotspot locations to find additional incidents that may not be in the ESDPA list. Focus on locations with confirmed multiple incidents — these are the most likely to have additional unreported events.

## Search Targets

### Lake Hamilton, Arkansas (3 documented deaths — KATV says 5 total in AR)
1. drowning "Lake Hamilton" Arkansas 1980-2025
2. "Lake Hamilton" electrocution OR "electric shock"
3. drowning dock "Hot Springs" Arkansas lake
4. "Lake Hamilton" drowning investigation

### Northeastern Oklahoma "Lake A" Cluster (CDC documented 5 deaths 1989-1993)
5. drowning "Grand Lake" Oklahoma 1980-2025
6. drowning "Lake Hudson" Oklahoma 1980-2025
7. electrocution dock Oklahoma lake 1980-2025
8. "submersible pump" electrocution Oklahoma

### Tims Ford Lake, Tennessee (2+ documented, ~2013 referenced)
9. drowning "Tims Ford Lake" 2012 OR 2013 OR 2014
10. electrocution "Tims Ford Lake" 2010-2020
11. drowning "Tims Ford Lake" dock OR marina

### Smith Mountain Lake, Virginia (2024 first death — any earlier near-misses?)
12. "stray voltage" "Smith Mountain Lake" before 2024
13. "electric shock" "Smith Mountain Lake"
14. drowning "Smith Mountain Lake" dock 1990-2023

### Michigan Marinas (5+ documented)
15. drowning marina Michigan electrocution 1980-2025

## Output
Write results to: /opt/repos/esd-research/phase2-findings/LOA6-community/
File naming: LEAD-NNN.md
Summary: LOA6-C-summary.md

[Include general agent instructions from above]
```

---

## Prioritization

### Ranking by Expected Yield, Effort, and Confidence

| Rank | Line of Attack | Expected Yield | Effort | Confidence | Rationale |
|------|---------------|---------------|--------|------------|-----------|
| **1** | **LOA1: News Archive Search** | **HIGH (20-50 incidents)** | Moderate | **HIGH** | Most incidents were reported in local news; gaps likely reflect search gaps, not reporting gaps. Digital news archives have grown dramatically; many 1990s-2000s articles now searchable that weren't when ESDPA was compiled. |
| **2** | **LOA3: Legal Record Mining** | **MODERATE (10-25 incidents)** | Moderate | **HIGH** | Lawsuits contain verified factual details and often surface incidents with minimal news coverage. The Marina Shores case proved this approach works. Google Scholar case law is free and comprehensive. |
| **3** | **LOA4: Government Records** | **MODERATE (5-15 incidents)** | High | **HIGH** | OSHA, CPSC, and USCG maintain structured databases. USCG boating accident data in particular should capture many marina electrocutions. Effort is high because some data requires FOIA requests. |
| **4** | **LOA5: Academic Research** | **LOW-MOD (5-10 incidents + prevalence data)** | Low | **VERY HIGH** | Peer-reviewed sources are the gold standard. Papers may reference specific incidents AND provide epidemiological context. Main value is the prevalence estimates, not raw incident count. |
| **5** | **LOA2: Misclassified Drownings** | **UNCERTAIN (5-50+ incidents)** | Very High | **LOW-MODERATE** | Potentially the largest category but hardest to confirm. Many of these may remain "suspected" rather than "verified." Best used to estimate the dark figure, not to build verified incident list. |
| **6** | **LOA6: Community Sources** | **LOW (3-10 leads)** | Low | **LOW** | Forums and social media are lead generation only. Every claim requires independent verification. But effort is low and occasionally surfaces incidents completely absent from other sources. |

### Recommended Execution Order

**Practical constraint:** Running too many agents in parallel hits API rate limits. Phase 1.5 found that **6 agents at a time** is the practical maximum. Each agent takes 1-3 minutes depending on search depth.

**Phase 2A (Run first — highest ROI):**
1. LOA1 agents A through E (5 news archive agents) — run in batches of 6 with LOA5-A
2. LOA5-A (medical/forensic literature) — run in parallel with LOA1

**Phase 2B (Run second — builds on Phase 2A findings):**
3. LOA3-A and LOA3-B (court records and law firm search) — run in parallel
4. LOA4-A and LOA4-B (OSHA/CPSC and CDC/USCG) — run in parallel
5. LOA5-B and LOA5-C (engineering literature and epi data) — run in parallel

**Phase 2C (Run third — lead generation and deep dives):**
6. LOA2-A, LOA2-B, LOA2-C (misclassified drownings) — run in parallel
7. LOA6-A, LOA6-B, LOA6-C (community and forum sources) — run in parallel
8. LOA4-C (state agency records) — run after LOA1 identifies which states need attention

**Phase 2D (Follow-up):**
9. Verification agents for all leads generated by LOA6
10. Deep dives into any new geographic clusters identified by LOA1-LOA4
11. FOIA requests to USCG, CPSC, CDC if initial searches show promise

### Total Agent Count

| Phase | Agents | Parallelism | Est. Time |
|-------|--------|-------------|-----------|
| 2A | 6 agents (LOA1-A through E + LOA5-A) | 6 at once | ~5 min |
| 2B | 6 agents (LOA3-A,B + LOA3-C + LOA4-A,B + LOA5-B,C) | 6 at once | ~5 min |
| 2C | 7 agents (LOA2-A,B,C + LOA6-A,B,C + LOA4-C) | 6+1 | ~10 min |
| 2D | Variable | Depends on findings | Variable |
| **Total** | **~19 initial + follow-ups** | | ~20-30 min |

---

## New Lines of Attack: LOA7–LOA14 (from Perplexity Analysis)

*Source: `perplexity-additional-data-sources-and-lines-of-attack.md`*

These additional LOAs were identified through systematic analysis of data sources not covered by LOA1–LOA6. They are ordered by expected impact and feasibility.

### LOA7: Structured Database Mining (BARD + NEISS + NFIRS)

**Rationale:** Unlike LOA1–LOA6 which rely on text search, LOA7 involves filtering structured databases by cause-of-death codes and location types. This is qualitatively different and likely the single highest-yield immediate action.

**BARD data is already downloaded** at `/opt/repos/esd-research/BARD-dataset-2009-2023-csv/`. The Deaths CSVs contain a `CauseofDeath` field that can be filtered for electrocution. Cross-reference against ESDPA list by date and state.

| Database | Records | Coverage | Cost | Priority |
|----------|---------|----------|------|----------|
| **BARD (USCG)** | 8,935 deaths (2009–2023) | Boating accidents nationwide | Free — **already downloaded** | **IMMEDIATE** |
| **NEISS (CPSC)** | 20 years of ER visits | ~100 hospital EDs | Free (online query at cpsc.gov) | HIGH |
| **NFIRS (USFA/FEMA)** | Fire dept. incident reports | Voluntary, national | Free (PDR download) | MODERATE |

**Agent LOA7-A: BARD Analysis**
```
Filter BARD Deaths CSVs for:
1. CauseofDeath = "Electrocution" or similar values
2. Cross-reference results against ESDPA incident list by date ± 2 years, state, victim age
3. Flag any BARD electrocution deaths NOT in ESDPA list as new incidents
4. For each new incident, search for news coverage using victim details from BARD

Data location: /opt/repos/esd-research/BARD-dataset-2009-2023-csv/
- bard-2009-2013-ReleasableDeaths.csv
- bard-2014-2022-ReleasableDeaths.csv
- bard-2023-2023-ReleasableDeaths.csv

Output: /opt/repos/esd-research/phase2-findings/LOA7-structured-databases/
```

**Agent LOA7-B: NEISS Query**
```
Query NEISS at https://www.cpsc.gov/cgibin/NEISSQuery/UserCriteria.aspx for:
1. Electrocution diagnosis + water/pool/dock product codes
2. Extract narrative fields for ESD-pattern language ("dock", "marina", "shock in water", "tingling")
3. Cross-reference against ESDPA list

Output: /opt/repos/esd-research/phase2-findings/LOA7-structured-databases/
```

### LOA8: AI-Powered Obituary and Memorial Mining

**Rationale:** A 2025 JMIR study demonstrated 96.5% accuracy mining obituaries for cause-of-death using LLMs. Phase 1.5 confirmed that obituaries are a key source — once a victim name is known, Legacy.com and funeral home sites consistently provide corroborating details.

**Approach:**
- Search Legacy.com, EverLoved, TributeArchive for obituaries mentioning drowning + dock/marina/electrocution
- Search GoFundMe for ESD survivor/victim campaigns (precedent: Eric Hancock, 2012 boat lift electrocution)
- Use LLM classification to flag obituaries with ESD-pattern language

**Key reference:** Automated Extraction of Mortality Information From Publicly Available Sources Using Large Language Models (JMIR 2025, https://www.jmir.org/2025/1/e71113/)

### LOA9: State Child Fatality Review Team Data

**Rationale:** Every U.S. state has a CFRT that conducts detailed reviews of child deaths, including circumstances that go beyond death certificates. Child drownings near docks are a recognized high-suspicion pattern for ESD.

**Action:** File FOIA requests to CFRTs in top 10 boating states (TN, AR, MI, FL, TX, MN, WI, VA, NC, SC) requesting drowning death reviews involving docks, marinas, or boat facilities.

### LOA10: GIS Proximity Analysis

**Rationale:** Validated in peer-reviewed research (Australian drowning hotspot analysis, UK DBSCAN clustering). Overlay drowning death coordinates with marina/dock locations to identify statistical anomalies that suggest ESD.

**Approach:**
1. Obtain drowning death coordinates from CDC WONDER (W65–W74 codes)
2. Obtain marina/dock locations from USACE, state permits, NOAA charts
3. Flag all drowning deaths within 500m of registered marina/dock facilities
4. Identify locations with statistically elevated drowning rates

### LOA11: Video News Archive Mining (YouTube)

**Rationale:** Many local TV news stories are on YouTube but not in text archives. YouTube's auto-generated transcripts make them searchable. Multiple ESD incidents were found during Phase 1.5 with video coverage but limited text web presence.

**Approach:** Systematic YouTube search for "electrocuted dock," "electric shock drowning," "marina electrocution," "drowned dock" by date range and region.

### LOA12: Insurance and Liability Claims Data

**Rationale:** The NFPA Fire Protection Research Foundation's Marina Risk Reduction report explicitly identified the data gap for ESD-related claims. Marina liability insurers track electrocution claims that may never make news.

### LOA13: Internet Archive / Wayback Machine Recovery

**Rationale:** Local newspaper websites frequently delete older articles. The Wayback Machine CDX API allows programmatic searching for archived versions. Particularly valuable for 1990s-2000s gap years.

### LOA14: Medical Examiner Protocol Gap Analysis

**Rationale:** NASBLA has an ESD investigation checklist, but adoption is not universal. A survey of ME/coroner offices to determine whether they routinely test for electrical current in dock/marina drownings would quantify the diagnostic gap. This is an original research contribution suitable for PhD dissertation work.

---

### Additional Critical Data Sources (Not in Original LOA1–LOA6)

| Source | Type | Access | Cost | ESD Relevance |
|--------|------|--------|------|---------------|
| **BARD (USCG)** | Structured DB | **Already downloaded** | Free | **Very High** — direct cause-of-death filtering |
| **NEMSIS** | Structured DB | Research request | Free | High — EMS response data with ICD-10 codes |
| **NEISS (CPSC)** | Structured DB | Online query | Free | High — ER visits with narrative fields |
| **NFIRS (USFA/FEMA)** | Structured DB | Public download | Free | Moderate — fire dept. electrocution incidents |
| **CDC National Death Index** | Research DB | IRB + application | Fee-based | **Very High** — definitive national mortality data |
| **State CFRT Reports** | Reports/data | FOIA or published | Free–Low | High — detailed child drowning circumstances |
| **GoFundMe** | Unstructured text | Web search | Free | Moderate — survivor/victim campaign narratives |
| **YouTube (Local TV)** | Video/transcript | API search | Free | Moderate — visual coverage not in text archives |
| **Internet Archive** | Archived web | CDX API | Free | Moderate — recovery of deleted news articles |

### Updated Execution Plan (with LOA7–LOA14)

**Phase 2A (Run first — highest ROI):**
1. **LOA7-A: BARD Analysis** — IMMEDIATE. Data already downloaded. Filter Deaths CSVs for electrocution. Could produce results in minutes.
2. LOA1 agents A through E (news archive search) — run in batches of 6
3. LOA5-A (medical/forensic literature) — run in parallel with LOA1

**Phase 2B (Run second):**
4. LOA3-A and LOA3-B (court records and law firm search)
5. LOA4-A and LOA4-B (OSHA/CPSC and CDC/USCG)
6. LOA5-B and LOA5-C (engineering literature and epi data)
7. LOA7-B: NEISS Query

**Phase 2C (Run third — lead generation):**
8. LOA2-A, LOA2-B, LOA2-C (misclassified drownings)
9. LOA6-A, LOA6-B, LOA6-C (community/forum sources)
10. LOA11: YouTube video archive mining
11. LOA4-C (state agency records)

**Phase 2D (Medium-term — requires more setup):**
12. LOA8: Obituary mining (systematic Legacy.com/GoFundMe search)
13. LOA13: Wayback Machine recovery of deleted articles
14. LOA9: CFRT FOIA requests

**Phase 2E (PhD-track — long-term):**
15. LOA10: GIS proximity analysis
16. LOA14: ME/coroner protocol survey
17. CDC NDI study (capture-recapture prevalence model)

---

## Directory Structure

```
/opt/repos/esd-research/
├── phase2-plan.md                          (this document)
├── perplexity-additional-data-sources-and-lines-of-attack.md  (Perplexity analysis)
├── Perplexity-ESD-research-sources.md      (Perplexity reference links)
├── BARD-dataset-2009-2023-csv/             (USCG BARD data — already downloaded)
├── mcp-search-tracker.md                   (Phase 1.5 MCP search results)
├── phase2-findings/
│   ├── LOA1-news-archive/
│   │   ├── LOA1-A-summary.md
│   │   ├── LOA1-B-summary.md
│   │   ├── LOA1-C-summary.md
│   │   ├── LOA1-D-summary.md
│   │   ├── LOA1-E-summary.md
│   │   └── NEW-YYYY-NNN.md               (new incident files)
│   ├── LOA2-misclassified-drownings/
│   │   ├── LOA2-A-summary.md
│   │   ├── LOA2-B-summary.md
│   │   ├── LOA2-C-summary.md
│   │   └── SUSP-YYYY-NNN.md              (suspected ESD files)
│   ├── LOA3-legal-records/
│   │   ├── LOA3-A-summary.md
│   │   ├── LOA3-B-summary.md
│   │   ├── LOA3-C-summary.md
│   │   └── LEGAL-YYYY-NNN.md             (legal record findings)
│   ├── LOA4-government-records/
│   │   ├── LOA4-A-summary.md
│   │   ├── LOA4-B-summary.md
│   │   ├── LOA4-C-summary.md
│   │   └── GOV-YYYY-NNN.md               (government record findings)
│   ├── LOA5-academic/
│   │   ├── LOA5-A-summary.md
│   │   ├── LOA5-B-summary.md
│   │   ├── LOA5-C-summary.md
│   │   └── ACAD-NNN.md                   (academic paper summaries)
│   ├── LOA6-community/
│   │   ├── LOA6-A-summary.md
│   │   ├── LOA6-B-summary.md
│   │   ├── LOA6-C-summary.md
│       └── LEAD-NNN.md                   (community lead files)
│   ├── LOA7-structured-databases/
│   │   ├── LOA7-A-bard-summary.md
│   │   ├── LOA7-B-neiss-summary.md
│   │   └── BARD-YYYY-NNN.md              (BARD-sourced incident files)
│   ├── LOA8-obituary-mining/
│   │   └── OBIT-NNN.md
│   ├── LOA11-youtube/
│   │   └── VID-YYYY-NNN.md
│   └── LOA13-wayback/
│       └── WB-YYYY-NNN.md
├── incidents-new/                          (verified new incidents, final)
│   └── NEW-YYYY-NNN.md                   (promoted from phase2-findings/)
```

---

## Success Criteria

Phase 2 will be considered successful if it:

1. **Finds 30+ new verified ESD incidents** not in the ESDPA list (2+ independent sources each)
2. **Identifies 50+ suspected ESD cases** warranting further investigation
3. **Locates at least 3 peer-reviewed academic papers** discussing ESD prevalence or forensic markers
4. **Establishes a credible estimate** for the "dark figure" of misclassified ESD drownings
5. **Fills at least 3 of the 6 gap years** (1990, 1992, 1996, 2004, 2007, 2009) with new incidents
6. **Finds incidents in at least 5 underrepresented states** (TX, MN, WI, WA, NY, NC, SC, AZ, MD, etc.)
7. **Completes BARD database analysis** — filters all 8,935 USCG boating deaths (2009–2023) for electrocution and cross-references against ESDPA list (NEW — from LOA7)
8. **Identifies NEMSIS/NEISS data pathways** for ongoing ESD surveillance (NEW — from LOA7)

---

**Document Version:** 1.1
**Created:** March 6, 2026
**Updated:** March 6, 2026 — Added Phase 1.5 MCP campaign results, updated search platform table with Perplexity/Brave as primary tools, updated agent instructions with source exclusion list and search strategy lessons, updated execution plan with practical parallelism constraints.
**Author:** Phase 2 research planning agent
**Based on:** Phase 1 research of 175 ESDPA incidents, Phase 1.5 MCP search campaign (58 incidents re-searched, 25 new sources found), search-strategy.md, esd-search-terms.md, ISSUES.md, research-summary.md, mcp-search-tracker.md
