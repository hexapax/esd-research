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
