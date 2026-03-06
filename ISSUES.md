# ESD Incident List — Data Quality Issues

**Source:** "Electric Shock Drowning Incidents – Marinas©" Rev. 8/15/2025
**Authors:** James D. Shafer & Capt. David E. Rifkin, Quality Marine Services, LLC
**Analysis Date:** 2026-03-01

This document catalogues all identified data inconsistencies, ambiguities, and classification challenges found in the source PDF, and explains how each was handled in the `incidents-raw/` file set.

---

## 1. STRUCTURAL / NUMBERING ISSUES

### 1.1 Unlabeled Item Numbers in ESD Section
The following items appear in the ESD section without their item numbers printed:

| Inferred # | Date | Location | Basis for Assignment |
|------------|------|----------|----------------------|
| #8 | June 3, 2021 | Mission TX | Appears between numbered items #7 and #9 on page 4 |
| #49 | May 20, 2013 | Pulaski County KY | Appears between #48 and #50 |
| #69 | Aug 23, 2008 | Stonewall Jackson Lake WV | Appears between #68 and #70 |
| #76 | Mar 18, 2006 | Weiss Lake, Cherokee County AL | Appears between #75 and #77 |
| #82 | June 5, 2004 | Lake Waccamaw NC | Appears between #81 and #83 |
| #93 | Sept 30, 2000 | Put-in-Bay OH | Appears between #92 and #94 |
| #107 | May 11, 1991 | Oklahoma | Appears before numbered item #108 |

**Handling:** Assigned inferred numbers in all files and notes. Descriptions fully match sequence.

### 1.2 Item #65 Explicitly Removed
ESD section item #65 is listed as "Removed" with no description or date provided. No file was created.

### 1.3 Item #113 Contains Two Sub-Incidents
ESD item #113 (July 29, 1986) contains descriptions of TWO separate incidents:
- (A) Grosse Pointe Yacht Club, MI — single drowning, diver
- (B) Petosky, MI — single drowning, diver
Both noted as "relayed 3rd hand." Two files created: `FI-1986-001.md` and `FI-1986-002.md`.

### 1.4 Document Page Numbering Overflow
Pages 15–23 are labeled "Page 15–23 of 16" — the document grew beyond its original 16-page estimate. This is cosmetic and does not affect incident data.

---

## 2. DATE DISCREPANCIES (Same Incident, Different Dates Across Sections)

The NM section header states "(Additional ones included above)" confirming intentional cross-referencing. However, many cross-referenced entries carry different dates. The ESD section date is used as primary in all files.

| ESD # | NM # | ESD Date | NM Date | Gap (days) | Severity | Notes |
|-------|-------|----------|---------|-----------|----------|-------|
| #1 | 1 | Jul 11, 2025 | Jul 11, 2025 | 0 | None | Identical |
| #2 | 2 | Jun 21, 2025 | Jun 21, 2025 | 0 | None | Identical |
| #3 | 3 | Jul 4, 2024 | Jul 4, 2024 | 0 | None | Identical |
| #10 | 4 | Aug 30, 2020 | Nov 4, 2020 | 66 | Moderate | Tropical Storm ETA hit FL Nov 9–12, 2020 — Nov date more plausible; ESD section date likely in error |
| #12 | 5 | Sep 19, 2019 | Aug 12, 2020 | 327 | **MAJOR** | Nearly a year apart; possibly different incidents or severe transcription error |
| #16 | 10 | Sep 1, 2017 | Sep 30, 2018 | 394 | **MAJOR** | Over one year apart despite identical descriptions; severe transcription error likely |
| #17 | 16 | Aug 29, 2017 | Sep 1, 2017 | 3 | Minor | Both during Hurricane Harvey; 3-day gap may reflect reporting vs. event date |
| #23 | 21 | May 22, 2017 | Jun 17, 2017 | 26 | Minor | Same incident (Put-In-Bay OH, Miller Marina); 26-day gap |
| #26 | 22 | Apr 14, 2017 | May 19, 2017 | 35 | Minor | Florence AL pool; 35-day gap |
| #31 | 26 | May 29, 2016 | Jul 3, 2016 | 35 | Minor | Tennessee Lake; 35-day gap |
| #32 | 27 | Jun 27, 2016 | May 29, 2016 | -29 | Minor | Silver Spring Township PA; dates REVERSED in NM section |
| #35 | 28 | Mar 27, 2016 | Apr 16, 2016 | 20 | Minor | Smith Lake AL; also spelling discrepancy: "Princeville" vs "Priceville" |
| #38 | 31 | Aug 24, 2014 | Jun 21, 2015 | 300 | **MAJOR** | Lake of the Ozarks MO, same 22.2 mile marker; 10-month gap despite identical descriptions |
| #59 | 41 | Jun 27, 2012 | Jul 4, 2012 | 7 | Minor | German Creek Marina TN; 7-day gap |
| #60 | 42 | May 5, 2012 | Jun 27, 2012 | 53 | Moderate | Celebration FL mini-golf pond; 53-day gap |

