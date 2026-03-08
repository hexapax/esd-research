# LOA13: Internet Archive / Wayback Machine Recovery
## Electric Shock Drowning Research — Archived Article Recovery

**Date conducted:** March 8, 2026  
**Researcher:** Claude Sonnet 4.6  
**Output directory:** `/opt/repos/esd-research/phase2-findings/LOA13-wayback/`

---

## Executive Summary

LOA13 attempted to recover deleted/archived local newspaper articles about ESD incidents using the Wayback Machine CDX API and supplementary web searches. The primary finding is that **the Wayback Machine did not archive the specific local newspaper pages** for the target incidents in gap years (1990, 1992, 1996, 2004, 2007, 2009). Local newspapers from this era were not systematically web-indexed until 2000-2005 at the earliest, and the specific articles about ESD incidents were not captured before being deleted.

However, the research produced significant **new findings via Perplexity and Brave web searches** that are documented as recovered content below. Several previously unidentified victim names and legal case details were found through non-Wayback sources accessible today.

---

## CDX API Queries Attempted

All CDX API queries used the endpoint format:  
`https://web.archive.org/cdx/search/cdx?url=DOMAIN&output=json&fl=timestamp,original&limit=N&from=YYYYMMDD&to=YYYYMMDD`

### Query 1: Watertown Daily Times (Alexandria Bay NY 1993 incident)
- **URL pattern:** `*.watertowndailytimes.com/*`
- **Date range:** 1993-01-01 to 1993-12-31
- **Result:** TIMEOUT — CDX API timed out (504 Gateway Time-out)
- **Availability API check:** `watertowndailytimes.com` — Earliest snapshot: June 18, 2000. **No archives from 1993.** The paper's website did not exist in 1993 (newspaper websites were not widespread until mid-to-late 1990s).

### Query 2: Watertown Daily Times — Expanded range
- **URL pattern:** `watertowndailytimes.com`
- **Date range:** 1996-2000
- **Result:** Earliest Wayback snapshot: `20000618013039` (June 18, 2000). No 1993-era content archived. The paper's web presence post-dates the 1993 Alexandria Bay incident by 7 years.

### Query 3: NNY360.com (Northern NY papers successor domain)
- **URL pattern:** `nny360.com`
- **Date range:** 2000-2005
- **Result:** No results — domain likely did not exist until after 2005.

### Query 4: Austin American-Statesman (Lake Travis TX August 2004)
- **URL pattern:** `*.statesman.com/*`
- **Date range:** 2004-08-01 to 2004-08-31
- **Result:** No CDX results. Availability API: No snapshot of `statesman.com` from August 2004 available.
- **Note:** The statesman.com domain was active in 2004 but the CDX API returned no matches for this date range, suggesting the Wayback Machine did not archive statesman.com pages from this period, or the relevant articles were behind a paywall.

### Query 5: WECT-TV (Wilmington NC) — Lake Waccamaw 2010
- **URL pattern:** `*.wect.com/*drowning*`
- **Date range:** 2010-06-01 to 2010-07-31
- **Result:** No results.

### Query 6: Star News Online (Wilmington NC)
- **URL pattern:** `*.starnewsonline.com/*drowning*`
- **Date range:** 2010-06-01 to 2010-07-31
- **Result:** No results.

### Query 7: WWAY-TV3 (Wilmington NC) — Lake Waccamaw electric
- **URL pattern:** `*.wwaytv3.com/*electric*`
- **Date range:** 2010-06-01 to 2010-07-31
- **Result:** No results.

### Query 8: Oregonlive.com — Multnomah Channel 1999
- **URL pattern:** `*.oregonlive.com/news/*`
- **Date range:** 1999-08-01 to 1999-09-01
- **Result:** No results. Domain was not being archived by Wayback Machine in August 1999.

### Query 9: STLToday.com — DeSoto MO March 2006
- **URL pattern:** `stltoday.com/*harbison*` and `stltoday.com/*electrocution*`
- **Result:** No matching CDX entries found. Availability API confirmed `stltoday.com` was archived on March 19, 2006 (timestamp: `20060319232751`), but the specific article URLs were not captured.

