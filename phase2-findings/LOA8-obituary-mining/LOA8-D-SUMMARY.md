# LOA8-D: Systematic Obituary and Memorial Mining — Summary

**Research Date:** March 8, 2026
**Researcher:** Claude Sonnet 4.6 (AI agent with MCP tools)
**Tools Used:** Brave Web Search (primary), grep deduplication checks against 175+ project incident files
**Output Directory:** `phase2-findings/LOA8-obituary-mining/`
**Output Files Created:** `LOA8-OBT-2023-001.md` (Nate Davenport, Jupiter FL fountain), this summary

---

## Executive Summary

LOA8-D executed the systematic obituary and memorial keyword mining campaign that was explicitly flagged as incomplete in the prior LOA8 summary (March 7–8, 2026). The mission was to search Legacy.com, EverLoved, TributeArchive, Find a Grave, GoFundMe, and general news/obituary sources for ESD/in-water electrocution victims NOT already in the project's 175+ incident files.

**Total distinct searches run: 25+**
**New named victims identified: 1**
**New victim file created: 1 (LOA8-OBT-2023-001.md)**
**Known victims re-encountered but confirmed as already documented: 15+**
**Null-result searches (confirmed no new victims): 10+**

---

## The One New Victim: Nate Davenport

**Nathaniel "Nate" Davenport**, 45, Jupiter, Florida native, Navy veteran, father of four — died **October 22, 2023** at Jupiter Medical Center after jumping into an electrified decorative fountain at the **Harbourside Place** shopping center to save his children and a friend's children who were being electrically shocked in the fountain's pool.

- Cause: Broken light fixtures inside fountain leaking electrical voltage into water (confirmed by Town of Jupiter Building Department)
- Classification: In-water electrocution (direct fatal electrocution, not ESD paralysis-then-drowning; head was not submerged)
- Mechanism falls within ESDPA's stated scope of "in-water electrocution fatalities included"
- National coverage: Palm Beach Post (primary), CBS12/WPEC, WPBF, WPTV, People.com, The Independent, Fox affiliates
- Wrongful death lawsuit by widow Amy Davenport settled with Harbourside Place in March 2024 (confidential terms)
- Second rescuer Syler Sparks (age 20) was also shocked and filed a separate lawsuit
- Florida law at time of incident did not require regular inspection of public decorative fountains
- Prior warning evidence: Woman (Dina Fleck) reported feeling a shock in the same fountain in July 2023, ~15 weeks before Davenport's death

**Deduplication confirmed:** `grep -rl "Davenport|Jupiter.*2023|fountain.*elec|2023.*fountain|Harbourside"` returned zero results from `/opt/repos/esd-research/incident-research/`.

**Full documentation:** See `LOA8-OBT-2023-001.md`

---

## All Searches Conducted

### Category 1: EverLoved / TributeArchive Searches

| Search # | Query | Result |
|----------|-------|--------|
| 1 | `EverLoved obituary "electric shock drowning" dock lake memorial` | No EverLoved-specific hits; returned general ESD news results. Null for new victims. |
| 2 | `EverLoved.com obituary "electric shock" OR "dock" OR "marina" drowning lake memorial` | EverLoved returned only a venue listing (Hideaway Lake Marina TX). No obituary hits. Null. |
| 3 | `tributearchive.com obituary "electric shock" OR "electrocuted" "lake" OR "dock" OR "marina" drowned` | TributeArchive returned only site navigation pages; no keyword-obituary matching accessible via search engine. Null. |
| 4 | `tributearchive.com OR "tribute archive" obituary drowned dock lake electric shock memorial 2019 2020 2022` | No obituary content accessible. Null. |

**Assessment:** Legacy.com, EverLoved, and TributeArchive do not expose full obituary text to web search engines in a way that allows meaningful keyword mining for ESD-related language. These databases require direct on-site search. Systematic keyword mining of these databases was not possible through external search tools.

### Category 2: Find a Grave / GoFundMe Searches

| Search # | Query | Result |
|----------|-------|--------|
| 5 | `FindAGrave memorial "electric shock drowning" OR "electrocuted lake" OR "drowned dock" victim 2019 2020 2021` | No Find a Grave obituary hits returned. General ESD news articles only. Null. |
| 6 | `gofundme "electric shock drowning" OR "drowned dock" OR "electrocuted lake" memorial fund victim 2019 2020 2021` | GoFundMe results not returned via Brave search. Returned general ESD awareness articles. Null for new victims. |
| 7 | `obituary memorial fund "electric shock" drowned dock lake 2024 2025 GoFundMe victim death` | ESDPA press releases page. No new victims found. |

**Assessment:** GoFundMe and Find a Grave ESD content is not surfaced by standard web search in a way that enables systematic mining. These platforms require direct on-site searches which were not possible through the available MCP tools.