---

## 3. POTENTIALLY SEPARATE INCIDENTS WITH CONFLICTING DATA

### 3.1 ESD #36 vs NM #29 — Palm Springs FL vs CA (UNRESOLVED)

| Field | ESD #36 | NM #29 |
|-------|---------|--------|
| Date | Aug 8, 2015 | Mar 27, 2016 |
| Location | Palm Springs, **FL** | Palm Springs, **CA** |
| Outcome | Man died; daughter (10yo) died at hospital | Man died; one girl in **critical condition** (not confirmed dead) |
| Others | 5 others treated | 5 others treated |
| Cause | Faulty pool wiring | Faulty pool wiring |
| Homes built | 1963 | 1963 |

**Assessment:** Both descriptions are nearly identical in structure and cause, but differ in:
- State (FL vs CA) — two different cities both named "Palm Springs"
- Date (7-month gap)
- Outcome (daughter died in ESD version vs. critical condition in NM version)

**Possible explanations:**
1. Same incident, significant transcription errors in state and date
2. Two genuinely separate incidents with strikingly similar circumstances

**Handling:** Created one FI file (`FI-2015-001.md`) using ESD #36 as primary, noting NM #29 discrepancies. Classified FI because deaths are confirmed in ESD section. Flagged as unresolved.

---

## 4. OUTCOME UNCERTAINTY

### 4.1 "Last Known in Critical Condition" Cases

| ESD # | Date | Location | Last Known Status |
|-------|------|----------|-------------------|
| #32 | Jun 27, 2016 | Silver Spring Township PA | 8yo girl in critical condition |
| #34 | Apr 16, 2016 | Wildwood Crest NJ | 34yo man in critical condition |

**Handling:** Both classified as FI because they are listed in the ESD Drownings section (implying likely fatality) and critical condition from electric shock frequently results in death. Outcome uncertainty noted in Classification Notes of each file.

---

## 5. CLASSIFICATION CHALLENGES

### 5.1 Items in ESD Section Where All Humans Survived

| ESD # | Date | Location | Why Listed in ESD Section | Classification Used |
|-------|------|----------|---------------------------|---------------------|
| #31 | May 29, 2016 | Tennessee Lake TN | 13yo in trouble; 2 adults overcame shock but saved him; all survived | **NM** |

### 5.2 Items in NM Section Involving Human Fatalities

These NM entries involve deaths — they appear in NM section because at least one person in the incident survived. All classified as FI:

| NM # | ESD # | Fatalities |
|-------|-------|------------|
| 1 | 1 | 21yo died (23yo survived) |
| 2 | 2 | 13yo died |
| 3 | 3 | 18yo died |
| 4 | 10 | Man died |
| 5 | 12 | 2 brothers died |
| 10 | 16 | Man electrocuted (fatal) |
| 16 | 17 | 2 men killed |
| 21 | 23 | 19yo died |
| 22 | 26 | Man and son died |
| 28 | 35 | One girl drowned |

### 5.3 Wildlife-Only Fatality

| ESD # | Date | Victims | Classification Used |
|-------|------|---------|---------------------|
| #85 | May 2003 | 6 ducks | FI — documented fatality; no humans harmed |

---

## 6. INCIDENTS WITH UNKNOWN OR APPROXIMATE DATES