### Query 10: Whiteville NC news (Columbus County)
- **URL pattern:** `*.whiteville.com/*`
- **Date range:** 2004-06-01 to 2004-06-30
- **Result:** No results.

---

## Wayback Machine Availability API Results

| Domain | Target Date | Earliest Archive Found | Notes |
|--------|------------|----------------------|-------|
| watertowndailytimes.com | 1993-08 | 2000-06-18 | Pre-web era; no 1993 archives |
| statesman.com | 2004-08 | None found | Site existed but not archived for this date |
| stltoday.com | 2006-03-20 | 2006-03-19 | Main page archived; article URLs not captured |
| nny360.com | 2000-2005 | No results | Domain likely post-2005 |
| oregonlive.com | 1999-08 | No results | Not archived in 1999 |

---

## Gap Year Analysis: Why Wayback Machine Cannot Fill These Gaps

### Pre-2000 Incidents (1990, 1992, 1993, 1996)
The Wayback Machine began archiving in 1996, but most local newspapers did not have functional websites until 1998-2002. The Alexandria Bay NY incident (July/August 1993), Oklahoma lake incidents (1991, 1993), and other pre-2000 events occurred before the web era for local news. **No Wayback recovery is possible for these incidents.**

### 2000-2005 Incidents
Some local newspapers had websites during this period, but:
1. The Wayback Machine did not comprehensively crawl local news sites
2. Many newspaper CMS systems used dynamic URLs that are not preserved
3. Subscription-paywalled content was excluded from crawls
4. The Austin American-Statesman, Watertown Daily Times, and Wilmington Star-News from this era are not recoverable via Wayback

---

## Alternative Sources Found: Significant New Research Results

### FINDING 1: DeSoto MO Victim Fully Identified (FI-2006-XXX / SUSP-2006-043)

**Victim:** Nicholas "Nic" Harbison, age 16, of De Soto, MO  
**Date:** March 18, 2006 (shortly before 7:00 p.m. on Saturday)  
**Location:** Spring Lake, Summerset Lake subdivision, off Highway E, ~5 miles from De Soto, Jefferson County, MO  

**Confirmed from St. Louis Post-Dispatch article (reproduced in Google Groups):**
> "De Soto teen is electrocuted; two others are hurt" — By Bill Bryan and Michele Munz, St. Louis Post-Dispatch, 03/20/2006

Key facts:
- Nicholas Harbison, 16, star sophomore basketball player for DeSoto High School, was killed
- Morgan Milfeld, 15, and Timothy Fitzpatrick, 15, were critically injured; flown to St. John's Mercy Medical Center in Creve Coeur
- Josh McClure, 18, was unhurt (4th teen in water; his father was the homeowner who jumped in and pulled all four out)
- Teens had been in a hot tub at the home of Tracy and Ginger Jones in the Summerset Lake subdivision
- Current ran down an aluminum ladder from dock wiring into the water
- The dock had electrical power for a power boat lift and lighting
- Jefferson County Sheriff Oliver "Glenn" Boyer confirmed Ameren UE was investigating

**Legal outcome (from Gray Ritter Graham law firm newsletter and Dallas/Fort Worth Injury Lawyer):**
- On March 18, 2006: four teens jump into Spring Lake
- Harbison drowns; Milfeld and Fitzpatrick nearly drowned, required induced coma for 5 days
- Jefferson County civil jury (2009) found AmerenUE liable — $2.3 million verdict
  - Harbisons (parents Jerry and Tina Harbison): $1.25 million
  - Timothy Fitzpatrick (and parents Bryan and Diana Fitzpatrick): $725,000
  - Morgan Milfeld (and parents Felix and Tarrole Milfeld): $350,000
- Root cause: Underground power distribution cable from AmerenUE with defective/missing neutral; neutral current returned to substation through earth and into Spring Lake; current concentrated at bonded swim ladder
- AmerenUE blamed the Jones family's dock wiring (done by homeowner); jury disagreed