### Category 3: General Keyword Searches — ESD Victims by Year

| Search # | Query | Key Findings |
|----------|-------|--------------|
| 8 | `"electric shock drowning" death 2018 lake dock victim family memorial` | Returned known victims (Carmen Johnson, Lake Tuscaloosa, Thomas Milner). No new 2018 victims identified. |
| 9 | `"electric shock drowning" 2018 lake marina dock death fatal victim name news` | No new 2018 victims found. Null. |
| 10 | `electrocuted drowned dock marina lake 2018 death investigation "electric current" OR "stray voltage" name obituary` | No results returned. Null. |
| 11 | `"electric shock drowning" death 2019 lake dock victim obituary name age Tennessee Georgia Alabama` | Returned known victims only. No new 2019 victims. |
| 12 | `"electric shock drowning" OR "electrocuted lake" OR "drowned marina" death 2020 NOT "Lake Pleasant" NOT "Miller" victim name` | No new 2020 victims found beyond Miller brothers (already in FI-2019-001). Null. |
| 13 | `"electric shock" OR electrocuted drowned lake dock 2022 death victim name age investigation` | Returned known cases (Kayla Matos 2017, Jesse Hamric 2024, Keith Elkins 2022 LEAD-007). No new victims. |

### Category 4: Targeted Named Victim Searches

| Search # | Query | Result |
|----------|-------|--------|
| 14 | `Carmen Johnson "Smith Lake" electric shock drowning Alabama death year` | Carmen Johnson (Apr 16, 2016, Smith Lake AL) — **already in FI-2016-007**. Not new. |
| 15 | `Newark girl electrocuted Toms River lagoon electric shock drowning New Jersey 11 year old death` | Kayla Matos, 11, Toms River NJ, June 17, 2017 — **already in FI-2017-007**. Not new. |
| 16 | `"Clyde Lake" electrocution electric shock drowning death 2021 high school graduate` | Trevor Cate, 18, Clyde Lake TX, June 3, 2021 — **already in NEW-2021-001**. Not new. |
| 17 | `Kentucky diver electrocuted yacht club 2022 "stop work order" Louisville lake death` | Keith Elkins, commercial diver, Prospect Yacht Club, Ohio River, April 2022 — **already in LEAD-007**. Not new. |
| 18 | `Nathaniel Davenport Jupiter Florida Harbourside fountain electrocution 2023 obituary memorial` | **NEW VICTIM CONFIRMED** — Nate Davenport, 45. Not in any project file. → `LOA8-OBT-2023-001.md` |
| 19 | `Syler Sparks Jupiter Florida fountain electrocution 2023 lawsuit Harbourside` | Second rescuer at Davenport incident; confirmed Davenport details. Not a separate ESD death. |
| 20 | `Meadors Anderson County South Carolina drowning electric shock 2023 lake dock marina victim` | Dr. Marshall L. Meadors III, 65, Lake Hartwell SC, July 17, 2023 — **already in NEW-2023-002**. Not new. |

### Category 5: ESDPA Press Releases Page — Cross-Checking Known Incidents

| Search # | Query / Check | Result |
|----------|-------|--------|
| 21 | Review of ESDPA press releases page (2018–2024 entries) | Identified "Recent HS graduate dies at Clyde Lake" → already NEW-2021-001; "July 9, 2023: 2 shocked at New Rochelle marina boat ramp" (non-fatal near-miss, already tracked in other LOAs); Keith Elkins 2022 → already LEAD-007. No new fatalities identified. |
| 22 | `"electric shock drowning" death 2018 lake dock victim family memorial` | Returned generic ESD awareness content. No new victims. |

### Category 6: Obituary Platform Direct Searches (Attempted)

| Search # | Platform | Query Attempted | Result |
|----------|----------|-----------------|--------|
| 23 | Legacy.com | `legacy.com obituary "drowned" "dock" "electric" lake memorial 2022 2023` | No results returned by Brave search (site: operator not supported in this tool). |
| 24 | Legacy.com | `legacy.com "electric shock" obituary lake dock drowning death` | No dedicated Legacy.com results. Null. |
| 25 | EverLoved/TributeArchive | Multiple keyword combinations | No obituary content accessible via external search engine. All returned navigation pages only. |

---

## Already-Documented Victims Re-Encountered (Confirmed Not New)

The following victims were surfaced during LOA8-D searches and verified as already documented in project files:

| Victim | Year | Location | Project File |
|--------|------|----------|-------------|
| Carmen Johnson, 15 | Apr 16, 2016 | Smith Lake, AL | FI-2016-007 |
| Kayla Matos, 11 | Jun 17, 2017 | Toms River, NJ | FI-2017-007 |
| Trevor Cate, 18 | Jun 3, 2021 | Clyde Lake, TX | NEW-2021-001 |
| Keith Elkins (diver) | Apr 2022 | Ohio River, Louisville KY | LEAD-007 |
| Dr. Marshall Meadors III, 65 | Jul 17, 2023 | Lake Hartwell, SC | NEW-2023-002 |
| Thomas Milner, 24 | Jul 27-28, 2023 | Lake Lanier, GA | NEW-2023-001 |
| Gabriel Gonzalez, 21 | Jul 10, 2025 | Marina Shores, IN | FI-2025-001 |
| Miller brothers (Timothy 53, Michael 50) | Jul 12, 2020 | Lake Pleasant, AZ | FI-2019-001 |
| Michael Cunningham (teen) | ~2004 | Stonewall Jackson Lake, WV | FI-2008-001 |
| McKenzie Kinley, 9 | — | Citrus Heights, CA (pool) | FI-2019-003 |
| Noah Winstead, 10 / Nate Lynam, 11 | Jul 4, 2012 | Cherokee Lake, TN | FI-2000-001 |
| James DeAngelo, 23 | Jul 4, 2021 | Monongahela River, PA | FI-2021-002 |
| Jesse Hamric, 18 | Jul 4, 2024 | Smith Mountain Lake, VA | (in project) |
| Shelly Darling, 34 / Elizabeth Whipple, 41 | Apr 14-15, 2017 | Lake Tuscaloosa, AL | SUSP-2017-042 |

---

## Methodology Limitations

**Direct obituary database keyword mining was not feasible** with the available search tools:

1. **Legacy.com:** The site's obituary full text is not indexed by search engines in a way that allows ESD-specific keyword queries. `site:` operators are not supported by the Brave Search MCP tool. Direct on-site search at legacy.com would be required.

2. **EverLoved:** Similar limitation — EverLoved pages appear in search results only when specifically linked from news articles, not through obituary keyword mining.

3. **TributeArchive:** Returns only navigation pages through external search engines.

4. **Find a Grave:** Memorial text not indexed in a searchable way for this purpose.

5. **GoFundMe:** Campaign content not accessible via Brave Search in a useful way.

**What did work:** General web searches for ESD deaths by year + location + keywords ("electric shock" + "lake" + "drowned" + "dock") surfaced news articles that named victims. This approach found the Nate Davenport case through news coverage rather than through direct obituary mining.

---

## Why LOA8-D Found Only One New Victim

The ESDPA incident list (Rev. 8/15/2025) and the project's 175+ incident files are already well-populated with known, documented ESD deaths. The major incidents that received substantial news coverage are already documented. The LOA8-D approach of searching for named victims via news and obituary sources is most effective for:

1. Incidents with local coverage only (small-town papers, not indexed well)
2. Incidents initially classified as "drowning" with no ESD suspicion at the time

The Nate Davenport case was found because it received national news coverage as a "fountain electrocution" rather than an "electric shock drowning." It was not in the project because it falls slightly outside the standard dock/marina ESD category. This suggests future searches should explicitly target:
- Pool electrocution deaths
- Public fountain electrocution deaths
- Flooded area / infrastructure electrocution deaths
- Any "electrocution near water" death, not just "electric shock drowning"

---

## Recommended Next Steps

1. **Direct Legacy.com on-site search:** Using a browser tool (if available), conduct keyword searches at legacy.com for "electric shock" + "dock" and "electrocuted" + "lake" + date ranges 2018–2025. The current search tools cannot access Legacy.com's internal search database.

2. **EverLoved on-site search:** Same limitation applies; direct browser access required.

3. **Harbourside Place prior-incident investigation:** The July 2023 shock reported by Dina Fleck at the same fountain (prior to Davenport's death) should be documented. This is a near-miss not in the project files.

4. **2023 New Rochelle marina boat ramp electrocution (non-fatal):** Referenced in ESDPA press releases (July 9, 2023 entry). Not confirmed as already in project files; should be checked.

5. **Cross-check the ESDPA Rev. 8/15/2025 list directly against project files** for any entries from 2020–2025 not yet fully researched.

---

## Search Count Summary

| Category | Searches | New Finds |
|----------|----------|-----------|
| EverLoved/TributeArchive direct | 4 | 0 |
| Find a Grave / GoFundMe | 3 | 0 |
| General ESD keyword by year | 6 | 0 |
| Named victim targeted | 7 | 1 (Nate Davenport) |
| ESDPA press releases cross-check | 2 | 0 |
| Legacy.com direct | 3 | 0 |
| **Total** | **25** | **1** |

---

*Research completed: March 8, 2026*
*LOA: LOA8-D — Systematic Obituary and Memorial Mining*
*Repository: `/opt/repos/esd-research/`*
