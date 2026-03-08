# esd-research

Independent research into Electric Shock Drowning (ESD) incidents in the United States.

## What Is Electric Shock Drowning?

Electric Shock Drowning occurs when AC electrical current leaks into water near docks, marinas, boats, or pools. A swimmer entering the energized water experiences involuntary muscle paralysis, loses the ability to swim, and drowns. ESD is frequently misclassified as ordinary drowning because the electrical component leaves little physical evidence at autopsy.

## Source Data

The starting point for this research is the **"Electric Shock Drowning Incidents -- Marinas"** list compiled by James D. Shafer and Capt. David E. Rifkin of Quality Marine Services, LLC (Rev. 8/15/2025), obtained from the [ESDPA (Electric Shock Drowning Prevention Association)](https://electricshockdrowning.org/) website. This list provided the foundation of **175 incidents** spanning 1981-2025, including 115 fatal incidents and 60 near misses.

The ESDPA list is the most comprehensive catalog of ESD incidents available. This project uses it as a starting point, not as a verification source.

## Purpose

This project **independently verifies, corrects, and expands** on the ESDPA list using primary sources only:

- News archives (local and national)
- Obituaries and memorial records
- Court records and legal filings
- OSHA and NTSB reports
- CDC MMWR publications and NCHS mortality data
- USCG Boating Accident Report Database (BARD)
- Trade journal articles (EC&M, Soundings, etc.)
- Government and legislative records
- YouTube local TV news archives

The ESDPA list and its derivatives (mikeholt.com reposts, etc.) are explicitly **excluded** as verification sources to avoid circular sourcing.

## Research Phases

### Phase 1: ESDPA List Extraction and Verification (Complete)

Extracted all 175 incidents from the ESDPA PDF into structured files, then independently researched each one.

| Metric | Result |
|--------|--------|
| Independently verified (full or partial) | 106 of 175 (61%) |
| No independent sources found | 69 of 175 (39%) |
| Date corrections needed (among verified) | ~80% |
| Date errors > 6 months | 15 incidents |
| Location errors found | 8 incidents |
| Phantom duplicate entry | 1 (FI-2022-001 duplicates FI-2023-001) |
| Near miss that was actually a double fatality | 1 (NM-2016-001) |

**Results:** [`incident-research/`](incident-research/) (175 files), [`research-summary.md`](research-summary.md), [`ISSUES.md`](ISSUES.md)

### Phase 1.5: MCP Search Campaign (Complete)

Re-searched 58 incidents using Perplexity AI and Brave Web Search, achieving a 43% hit rate — finding new sources for 25 incidents the initial pass missed.

**Results:** [`mcp-search-tracker.md`](mcp-search-tracker.md)

### Phase 2: Unlisted Incident Search (Complete)

Used 14 Lines of Attack (LOA1–LOA14) to systematically find ESD incidents not in the ESDPA list.

| LOA | Description | Status | Key Result |
|-----|-------------|--------|------------|
| LOA1 | News archive search | Complete | 13 verified new incidents |
| LOA2 | Misclassified drownings | Complete | 25 SUSP files; 6 high-probability |
| LOA3 | Legal record mining | Complete | 20 LEGAL files; settlement/verdict data |
| LOA4 | Government records (OSHA, CPSC, CDC) | Complete | 5 new incidents |
| LOA5 | Academic/epidemiological literature | Complete | No new incidents; critical methodology findings |
| LOA6 | Community/forum sources | Complete | 52 LEAD files; 10-15 new incidents |
| LOA7-A | BARD structured database | Complete | 8% ESD capture rate; 3 new incidents |
| LOA7-B | NEISS structured database | Abandoned | Structural zero — NEISS cannot capture ESD |
| LOA7-C | NCHS mortality cross-tabulation | Complete | 42 statistical ESD candidates (2003-2023) |
| LOA8 | Obituary/memorial mining | Complete | 4 victim IDs confirmed; Legacy.com tool ceiling found |
| LOA11 | YouTube video archive mining | Complete | 17 probable new incidents; 55+ YouTube URLs |
| LOA13 | Wayback Machine recovery | Complete | CDX structural gap confirmed; pre-2005 papers not crawled |
| LOA9 | CFRT FOIA requests | Not started | Requires external filing |
| LOA10-14 | GIS, insurance, ME survey, NDI | Not started | Advanced methodology track |

**Results:** [`phase2-findings/`](phase2-findings/) subdirectories, [`phase2-findings/PHASE2-META-ANALYSIS.md`](phase2-findings/PHASE2-META-ANALYSIS.md)

### Phase 3: Consolidated Dataset (Complete)

Merged all ESDPA entries and Phase 2 findings into a single unified dataset with structured YAML frontmatter.

| Metric | Count |
|--------|-------|
| Total incident files | 193 |
| From ESDPA base list | 171 |
| Net-new from Phase 2 | 22 |
| Fatal incidents | ~130 |
| Near-miss incidents | ~63 |
| VERIFIED (multiple independent sources) | ~70 |
| CONFIRMED (one independent source) | ~30 |
| UNVERIFIED (ESDPA-only, no independent sources) | ~75 |
| SUSPECTED (Phase 2 leads, not in ESDPA) | ~18 |
| ESDPA date corrections applied | 25+ |
| ESDPA location corrections applied | 4+ |

**Results:** [`esd-dataset/`](esd-dataset/), [`esd-dataset/SCHEMA.md`](esd-dataset/SCHEMA.md)

## Key Findings

| Finding | Detail |
|---------|--------|
| New incidents found (beyond ESDPA) | ~55-70 verified + suspected |
| Statistical ESD candidates in NCHS data | 42 (2003-2023) |
| BARD capture rate for known ESD | ~8% |
| Deadliest single US ESD site | Lake of the Ozarks, MO (6 deaths, 5 incidents) |
| Highest dock stray voltage prevalence | Smith Mountain Lake, VA (97% of 209 docks, 2017) |
| Strongest US ESD regulation | Tennessee (Noah Dean and Nate Act) |
| Estimated true annual ESD deaths | 20-30 (vs. 4-6 documented) |

## Repository Structure

### Primary Outputs

| Path | Description |
|------|-------------|
| `esd-dataset/` | **Consolidated dataset** — 193 incident files in unified YAML+markdown schema, with CSV/XLSX exports. |
| `phase2-findings/` | Results of the unlisted-incident search, organized by LOA. |

### Source Data and Verification

| Path | Description |
|------|-------------|
| `source-data/` | 175 structured files extracted from the ESDPA PDF, plus extraction methodology. |
| `verification/` | 175 independently researched files with verification status, corrections, and sources. |

### Root Documents

| File | Description |
|------|-------------|
| [`research-summary.md`](research-summary.md) | Phase 1 verification results — statistics, date errors, notable corrections. |
| [`phase2-plan.md`](phase2-plan.md) | Research plan for all LOA tracks with execution status. |
| [`DATA-GOVERNANCE.md`](DATA-GOVERNANCE.md) | Data sources, privacy considerations, and governance policies. |
| [`phase2-findings/PHASE2-META-ANALYSIS.md`](phase2-findings/PHASE2-META-ANALYSIS.md) | Cross-LOA analysis, underreporting model, priority next actions. |
| [`esd-dataset/SCHEMA.md`](esd-dataset/SCHEMA.md) | Dataset schema / data dictionary. |

### Reference Materials

| Path | Description |
|------|-------------|
| `reference/search-strategy.md` | ESD incident patterns, geographic gaps, and search methodology. |
| `reference/esd-search-terms.md` | Practical search queries for finding ESD incidents. |
| `reference/source-count-by-incident.md` | All 175 ESDPA incidents ranked by independent source count. |
| `reference/mcp-search-tracker.md` | Phase 1.5 MCP re-search results. |
| `reference/additional-data-sources-and-lines-of-attack.md` | LOA7–LOA15 data source analysis. |
| `reference/additional-research-sources.md` | Extended data source report with citations. |
| `reference/BARD-dataset-2009-2023-csv/` | USCG Boating Accident Report Database (public domain). |

### Phase 2 Findings Subdirectories

| Path | LOA | Files | Key Finding |
|------|-----|-------|-------------|
| `LOA1-news-archive/` | LOA1 | 21 NEW + 5 summaries | 13 new verified incidents |
| `LOA2-misclassified-drownings/` | LOA2 | 25 SUSP + 3 summaries | 6 high-probability ESD misclassifications |
| `LOA3-legal-records/` | LOA3 | 20 LEGAL + 4 summaries | Settlements, verdicts, regulatory gaps |
| `LOA4-government-records/` | LOA4 | 12 GOV + 4 summaries | OSHA, CPSC, CDC, USCG findings |
| `LOA5-academic/` | LOA5 | 34 ACAD + 3 summaries | No peer-reviewed ESD epidemiology exists |
| `LOA6-community/` | LOA6 | 52 LEAD + 3 summaries | Hotspot deep dives (LOTOZ, SML) |
| `LOA7-structured-databases/` | LOA7-A/B | Analysis files | BARD 8% capture; NEISS structural zero |
| `LOA7C-nchs-mortality/` | LOA7-C | 3 files | 42 ESD candidates in 61M death records |
| `LOA8-obituary-mining/` | LOA8 | 21 research files | 4 victim IDs confirmed; LOTOZ/SML deep dives |
| `LOA11-youtube/` | LOA11 | 35 VID + 3 summaries | 17 new incidents; 55+ YouTube URLs |
| `LOA13-wayback/` | LOA13 | 2 files | Pre-2005 local papers not in Wayback Machine |
| `PHASE2-META-ANALYSIS.md` | All | 1 file | Cross-LOA synthesis and underreporting model |

## Methodology

### Phase 1: Extraction
The ESDPA PDF was processed into 175 structured markdown files in `source-data/`, one per real-world incident. Classification rules and naming conventions are documented in [`source-data/methodology/CLAUDE-PROMPT.md`](source-data/methodology/CLAUDE-PROMPT.md).

### Phase 1 & 1.5: Independent Verification
Each of the 175 incidents was independently researched using AI-assisted search (Claude Sonnet, Perplexity AI, Brave Web Search). For each incident, the researcher searched for independent primary sources, compared findings against the ESDPA entry, and documented corrections and verification status. The ESDPA list itself and sources deriving from it were excluded as verification.

### Phase 2: Unlisted Incident Search
Using patterns identified during Phase 1 (geographic gaps, temporal gaps, common misclassification as drowning), 14 Lines of Attack searched for ESD incidents not in the ESDPA list. The full plan is in [`phase2-plan.md`](phase2-plan.md). LOA1 through LOA8, LOA11, and LOA13 are complete. Remaining tracks (LOA9, LOA10, LOA12, LOA14) require institutional access or external filing.

### Phase 3: Dataset Consolidation
All ESDPA entries and Phase 2 findings were merged into the unified [`esd-dataset/`](esd-dataset/) with YAML frontmatter designed for programmatic parsing and Excel export. The schema supports both incident-level and victim-level analysis. See [`esd-dataset/SCHEMA.md`](esd-dataset/SCHEMA.md).

## Remaining Research Tracks

| Track | Description | Requirement |
|-------|-------------|-------------|
| LOA9 | State Child Fatality Review Team records | FOIA filing |
| LOA10 | GIS proximity analysis (drowning deaths near marina coordinates) | GIS tooling |
| LOA12 | Marina insurance/liability claims data | Industry contacts |
| LOA14 | Medical examiner protocol gap survey | Institutional affiliation |
| CDC NDI | National Death Index W86+drowning cross-reference | IRB approval + institutional affiliation |
| NewspaperArchive | Pre-internet local newspaper keyword search (1980-2005) | API access agreement |

## Limitations

- **Pre-internet era:** Incidents from the 1980s and early 1990s are largely unverifiable because local newspaper archives are not digitized.
- **Near misses:** Non-fatal incidents where everyone survived rarely generate lasting documentation, resulting in a 43% verification rate for NM incidents vs. 70% for fatal incidents.
- **Paywalled sources:** Some potentially relevant articles could not be accessed.
- **Verification is not causation:** Confirming that an incident occurred does not confirm that ESD was the mechanism.
- **Completeness unknown:** The true number of ESD incidents in the US is likely substantially higher than the 193 documented here.

## License

CC0 1.0 Universal. See [LICENSE](LICENSE).