**Sources:**
- St. Louis Post-Dispatch, March 20, 2006 (reproduced in Google Groups): `https://groups.google.com/g/alt.support.childfree/c/pxVSLwfqN6s`
- Gray Ritter Graham Newsletter (PDF, law firm that tried the case): `https://www.grgpc.com/assets/htmldocuments/uploads/2016/11/grg41.pdf`
- Dallas Fort Worth Injury Lawyer Blog: `https://www.dallasfortworthinjurylawyer.com/missouri_jury_orders_electric/`
- Claims Journal (August 13, 2013): `https://www.claimsjournal.com/news/midwest/2013/08/13/234750.htm`

**Assessment:** VERIFIED — Multiple independent primary sources. The St. Louis Post-Dispatch article from March 20, 2006 is reproduced in a Google Groups post and constitutes a recovered news article. The ESDPA list entry (date: "Mar 18, 2006, Summerset Lake near Desoto, St. Louis, MO") is confirmed correct for date and location.

---

### FINDING 2: Lake Waccamaw NC Incidents — Two Separate ESD Events

The ESDPA list contains TWO distinct ESD incidents at Lake Waccamaw, NC (Columbus County):

**Incident A — June 19, 2004:**
- 10-year-old boy drowned while swimming with friends near a private dock boat lift that had just been raised from the water
- An adult reported a heavy shock when touching the lift; several children in water reported being shocked
- Victim was found motionless face-down; could not be revived
- Cause: Lift frame became energized; bonding conductor from supply panel was not connected
- Source: ESDPA list (multiple versions confirmed consistent date of June 19, 2004)
- **No victim name found in any accessible online source**
- The ECM ebook "Electric Shock Drowning" (2018) describes a detailed forensic engineering case study titled "The Case of the Floating Dock" authored by John Cavallaro, P.E., Forensic Engineering, Inc. — this appears to describe either the 2004 or 2010 Lake Waccamaw incident (floating dock, boy hanging from boat lift rails with feet in water, electrocuted, open ground + water-filled junction box)

**Incident B — June 2010:**
- A boy was killed swimming near a boat lift
- Owner was told by another child that he was feeling tingles in the water
- Owner reached up, touched the boat lift, was shocked; told other kids to get out of water
- After exiting, one boy found face-down in water; could not be revived at scene
- Cause: Open ground in lines from house to dock; one small junction box under dock filled with water; possibly also a fault in the lift motor
- Source: ESDPA list (consistent across versions)
- **No victim name found in any accessible online source**

**Assessment:** Both incidents are ESDPA-only; no independent primary sources found. The ECM ebook forensic case study (Cavallaro, PE) likely describes one of these two Lake Waccamaw incidents but does not name the victim or give the exact date. Recommend FOIA/records request to Columbus County, NC.

---

### FINDING 3: Lake Wylie Charlotte NC — June 5, 2004 Double ESD

Separate from the Lake Waccamaw incident, the ESDPA list also contains:

**Date:** June 5, 2004  
**Location:** Lake Wylie, Charlotte, NC  
**What happened:** Two young boys swimming at bow of houseboat called for help. Father of victim and friend rushed forward — boy on ladder said he was being shocked; other boy in water not moving. Friend rushed aft to pull shore cord. Father entered water; his son could not be resuscitated.  
**Cause:** Substantial errors in wiring on both the dock and the boat, apparently done by unqualified individuals.  
**Status:** One fatality confirmed (the son of the father who entered the water).

**Assessment:** No victim name, no independent source found. The WCNC-TV YouTube video "Child who drowned in Lake Wylie laid to rest" may reference this case but the auto-captions were not sufficient to confirm.

---

### FINDING 4: Lucas Ritz (OR, 1999) — Full Victim Identification Confirmed

**Victim:** Lucas Ritz, age 8 (some sources say "10" due to age-at-death vs. age-when-incident-occurred confusion; born c. 1991; age 8 at time of incident August 1, 1999)  
**Date:** August 1, 1999  
**Location:** Multnomah Channel of the Willamette River, near Scappoose, Oregon (freshwater marina, tributary of the Willamette River north of Portland)  
**Parents:** Kevin Ritz (father, subsequently became Master Marine Technician and co-founder of ESDPA) and Sheryl Ritz (mother, a graduate nurse; was in the water and became paralyzed)  
**Brother:** Ian Ritz, age 10 at time of incident  
**Cause:** AC fault aboard a docked powerboat (120 volts leaking into water); death certificate initially stated "drowning," subsequently changed to "electrocuted in water while swimming"  
**Cause of death per Multnomah County Coroner:** Initially "drowning" — changed after Kevin Ritz's own investigation

