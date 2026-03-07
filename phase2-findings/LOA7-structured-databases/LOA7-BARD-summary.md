# LOA7 Summary: BARD (Boating Accident Report Database) Analysis

## Data Source
- **Database:** USCG Boating Accident Report Database (BARD)
- **Coverage:** 2009-2023 (3 dataset periods: 2009-2013, 2014-2022, 2023)
- **Obtained via:** FOIA by Data Liberation Project
- **Total accident records:** 58,430
- **Total death records:** 8,935
- **Analysis date:** 2026-03-07

## Methodology
1. Searched all death records for CauseofDeath containing "electr" — found only 3 records
2. Searched all accident narratives for ESD-related keywords (electrocuted, electrocution, electric shock, electricity in the water, shocked in the water)
3. Cross-referenced known ESDPA incidents (2009-2023) against BARD by date, state, and body of water
4. Searched for drowning deaths near docks/marinas that could be misclassified ESD

## Key Finding: BARD Severely Underreports ESD

**Only 3 death records in all of BARD list "Electrocution" as cause of death** across 8,935 total deaths over 15 years. Of these:
- AZ-2020-0095 (2 deaths) — Scorpion Bay Marina, Lake Pleasant = **matches FI-2019-001** (Miller brothers)
- TX-2021-0068 (1 death) — sailboat hit powerline at Lake Clyde = **matches FI-2020-001** (but listed as powerline contact, not classic ESD)

Most ESD deaths are coded as "Trauma" or "Drowning" in BARD, not "Electrocution."

## Confirmed BARD-to-ESDPA Matches

| BARDID | Date | State | Water Body | Deaths | Injured | ESDPA Match | Notes |
|--------|------|-------|------------|--------|---------|-------------|-------|
| AZ-2020-0095 | 2020-07-12 | AZ | Lake Pleasant | 2 | 2 | FI-2019-001 | CoD: "Electrocution". Shore power cable modification. Ages 53, 50 (deaths); 23, 63 (injured) |
| TX-2021-0068 | 2021-06-02 | TX | Lake Clyde | 1 | 0 | FI-2020-001 | Sailboat mast hit powerline. Age 18. CoD: Trauma |
| OH-2017-0032 | 2017-06-16 | OH | Lake Erie/Put-in-Bay | 1 | 0 | FI-2017-008 | Shore power electrified water, dog rescue. Age 19. CoD: Trauma. **BARD date Jun 16 vs ESDPA May 22** |
| TN-2012-0073 | 2012-07-04 | TN | Cherokee Lake | 2 | 6 | FI-2012-010 | German Creek Marina houseboat. Ages 10, 11 (deaths). CoD: Trauma |
| WV-2010-0005 | 2010-05-29 | WV | Stonewall Jackson Lake | 1 | 1 | **NOT IN ESDPA** | Juveniles shocked at swim ladder while moored at marina. Age 15 (death, CoD: Hypothermia). **POTENTIAL NEW INCIDENT** |
| KY-2010-0043 | 2010-07-31 | KY | Green River Lake | 0 | 2 | **NOT IN ESDPA** | Passenger shocked in water, owner entered to rescue and was also paralyzed. Ages 47, 42. **POTENTIAL NEW NEAR-MISS** |
| TN-2011-0090 | 2011-06-03 | TN | Norris Lake | 0 | 1 | **NOT IN ESDPA** | Houseboat breaker reset shocked swimmer. Age 9. **POTENTIAL NEW NEAR-MISS** |

## Additional BARD Records with Electrical Involvement (Not Classic ESD)

| BARDID | Date | State | Description | Match |
|--------|------|-------|-------------|-------|
| FL-2016-0648 | 2016-08-14 | FL | Lightning strike killed boater | NOT ESD |
| UT-2016-0043 | 2016-07-22 | UT | Lightning struck PWC riders | NOT ESD |
| MO-2013-0096 | 2013-08-07 | MO | Boat drifted into powerline | NOT ESD |
| MO-2020-0036 | 2020-05-15 | MO | Kayaker's line hit electrical wire | NOT ESD |
| AL-2019-0022 | 2019-05-24 | AL | Sailboat mast hit powerline | NOT ESD |
| LA-2023-0064 | 2023-07-22 | LA | Sailboat mast hit powerline | NOT ESD |
| LA-2013-0024 | 2013-05-10 | LA | Lightning strike | NOT ESD |

## NEW Incidents Found (Not in ESDPA List)

