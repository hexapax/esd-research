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

## What's in This Repository

| Path | Description |
|------|-------------|
| `incidents-raw/` | 175 structured markdown files extracted from the ESDPA PDF. One file per incident. These represent the original ESDPA data. |
| `incident-research/` | 175 independently researched files, one per incident. Each contains verification status, corrections found, independent sources, and additional details discovered. |
| `research-summary.md` | Comprehensive analysis of all 175 incidents with statistics, notable cases, and pattern analysis. |
| `ISSUES.md` | Data quality issues found during extraction and research: date errors, misclassifications, duplicates, location errors. |
| `search-strategy.md` | Detailed guide to ESD incident patterns, geographic gaps in the ESDPA list, and search terms for finding unlisted incidents. |
| `esd-search-terms.md` | Practical search strategies for finding ESD incidents and independent sources. |
| `CLAUDE-PROMPT.md` | Documents the extraction methodology used to create `incidents-raw/`. |

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

### Phase 3: Searching for Unlisted Incidents (next)

Using patterns identified during Phase 2 (geographic gaps, temporal gaps, common misclassification as drowning), search for ESD incidents that do not appear in the ESDPA list at all. The `search-strategy.md` document identifies specific states, years, and lake systems that are likely underrepresented.

## Limitations

- **Pre-internet era:** Incidents from the 1980s and early 1990s are largely unverifiable because local newspaper archives are not digitized.
- **Near misses:** Non-fatal incidents where everyone survived rarely generate lasting documentation, resulting in a 43% verification rate for NM incidents vs. 70% for fatal incidents.
- **Paywalled sources:** Some potentially relevant articles could not be accessed.
- **Verification is not causation:** Confirming that an incident occurred does not confirm that ESD was the mechanism. Some verified incidents may have been ordinary drownings, direct electrocution, or other causes.
- **Completeness unknown:** The true number of ESD incidents in the US is likely higher than 175. The search strategy document identifies significant geographic gaps (Texas, Pacific Northwest, Northeast) where incidents are likely underreported.

## License

CC0 1.0 Universal. See [LICENSE](LICENSE).