**Multiple independent sources confirming this incident:**
- BoatUS Expert Advice Archive (February 2019): `https://www.boatus.com/expert-advice/expert-advice-archive/2019/february/a-preventable-dockside-tragedy`
- Safe Electricity (educational org): `https://safeelectricity.org/lucas-sake-learn-prevent-esd/`
- ICL Cooperative (2024): `https://icl.coop/water-recreation-electric-shock-drowning-lucas-story/`
- Sail-World (Australia, 2009): `https://www.sail-world.com/Australia/Dock-tragedy-shows-danger-of-fresh-water-marinas/-62455`
- Boating Magazine (April 2013): `https://boatingmag.com/how-to/electric-shock-drowning-prevention/`

**Assessment:** VERIFIED by multiple independent sources. This is NOT a gap year incident (1999 is in the ESDPA list) but represents the underrepresented state of Oregon. The original 1999 Oregonian newspaper article was not recoverable via Wayback Machine (no CDX results for oregonlive.com from August 1999), but extensive documentation exists through Kevin Ritz's public advocacy.

---

### FINDING 5: Lake Travis TX Incident Date Discrepancy

Cross-referencing multiple versions of the ESDPA list revealed conflicting dates for the Lake Travis Austin TX incident:

| ESDPA Version | Date Listed |
|--------------|-------------|
| Harbor Marine June 2004 (2CoolFishing copy) | No Joule marks; described as recent |
| ESDPA Rev 5/9/2016 | August 8, 2004 |
| ESDPA Rev 8/15/2016 | August 8, 2004 |
| ESDPA Rev 10/17/2017 | August 8, 2004 |
| ESDPA Rev 11/19/2020 | August 8, 2004 |
| ESDPA Rev 8/1/2024 | **June 19, 2004** |
| ESDPA Rev 8/15/2025 | August 8, 2004 |