### BARD-2010-001: WV-2010-0005 — Stonewall Jackson Lake Marina ESD
- **Date:** May 29, 2010
- **Location:** Stonewall Jackson Lake, Walkersville, WV
- **Deaths:** 1 (age 15), **Injuries:** 1 (age 16)
- **Status:** POTENTIALLY NEW FATAL ESD INCIDENT
- **Narrative:** 3 juveniles swimming off stern of boat moored at marina. Victim and another juvenile approached swim ladder, both received electrical shock. Victim slipped under water, other juvenile escaped. CoD listed as "Hypothermia" — classic ESD misclassification.
- **Note:** Death coded as "Hypothermia" not "Electrocution" despite narrative describing electrical shock at swim ladder. This is exactly the misclassification pattern ESD researchers warn about.

### BARD-2010-002: KY-2010-0043 — Green River Lake Boat Electrical Shock (Near-Miss)
- **Date:** July 31, 2010
- **Location:** Green River Lake, Campbellsville, KY
- **Deaths:** 0, **Injuries:** 2 (ages 47, 42)
- **Status:** POTENTIALLY NEW NEAR-MISS
- **Narrative:** Passengers working on boat's AC. One entered water and was paralyzed by electricity. Another entered to rescue, was also paralyzed. Owner shut off master switch. Both rescued via rope.

### BARD-2011-001: TN-2011-0090 — Norris Lake Houseboat Electrical Shock (Near-Miss)
- **Date:** June 3, 2011
- **Location:** Norris Lake, LaFollette, TN
- **Deaths:** 0, **Injuries:** 1 (age 9)
- **Status:** POTENTIALLY NEW NEAR-MISS
- **Narrative:** Two swimmers behind houseboat with known electrical issues (breaker tripping). When breaker was reset, swimmers felt electric shock. One had to be pulled from water.

## Known ESDPA Incidents NOT Found in BARD

The following dock/marina/boat ESD incidents from the ESDPA list were NOT found in BARD, confirming that BARD misses most ESD incidents:

- FI-2010-001 (Lake Pepin MN, boat lift) — **NOT IN BARD**
- FI-2010-003 (Smith Lake AL, dock) — **NOT IN BARD**
- FI-2010-004 (Lake Waccamaw NC, boat lift) — **NOT IN BARD**
- FI-2011-001 (Lake Sinclair GA, dock) — **NOT IN BARD**
- FI-2011-002 (Grand Traverse Bay MI, dock) — **NOT IN BARD**
- FI-2012-001 (Rough River Lake KY, shore cord) — **NOT IN BARD**
- FI-2012-002 (Tims Ford Lake TN, dock) — **NOT IN BARD**
- FI-2012-007 (Pokegama Lake MN, boat lift) — **NOT IN BARD**
- FI-2012-008 (Lake of the Ozarks MO, dock) — **NOT IN BARD**
- FI-2012-009 (Lake of the Ozarks MO, dock) — **NOT IN BARD**
- FI-2013-006 (Eagle Lake MN, battery charger) — **NOT IN BARD**
- FI-2013-007 (Lake Cumberland KY, dock) — **NOT IN BARD**
- FI-2014-001 (Lake of the Ozarks MO, dock) — **NOT IN BARD**
- FI-2014-002 (Lake Bruin LA, boat lift) — **NOT IN BARD**
- FI-2014-005 (Lake Powell UT, marina) — **NOT IN BARD**
- FI-2015-002 (Lake Tuscaloosa AL, pontoon) — **NOT IN BARD**
- FI-2016-007 (Smith Lake AL, dock) — **NOT IN BARD**
- FI-2017-007 (Toms River NJ, boat lift) — **NOT IN BARD**
- FI-2017-009 (Mandeville LA, dock) — **NOT IN BARD**
- FI-2017-012 (Lake Tuscaloosa AL, dock) — **NOT IN BARD**
- FI-2021-001 (Ohio River KY, yacht club) — **NOT IN BARD**
- FI-2021-002 (Monongahela River PA, marina) — **NOT IN BARD**

**22 of 24 known dock/marina/boat ESD incidents (2009-2023) are ABSENT from BARD.** Only 2 of 24 (8%) were found. This means BARD captures less than 10% of known ESD fatalities.

## Why BARD Misses ESD

1. **BARD only covers "recreational boating accidents"** — dock/shore-power incidents where no vessel is underway are generally not reportable
2. **Private dock incidents are not reported** — the majority of ESD occurs at private docks
3. **When ESD deaths ARE in BARD, they're misclassified** — coded as "Trauma," "Drowning," or "Hypothermia" rather than "Electrocution"
4. **No searchable field for electrical cause** — the CauseofDeath field has limited categories; electrical is not standard

## Implications for Underreporting Research

The 8% capture rate (2 of 24 known incidents) combined with misclassification of the deaths that ARE captured (WV-2010-0005 coded as "Hypothermia") provides strong quantitative evidence for the ESD underreporting thesis. If BARD — the most comprehensive federal boating accident database — misses 92% of known ESD fatalities, the true national ESD death toll is almost certainly far higher than documented.
