# esd-research

Independent research into Electric Shock Drowning (ESD) incidents in the United States.

## What Is Electric Shock Drowning?

Electric Shock Drowning occurs when AC electrical current leaks into water near docks, marinas, boats, or pools. A swimmer entering the energized water experiences involuntary muscle paralysis, loses the ability to swim, and drowns. ESD is frequently misclassified as ordinary drowning because the electrical component leaves little physical evidence.

## Source Data

The starting point for this research is the **"Electric Shock Drowning Incidents -- Marinas"** list compiled by James D. Shafer and Capt. David E. Rifkin of Quality Marine Services, LLC (Rev. 8/15/2025), obtained from the [ESDPA (Electric Shock Drowning Prevention Association)](https://electricshockdrowning.org/) website. This list provided the foundation of **175 incidents** spanning 1981-2025, including 115 fatal incidents and 60 near misses.

The ESDPA list is the most comprehensive catalog of ESD incidents available. This project uses it as a starting point, not as a verification source.

## Purpose

This project **independently verifies, corrects, and expands** on the ESDPA list using primary sources only:

- News archives (local and national)
- Obituaries
- Court records and legal filings
- OSHA and NTSB reports
- CDC MMWR (Morbidity and Mortality Weekly Report) publications
- Trade journal articles (EC&M, Soundings, etc.)
- Government and legislative records

The ESDPA list and its derivatives (mikeholt.com reposts, etc.) are explicitly **excluded** as verification sources to avoid circular sourcing.

## Key Findings

### Phase 1 & 2: ESDPA List Verification

After researching all 175 incidents:

| Metric | Result |
|--------|--------|
| Independently verified (full or partial) | 106 of 175 (61%) |
| No independent sources found | 69 of 175 (39%) |
| Date corrections needed (among verified) | ~80% |
| Date errors > 6 months | 15 incidents |
| Location errors found | 8 incidents |
| Phantom duplicate entry | 1 (FI-2022-001 duplicates FI-2023-001) |
| Near miss that was actually a double fatality | 1 (NM-2016-001) |
| Two incidents merged into one entry | 1 (FI-2017-010) |

The most common data quality issue is **incorrect dates**, with errors ranging from one day to nearly two years. Among the 15 incidents with date errors exceeding 6 months, 11 were placed in the wrong calendar year. See [ISSUES.md](ISSUES.md) and [research-summary.md](research-summary.md) for full details.

## Phase 3 Key Findings (Unlisted Incident Search)

Phase 3 used 8 Lines of Attack (LOA1–LOA7, with LOA7 having three sub-tracks A/B/C) to systematically find ESD incidents not in the ESDPA list. Highlights:

| Finding | Detail |
|---------|--------|
| New verified incidents found | ~40–50 |
| Unverified leads (SUSP files) | ~60 |
| NCHS death certificates with ESD signature codes (2003–2023) | **42 statistical ESD candidates** |
| BARD capture rate for known ESD | ~8% (2 of 24 dock/marina ESD incidents) |
| Lake of the Ozarks | Confirmed single deadliest US ESD site (5–6 deaths) |
| Smith Mountain Lake VA | 97% of tested docks had stray voltage (2017 survey) |
| Tennessee | Strongest ESD regulation in any US state (Noah Dean and Nate Act) |
| Missouri | Recreational Use Act shields all private dock owners — zero successful ESD lawsuits despite 5–6 deaths |

See [`phase2-findings/PHASE2-META-ANALYSIS.md`](phase2-findings/PHASE2-META-ANALYSIS.md) for the complete cross-LOA analysis.

## What's in This Repository

| Path | Description |
|------|-------------|
| `incidents-raw/` | 175 structured markdown files extracted from the ESDPA PDF. One file per incident. These represent the original ESDPA data. |
| `incident-research/` | 175 independently researched files, one per incident. Each contains verification status, corrections found, independent sources, and additional details discovered. |
| `phase2-findings/` | Results of the Phase 3 unlisted-incident search. Subdirectories for each LOA plus the cross-LOA meta-analysis. |
| `NCHS-mortality/` | 24 years of NCHS Multiple Cause of Death zip files (2000–2023, ~2.4 GB). Excluded from git via `.gitignore`. |
| `NEISS-dataset/` | NEISS 2023 ER visit data (41 MB xlsx). Excluded from git via `.gitignore`. |
| `research-summary.md` | Comprehensive analysis of all 175 ESDPA incidents with statistics, notable cases, and pattern analysis. |
| `ISSUES.md` | Data quality issues found during extraction and research: date errors, misclassifications, duplicates, location errors. |
| `phase2-plan.md` | Detailed plan for all LOA search tracks, including those not yet executed (LOA8–LOA14). |
| `search-strategy.md` | Detailed guide to ESD incident patterns, geographic gaps, and search terms. |
| `esd-search-terms.md` | Practical search strategies for finding ESD incidents and independent sources. |
| `CLAUDE-PROMPT.md` | Documents the extraction methodology used to create `incidents-raw/`. |

### Phase 2 Findings Subdirectories

| Path | LOA | Description |
|------|-----|-------------|
| `phase2-findings/LOA1-news-archive/` | LOA1 | 25 incident files from direct news archive search; 1 new verified incident |
| `phase2-findings/LOA2-misclassified-drownings/` | LOA2 | 25 SUSP files; 6 high-probability ESD misclassifications |
| `phase2-findings/LOA3-legal-records/` | LOA3 | 20 LEGAL files; settlements, verdicts, structural legal findings |
| `phase2-findings/LOA4-government-records/` | LOA4 | 8 GOV files; OSHA, CPSC, CDC, USCG sources |
| `phase2-findings/LOA5-academic/` | LOA5 | 34 ACAD files; peer-reviewed literature and epidemiology |
| `phase2-findings/LOA6-community/` | LOA6 | 52 LEAD files; Reddit, boating forums, hotspot deep dives |
| `phase2-findings/LOA7-structured-databases/` | LOA7-A/B | BARD (8% capture rate confirmed); NEISS (abandoned — structural) |
| `phase2-findings/LOA7C-nchs-mortality/` | LOA7-C | NCHS MCod 21-year cross-tab: 42 ESD candidates, 11 high-confidence |
| `phase2-findings/PHASE2-META-ANALYSIS.md` | All | Cross-LOA summary, underreporting analysis, priority next actions |

## Methodology

### Phase 1: Extraction (completed)

The ESDPA PDF was processed into 175 structured markdown files in `incidents-raw/`, one per real-world incident. Classification rules, naming conventions, and handling of ambiguous cases are documented in `CLAUDE-PROMPT.md`.

### Phase 2: Independent Research (completed)

Each of the 175 incidents was independently researched using AI-assisted batch processing (Claude Sonnet). For each incident, the researcher:

1. Searched for the incident using victim names, locations, dates, and circumstances
2. Located and evaluated independent primary sources
3. Compared independent findings against the ESDPA entry
4. Documented corrections, additional details, and verification status

**Source exclusions:** The ESDPA list itself and sources that derive from it (mikeholt.com forum reposts of ESDPA data, websites that reproduce the ESDPA list) were not counted as independent verification.

### Phase 3: Searching for Unlisted Incidents (in progress)

Using patterns identified during Phase 2 (geographic gaps, temporal gaps, common misclassification as drowning), 8 Lines of Attack searched for ESD incidents not in the ESDPA list. The full plan is in `phase2-plan.md`; LOA1–LOA7-C are complete. LOA8 (obituary mining), LOA11 (YouTube), LOA13 (Wayback Machine), and additional tracks remain to be executed.

## Limitations

- **Pre-internet era:** Incidents from the 1980s and early 1990s are largely unverifiable because local newspaper archives are not digitized.
- **Near misses:** Non-fatal incidents where everyone survived rarely generate lasting documentation, resulting in a 43% verification rate for NM incidents vs. 70% for fatal incidents.
- **Paywalled sources:** Some potentially relevant articles could not be accessed.
- **Verification is not causation:** Confirming that an incident occurred does not confirm that ESD was the mechanism. Some verified incidents may have been ordinary drownings, direct electrocution, or other causes.
- **Completeness unknown:** The true number of ESD incidents in the US is likely higher than 175. The search strategy document identifies significant geographic gaps (Texas, Pacific Northwest, Northeast) where incidents are likely underreported.

## License

CC0 1.0 Universal. See [LICENSE](LICENSE).