The August 1, 2024 revision (mikeholt.com/files/PDF/Electric_Shock_Drowning_Incident_List_8-1-24.pdf) lists the date as **June 19, 2004**, which appears to be a brief anomaly in that revision. The TPWD Game Warden Field Notes from August 9, 2004 confirm a DIFFERENT Lake Travis drowning (party barge slide accident in Devil's Cove on or around August 9, 2004), not the ESD marina dock incident. No Austin American-Statesman article was recoverable via Wayback Machine for either date.

---

## Prong 3: Direct Archive.org Full-Text Search

Attempted: `https://archive.org/advancedsearch.php?q=%22electric+shock+drowning%22+%22dock%22&mediatype=texts`

**Result:** No relevant newspaper articles recovered. The archive.org texts collection contains scanned books and academic materials, not local newspaper content from 1990-2010.

**Brave Search for archive.org ESD content:** Multiple queries attempted; all returned Princeton NJ local papers and unrelated content, not ESD-related newspaper articles.

---

## Why Wayback Machine Recovery Failed for Gap Years

The Internet Archive's Wayback Machine has fundamental limitations for this research:

1. **Pre-1996:** No web archiving possible (web was in its infancy; local papers had no websites)
2. **1996-2000:** Sparse coverage; most local papers not yet on web
3. **2000-2005:** Local newspapers were online but the Wayback Machine crawled them sporadically; specific article URLs were often not captured
4. **Paywall content:** The Austin American-Statesman and similar papers had paywalls in the early 2000s; Wayback Machine excludes paid content
5. **Dynamic CMS URLs:** Many early newspaper CMS systems used session-based or database-generated URLs that change on each visit; the Wayback Machine cannot re-serve these
6. **robots.txt exclusion:** Some news sites excluded Wayback crawlers

---

## Summary of CDX Queries (All Results)

| Query # | Target URL | Date Range | Result |
|---------|-----------|-----------|--------|
| Q1 | *.watertowndailytimes.com/* | 1993-01-01 to 1993-12-31 | TIMEOUT (504) |
| Q2 | watertowndailytimes.com | 1996-2000 | Earliest snapshot: 2000-06-18 only |
| Q3 | nny360.com | 2000-2005 | No results |
| Q4 | *.statesman.com/* | 2004-08-01 to 2004-08-31 | No results |
| Q5 | *.wect.com/*drowning* | 2010-06-01 to 2010-07-31 | No results |
| Q6 | *.starnewsonline.com/*drowning* | 2010-06-01 to 2010-07-31 | No results |
| Q7 | *.wwaytv3.com/*electric* | 2010-06-01 to 2010-07-31 | No results |
| Q8 | *.oregonlive.com/news/* | 1999-08-01 to 1999-09-01 | No results |
| Q9 | stltoday.com/*harbison* | All dates | No results |
| Q10 | stltoday.com/*electrocution* | All dates | No results |
| Q11 | *.whiteville.com/* | 2004-06-01 to 2004-06-30 | No results |

---

## Recommendations for Further Recovery

### Highest Priority
1. **Watertown Daily Times microfilm (Alexandria Bay NY 1993):** Physical microfilm at Flower Memorial Library, 229 Washington Street, Watertown, NY 13601. Watertown Daily Times is the only newspaper serving Jefferson County. LOC catalog: sn84035541.

2. **Austin American-Statesman paywalled archives (Lake Travis TX 2004):** Access via NewsBank or ProQuest. Search for Lake Travis drowning, August 2004, marina dock. Travis County Medical Examiner public records request also viable.

3. **Columbus County, NC death records (Lake Waccamaw 2004, 2010):** Both incidents are documented by ESDPA but no victim names found. NC Office of Vital Statistics death certificate index search for drowning victims in Columbus County, June 2004 and June 2010.

4. **Willamette Week / The Oregonian archives (Lucas Ritz 1999):** ProQuest Historical Newspapers has The Oregonian back to 1861. Search for "Multnomah Channel" "drowning" "1999" OR "Lucas Ritz" OR "electric" "marina."

### Secondary Priority
5. **Missouri circuit court records (Harbison v. AmerenUE):** Jefferson County Circuit Court. Case filed by Jerry Harbison. Full case file would contain expert witness reports, investigation findings, and potential discovery documents about the fault mechanism.

6. **TPWD records request (Lake Travis TX 2004):** Texas Parks and Wildlife Department Game Warden boating accident reports for Lake Travis, August 2004. Under Texas Public Information Act.

---

## New Files Created

- `LOA13-SUMMARY.md` — This file
- `LOA13-RECOVERED-001.md` — DeSoto MO Nicholas Harbison case: St. Louis Post-Dispatch article reconstructed from Google Groups reproduction (March 20, 2006)

---

## Verification Status of Incidents Researched

| Incident | Location | Gap Year? | Victim Found? | Primary Source Found? |
|---------|---------|---------|-------------|---------------------|
| FI-1993-003 | Alexandria Bay NY | No (1993 not gap) | No | No |
| SUSP-2004-001 | Lake Travis TX | 2004 (gap) | No | No |
| FI-2006-XXX | DeSoto MO | No (2006 not gap) | YES: Nicholas Harbison, 16 | YES: St. Louis Post-Dispatch 3/20/2006 |
| FI-2004-XXX | Lake Waccamaw NC | 2004 (gap) | No | No |
| FI-2010-XXX | Lake Waccamaw NC | No (2010 not gap) | No | No |
| FI-2004-XXX | Lake Wylie NC | 2004 (gap) | No | No |
| FI-1999-003 | Multnomah Channel OR | No (1999 not gap) | YES: Lucas Ritz, 8 | YES: Multiple |

*Note: The term "gap year" above refers to gap years in the ESDPA list (1990, 1992, 1996, 2004, 2007, 2009). The DeSoto MO and Lake Waccamaw cases are not in gap years per se but are in underrepresented states/incidents.*