| ESD # / NM # | Date as Listed | File ID | Notes |
|-------------|----------------|---------|-------|
| ESD #64 | [none] | FI-XXXX-001.md | Lake Freeman, Carroll County IN; no date in PDF |
| ESD #92 | 2000 or 2001 | FI-2000-001.md | Norris Lake TN; used 2000 |
| ESD #98 | Approx. 1999 | FI-1999-005.md | South Carolina |
| ESD #100 | Approx. 1998 | FI-1998-001.md | Lake Sonoma CA |
| ESD #103 | Approx. 1994 | FI-1994-001.md | Bolling AFB, Washington DC |
| ESD #112 | 1987 or 1988 | FI-1987-001.md | Park Township MI; used 1987 |
| ESD #115 | Date Unknown | FI-XXXX-002.md | St Croix River, Prescott WI |
| ESD #116 | Date Unknown | FI-XXXX-003.md | Community pool, Oklahoma |
| NM #68 | Date Unknown | NM-XXXX-001.md | Man rescues dog |
| NM #69 | 2002-2003 | NM-2002-001.md | Florida divers; used 2002 |
| NM #71 | Date & Location Unknown | NM-XXXX-002.md | Swimmer feels A/C discharge tingle |

---

## 7. INCIDENTS WITH INCOMPLETE DETAILS

| ESD # | Date | Location | Missing Information |
|-------|------|----------|---------------------|
| #3 | Jul 4, 2024 | Smith Mountain Lake VA | "Details pending" — outcome confirmed fatal but no cause established |
| #6 | Jul 4, 2021 | Louisville KY | "Details pending" — coroner noted electricity, no specific source |
| #13 | Jul 19, 2019 | Jefferson County TX | Source of electricity not reported |
| #79 | Sep 13, 2004 | Lake of the Ozarks MO | No information on cable |

---

## 8. INTERNATIONAL INCIDENTS

The document focuses on US incidents. The following international incidents are included with notation:

| ESD # / NM # | Date | Location | Notes |
|-------------|------|----------|-------|
| ESD #21 | Jun 18, 2017 | Akyazi, Turkey | Explicitly noted as exception: "could have happened in the USA" |
| NM #17 | Jul 24, 2017 | Kelowna, British Columbia, Canada | — |
| NM #23 | May 8, 2017 | Ottawa, Canada | — |
| NM #57 | Jul 1, 2007 | Kingston, Ontario, Canada | — |

---

## 9. SUMMARY OF DATA QUALITY BY SEVERITY

| Severity | Count | Examples |
|----------|-------|---------|
| MAJOR discrepancy | 4 | ESD #12/#36 date/location, ESD #16, ESD #38 date gaps |
| MODERATE discrepancy | 3 | ESD #10 date, ESD #60 date gap, ESD #35 spelling |
| MINOR discrepancy | 8 | Small date gaps in cross-section duplicates |
| Structural issue | 5 | Unlabeled items, #65 removed, #113 split, page count |
| Outcome uncertain | 2 | ESD #32, #34 |
| Unknown dates | 11 | See Section 6 |

---

*Analysis performed during extraction to `incidents-raw/` — see `CLAUDE-PROMPT.md` for full extraction methodology.*

---

## Research Findings — Data Quality Issues

*Added 2026-03-06 after independent research of all 175 incidents.*

The following issues were discovered during independent research using primary sources (news archives, obituaries, court records, CDC reports, trade journals). These go beyond the extraction-stage issues documented above — they reflect errors in the underlying ESDPA data that could only be found by checking against independent sources.

### 10. CRITICAL DATE ERRORS (6+ Months Off)

Independent sources revealed that 15 incidents have ESDPA dates that are off by more than 6 months, often placing them in the wrong calendar year:

| Incident | ESDPA Date | Correct Date | Error | Verification Source |
|----------|-----------|-------------|-------|---------------------|
| FI-2008-001 (Stonewall Jackson Lake, WV) | Aug 23, 2008 | May 29, 2010 | ~21 months | Doan Law Firm, WV Public Broadcasting |
| FI-2007-001 (Lake Hamilton, AR) | Jul 28, 2007 | Aug 23, 2008 | ~13 months | Arkansas Democrat-Gazette, KAIT8 News |
| FI-1999-001 (Tims Ford Lake, TN) | Aug 1, 1999 | Sep 30, 2000 | ~13 months | Mike Holt Enterprises, OnTime Service |
| FI-2017-001 (Bricktown Canal, OKC) | Sep 1, 2017 | Sep 30, 2018 | 394 days | KFOR, News 9, Legacy.com |
| FI-2002-001 (North Fort Myers, FL) | May 31, 2002 | May 8, 2003 | ~11 months | Orlando Sentinel, Legacy.com |
| FI-2010-001 (Lake City, MN) | Jul 26, 2010 | May 28, 2011 | ~10 months | In-Depth Outdoors Forum, Find a Grave |
| FI-2019-001 (Lake Pleasant, AZ) | Sep 19, 2019 | Jul 12, 2020 | ~10 months | 12 News, ABC15 Arizona |
| FI-2003-001 (Lake Wylie, NC) | Aug 3, 2003 | Jun 5, 2004 | ~10 months | Earlier ESDPA list versions |
| FI-2012-001 (Rough River Lake, KY) | Sep 27, 2012 | May 20, 2013 | ~8 months | WHAS11, The News-Enterprise |
| FI-2013-001 (North Miami, FL) | Sep 2013 | Apr 13, 2014 | ~7 months | CBS Miami, NBC Miami |
| FI-2020-001 (Clyde Lake, TX) | Nov 4, 2020 | Jun 2, 2021 | ~7 months | NBC DFW, KTXS |
| FI-2016-001 (Raleigh, NC) | Sep 10, 2016 | Mar 29, 2017 | ~6 months | WRAL, Edwards Kirby |
| FI-2018-001 (Dixon, CA) | Sep 30, 2018 | Apr 1, 2019 | 6 months | CBS News, Mercury News |
| FI-2022-001 (Detroit, MI) | Aug 16, 2022 | Feb 7, 2023 | ~6 months | Phantom duplicate; see Section 12 |
| FI-2012-006 (Tampico, IL) | Jul 25, 2012 | Jul 25, 2011 | 1 year (wrong direction) | Shaw Local, Quad-City Times |

**Note:** Many additional incidents have date errors of 1-8 weeks. Among all verified incidents, approximately 80% required some form of date correction.

### 11. MISCLASSIFICATION: NM-2016-001 (Double Fatality Listed as Near Miss)

**The most significant error found in the entire dataset.**

NM-2016-001 (Chickamauga Lake, TN) is classified in the ESDPA list as a Near Miss with the implication that all involved survived. Independent sources unanimously confirm this was a **double fatality**:

- **Donna Berger**, age 55 — died
- **Randy Freeney**, age 74 — died
- **Zachary Berger**, age 13 — survived (the only survivor)

The correct date is **June 17, 2016** (not May 29 or July 3 as listed in different sections of the ESDPA document). The location is Chickamauga Lake near Sale Creek, Hamilton County, TN.

Sources: WSOC-TV, WTVC NewsChannel 9 (multiple articles), Chattanoogan.com obituary, Chattanooga Times Free Press, WRCB.

This incident should be reclassified from NM to FI.

### 12. PHANTOM DUPLICATE: FI-2022-001

FI-2022-001 (Detroit flooded basement, August 16, 2022) and FI-2023-001 (Detroit flooded basement, February 7, 2023) have **word-for-word identical descriptions** in the ESDPA list. Independent research confirms only one real incident: **James Stanley**, age 62, died on **February 7, 2023** at Russell Woods Apartments, Detroit, MI.

No evidence exists for any similar incident in August 2022. FI-2022-001 is a phantom entry that inflates the ESDPA incident count by one.

Sources: ClickOnDetroit (WDIV), FOX 2 Detroit, WXYZ, Cobbs Funeral Home obituary.

### 13. INCIDENT CONFLATION: FI-2017-010 (Two Incidents Merged)

The ESDPA entry for FI-2017-010 describes "two brothers" dying in a flooded field near Laredo, TX. Independent sources reveal this is a **conflation of two separate incidents**:

1. **Laredo, TX (May 21, 2017):** One victim — Aldo Jordani Rojas, 14, stepped in a puddle near a downed power line. No brother was involved.
2. **Fort Worth, TX (March 29, 2017):** Two brothers (the Lopez brothers) died in a separate incident.

The ESDPA entry merged details from both events into a single record.

Sources: CBS Austin, CBS Texas, FOX 4.

### 14. VICTIM COUNT AND OUTCOME ERRORS

Several incidents have incorrect victim counts or outcomes:

| Incident | ESDPA Description | Actual Finding | Source |
|----------|------------------|----------------|--------|
| FI-2012-006 (Tampico, IL) | "Boy and girl" killed | **Two girls** killed (Hannah Kendall and Jade Garza, both 14) | Shaw Local, Quad-City Times |
| FI-2013-002 (Houston, TX) | "Older man" died | Victim was 27 years old (Raul Hernandez Martinez) | KHOU, Courthouse News |
| FI-2016-004 (Silver Spring Twp, PA) | Classified as FI | Victim (8yo girl) last known in critical condition — outcome never confirmed | FOX43, ABC News |
| FI-2016-006 (Wildwood Crest, NJ) | "Last known in critical condition" | Victim **died** (Greg Subiszak, 34) | PhillyVoice, NJ 101.5 |
| FI-2017-002 (Hurricane Harvey) | 5 men on boat | **7 men** on boat (5 rescuers + 2 journalists). 2 confirmed dead, 2 missing/presumed dead | ABC News, Washington Post |
| NM-2013-004 (Lake Lanier, GA) | "Daughter" shocked | Victim was **granddaughter** (Ava Muter) | Gainesville Times |

### 15. LOCATION ERRORS

| Incident | ESDPA Location | Correct Location | Distance Off | Source |
|----------|---------------|-----------------|-------------|--------|
| FI-1986-003 | Lexington, KY | **Louisville, KY** | ~80 miles | ODMP, Louisville Metro PD |
| FI-2002-001 | Cape Coral, FL | **North Fort Myers, FL** | Adjacent city | Orlando Sentinel |
| FI-1999-004 | "Cedar Hill Lake" | **Center Hill Lake** | Different lake entirely | Sligo Marina, DeKalb County tourism |
| FI-2013-001 | North Miami Beach, FL | **North Miami, FL** | Different city | CBS Miami, NBC Miami |
| NM-2018-005 | Smith Mountain Lake, **GA** | Smith Mountain Lake, **VA** | Wrong state | WDBJ7, Smith Mountain Eagle |
| NM-2017-005 | Ottawa, Canada | **Gatineau, Quebec**, Canada | Different city/province | CBC News |
| NM-2016-002 | Shiloh, **MO** | Shiloh, **IL** | Wrong state | e-Hazard |
| NM-2017-001 | Kelowna, BC | **Spallumcheen, BC** | Different city | CBC News, Vernon Morning Star |

### 16. THE FI-1995-001 DATE ANOMALY

FI-1995-001 (Lake Mead houseboat drowning) presents an unresolvable discrepancy:
- **Current ESDPA list (Rev. 8/15/2025):** Lists the date as **February 1995**
- **All earlier publicly accessible versions:** List the date as **July 1997**

No independent sources exist for either date. If the July 1997 date is correct, this incident was moved backward in time by 2.5 years between list revisions, and the file should be reclassified as FI-1997-XXX.

### 17. INTERNALLY IMPOSSIBLE DATES

Two incidents have dates that are physically or meteorologically impossible:

1. **FI-1997-001 (AF Base, Washington, DC):** Listed as July 1997, but describes a boy **walking on ice**. Average July temperatures in Washington, DC exceed 90F. The actual month is likely January or February.

2. **FI-2020-002 (Bradenton Beach, FL):** Listed as August 30, 2020, during "Tropical Storm Eta." Tropical Storm Eta did not form until **November 8, 2020** and affected Florida November 11-12. The correct date is November 11, 2020.

### 18. POSSIBLE DUPLICATE: FI-1997-001 / FI-1994-001

Both FI-1997-001 and FI-1994-001 describe a boy electrocuted at a dock at an Air Force base in Washington, DC. Given the internally impossible date on FI-1997-001 (July + ice), the small geographic area involved (Bolling AFB / Capital Cove Marina), and the zero independent verification for either incident, these may describe the same event.

### 19. SCIENTIFICALLY QUESTIONABLE: FI-1993-001 (Salt Water ESD)

FI-1993-001 is classified as an ESD fatality in salt water (Texas boatlift). ESD researchers note that salt water ESD is extremely rare because high conductivity in salt water causes circuit breakers to trip before dangerous current levels can reach a swimmer. This incident has zero independent verification and the classification as ESD is scientifically questionable.

### 20. SUMMARY OF RESEARCH-IDENTIFIED DATA QUALITY ISSUES

| Category | Count |
|----------|------:|
| Date errors > 6 months (verified) | 15 |
| Date errors 1 week – 6 months (verified) | ~35 |
| Date errors 1-7 days (verified) | ~15 |
| Location errors | 8 |
| Misclassification (NM should be FI) | 1 |
| Phantom duplicate | 1 |
| Incident conflation (two merged into one) | 1 |
| Victim count / outcome errors | 6 |
| Internally impossible dates | 2 |
| Possible duplicates (unresolvable) | 1 |
| Scientifically questionable classification | 1 |
| Unresolvable date anomaly across list revisions | 1 |
