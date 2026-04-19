---
batch_id: SUSP-BATCH-2026-04-18
generated: 2026-04-18
updated: 2026-04-18 (added pass 2: electrical/inspection queries → +2 candidates)
method: Perplexity web search + Brave fallback, Section 4 red-flag terms + electrical-inspection phrasing
query_count: 34
raw_hits_reviewed: ~200
candidates_extracted: 9
already_in_dataset: 23
intended_destination: /opt/repos/esd-research/phase2-findings/LOA1-news-archive/SUSP-BATCH-2026-04-18.md
note: Target directory was read-only for my user (owned by devuser, mode 755); written to drafts/ for human to relocate after review.
---

# Suspected ESD candidates — batched red-flag search, 2026-04-18

## Summary

Ran 24 planned Section-4 red-flag / geographic-gap queries plus 2 targeted follow-ups against Perplexity. The vast majority of hits returned either (a) incidents already in the dedup reference (Carmen Johnson, Jesse Hamric, Thomas Milner, Alec McQueen, Evan Currie, Gabriel Gonzalez, Kayla Matos, Donna Berger, Randy Freeney, Shelly Darling, Elizabeth Whipple, Dr. Eric Hughes, Marcus Colburn, Timothy/Michael Miller, Alexandra/Brayden Anderson, Noah Winstead/Nate Lynam, Lucas Ritz, Michael Knudsen, Jason Mertz) or (b) well-known safety-advocacy boilerplate. Seven new candidates for human follow-up were extracted; most are low/medium confidence "suspected misclassified drowning" cases rather than confirmed ESD. The highest-confidence new lead is a 2018 Lake Lanier Holiday Marina dock fall that fits the classic ESD pattern at a marina with two subsequent confirmed/suspected ESD fatalities.

## Candidate list

### SUSP-BATCH-001: Teresa Ann Graham — Lake Lanier (Holiday Marina, Dock Q), Hall County, GA — 2018-07-17
- **Location:** Lake Lanier, Holiday Marina, Dock Q, Hall County, GA
- **Date:** 2018-07-17 (exact)
- **Victim:** Teresa Ann Graham, 51, female
- **Outcome:** fatal (single)
- **Red flags present:**
  - Fell from/went off a marina dock directly; no witnessed drowning event
  - Victim's group was staying on a boat at the marina (boat + shore power present)
  - Holiday Marina is the same marina associated with the 2023 Thomas Milner ESD death and the 2023 Whitlock dock fall
  - Found by husband + witness within minutes — no struggle reported
- **ESD fit confidence:** medium
- **Source:** AJC — https://www.ajc.com/news/local/suspected-drowning-victim-fell-off-dock-into-lake-lanier-sheriff-says/nzBlWapEwJ08XESyeDhJ4L/
- **Dedup check:** Not in dataset (no "Graham" in names; Lake Lanier location entries are 2006, 2013, 2023 only).
- **Follow-up needed:** Pull Hall County Coroner / GBI autopsy; check if any shore-power or GFCI findings were documented; contact Holiday Marina for electrical inspection records. The recurrence of fatalities at this specific marina elevates prior probability.
- **Reasoning:** Sudden, unwitnessed disappearance from a commercial marina dock where a later confirmed ESD fatality (Milner 2023) occurred at the same facility fits the canonical "silent" ESD pattern. Victim was walking down the dock, not swimming recreationally — but proximity to shore-power pedestals and her body being pulled from water directly at the dock make this a high-priority misclassified-drowning candidate.

### SUSP-BATCH-002: Charles William Crowe Jr. (+ unnamed female, injured) — Lake Norman, Iredell County, NC — 2025-06-14
- **Location:** Lake Norman, Main Channel Marker 20, Iredell County, NC
- **Date:** 2025-06-14 (exact)
- **Victim:** Charles W. Crowe Jr., 63, male (fatal); unnamed adult female (non-fatal, medical treatment)
- **Outcome:** fatal + near-miss (multi-victim)
- **Red flags present:**
  - Multi-victim: Crowe got into water and "started experiencing physical issues"; female jumped in to help and "started having health issues as well"
  - Rescuer-affected pattern (a core ESD flag)
  - WCNC update indicates he "got off a boat to get something that fell into the water" — same pattern as Gabriel Gonzalez 2025 ESD (Portage, IN) who retrieved a floating object
- **ESD fit confidence:** medium
- **Source:** WHKY — https://whky.com/update-released-on-drowning-catawba-county-man-identified-as-victim/ ; WCCB — https://www.wccbcharlotte.com/2025/06/17/lake-norman-drowning-victim-identified/
- **Dedup check:** Not in dataset. Lake Norman not in locs list for 2025.
- **Follow-up needed:** Pull NC Wildlife Resources Commission investigation file; check if boat was plugged into shore power (from a marina? or free-drifting? — news says "Main Channel Marker 20"); get the woman's statement about any tingling/shock sensation; coroner's cause of death.
- **Reasoning:** Two people entering water and both experiencing "physical issues" — one fatal, one requiring medical treatment — is a classic ESD signature. The parallel to the confirmed Gonzalez 2025 case (same pattern: man enters water to retrieve object, dies; rescuer also shocked) is striking. Needs investigation to rule in or out.

### SUSP-BATCH-003: Patrick Byrnes — Lake Anna, Louisa County, VA — 2020-08-01
- **Location:** Lake Anna, Old Mill Road area, Louisa County, VA
- **Date:** 2020-08-01 (exact; reported 2020-08-02)
- **Victim:** Patrick Byrnes, 21, male, of Vienna, VA
- **Outcome:** fatal (single)
- **Red flags present:**
  - Media explicitly described as a "strong swimmer"
  - Last seen swimming out to a floating chair ~20 ft from end of a private dock
  - Disappeared without apparent distress warning
- **ESD fit confidence:** low-medium
- **Source:** WTVR CBS6 — https://www.wtvr.com/news/local-news/patrick-byrnes-dead-drowning-lake-anna
- **Dedup check:** Not in dataset (no Byrnes in names). Lake Anna is not in locs list at all.
- **Follow-up needed:** Check Louisa County ME autopsy for unusual findings; determine whether the private dock had shore power / boat lift. Note that Lake Anna Civic Association has recently issued ESD safety bulletins, suggesting known ESD-adjacent risk on this lake.
- **Reasoning:** Strong-swimmer-drowns-feet-from-dock is the textbook red-flag pattern. Absent an electrical investigation at the time, this case fits the "misclassified drowning" hypothesis. The Lake Anna Civic Association's 2024 newsletter explicitly discusses ESD as an underappreciated cause on this lake, increasing prior probability.

### SUSP-BATCH-004: Gavrie Alexander Whitlock — Lake Lanier (near Holiday Marina), GA — 2023-09-02
- **Location:** Lake Lanier, near Holiday Marina, south end near Lanier Islands, GA
- **Date:** 2023-09-02 (exact)
- **Victim:** Gavrie Alexander Whitlock, 23, male, of Snellville, GA
- **Outcome:** fatal (single)
- **Red flags present:**
  - "Running down a dock when he slipped and fell into the water... never resurfaced"
  - Same Holiday Marina area as Milner 2023 ESD fatality (~5 weeks earlier) and Graham 2018 fatality
  - Young, presumably healthy adult — no reported distress or struggle
- **ESD fit confidence:** medium
- **Source:** Macon Telegraph — https://www.macon.com/news/state/georgia/article278944484.html
- **Dedup check:** Not in dataset. Lake Lanier | Lake Lanier, GA | 2023 location entry is for Milner (July 2023); this is a separate September 2023 incident.
- **Follow-up needed:** Pull Hall County / Forsyth County dive-recovery report; verify proximity to Holiday Marina's shore-power pedestals; get DNR investigative file. Was Holiday Marina's electrical system inspected after the July 2023 Milner death?
- **Reasoning:** Three separate fatal incidents (2018 Graham, July 2023 Milner, September 2023 Whitlock) at the same marina within 5 years is statistically anomalous. Whitlock "never resurfaced" is classic for sudden incapacitation (paralysis from electric shock or cardiac arrest). Body was in 17 feet of water — shallow enough for dock-wiring fault field.

### SUSP-BATCH-005: Keane "Art" Kolodzinski — Lake Pleasant, AZ — 2025-07-06
- **Location:** Lake Pleasant, near South Barker Island, Peoria, AZ
- **Date:** 2025-07-06 (approx; body located 2025-07-10)
- **Victim:** Keane "Art" Kolodzinski, 72, male; described as "avid boater and strong swimmer"
- **Outcome:** fatal (single)
- **Red flags present:**
  - Described by family as "strong swimmer" and "shocked how this happened"
  - Was trying to swim back to his boat when he went under yelling for help
  - Lake Pleasant is the exact site of the confirmed 2020 Miller brothers ESD (Scorpion Bay Marina)
- **ESD fit confidence:** low-medium
- **Source:** YouTube news segment — https://www.youtube.com/watch?v=j7NyZZIWNIA
- **Dedup check:** Not in dataset (no Kolodzinski in names). Lake Pleasant | Peoria, AZ | 2020 is in locs (Miller brothers incident).
- **Follow-up needed:** Find local print news coverage; determine whether his boat was plugged into shore power at a marina or free-anchored; pull MCSO report and Maricopa County ME autopsy.
- **Reasoning:** Strong-swimmer-calls-for-help-then-disappears at a lake with prior confirmed ESD history (Miller brothers 2020) is a suspected ESD candidate. Distance to South Barker Island makes marina-shore-power less likely, but an energized boat in an adjacent slip could still be a source if he was near a moored vessel.

### SUSP-BATCH-006: Isaac Mwungura — Nolin Lake, Edmonson County, KY — 2024-07-24
- **Location:** Nolin Lake, private dock at 310 Twin Oaks Drive, off Dickey's Mill Road, Edmonson County, KY
- **Date:** 2024-07-24 (exact)
- **Victim:** Isaac Mwungura, 18, male, of Kenya (Louisville-area student)
- **Outcome:** fatal (single)
- **Red flags present:**
  - Body was found *under the dock*
  - Belongings found on the dock (suggesting he entered water from it)
  - Gone unnoticed for ~2 hours — classic silent-ESD pattern where no one observes a struggle
  - Private lake dock context
- **ESD fit confidence:** low
- **Source:** Edmonson Voice — https://www.edmonsonvoice.com/-news/teen-drowning-at-nolin-lake
- **Dedup check:** Not in dataset (no Mwungura in names; no Nolin Lake in locs).
- **Follow-up needed:** Check Edmonson County coroner report for electrical contact marks; inspect the specific dock's wiring. Witnesses said he was "not a strong swimmer" which weakens the ESD-fit — this is primarily a "body under dock, belongings on dock" triage flag.
- **Reasoning:** Counts explicitly against strong-swimmer pattern (witnesses said he was NOT a strong swimmer), which lowers fit. Included as low-confidence because of the "body under the dock" geometry and silent-disappearance pattern. Primarily worth following up because 18yo, private dock, no splash/witness — but non-ESD causes (simple drowning, footing loss) are also plausible.

### SUSP-BATCH-007: Unnamed adult male — Sam Rayburn Reservoir, Umphrey Pavilion dock, Jasper County, TX — 2025-11-09
- **Location:** Umphrey Pavilion, Lake Sam Rayburn, Jasper County, TX
- **Date:** 2025-11-09 (approx; reported in Nov 2025 news)
- **Victim:** Unnamed adult male; was fishing with wife
- **Outcome:** fatal (single)
- **Red flags present:**
  - Was on a dock ("Umphrey Pavilion dock") when "began coughing, lost consciousness, and fell in"
  - Wife jumped in to try to save him (rescuer involved)
  - Loss of consciousness on dock before falling in is atypical of simple drowning
- **ESD fit confidence:** low
- **Source:** Local TX news YouTube — https://www.youtube.com/watch?v=PD4MuFb0I_Y
- **Dedup check:** Not in dataset (no Sam Rayburn in locs).
- **Follow-up needed:** Identify victim; pull Jasper County ME report; check whether the pavilion had exposed wiring / electrical fixtures the victim may have touched. "Coughing + unconsciousness + falling in" could be cardiac, stroke, or electrical contact.
- **Reasoning:** Low fit because the triggering event was ON the dock (coughing + LOC), not in the water, and the most common explanation is a cardiac event. However, sudden LOC on a dock adjacent to electrical equipment is also an ESD/contact-shock pattern. Texas is a known geographic gap per research-summary.md, so worth a follow-up keyword search.

### SUSP-BATCH-008: Two unnamed swimmers — Lake Cowichan, BC, Canada — 2018-05-26
- **Location:** Lake Cowichan, Vancouver Island, British Columbia, Canada
- **Date:** 2018-05-26 (exact; per Technical Safety BC report)
- **Victims:** Two swimmers (names not in regulatory report — need local news follow-up)
- **Outcome:** near-miss (multi-victim) — both incapacitated by electric shock, no fatalities
- **Red flags present:**
  - Two swimmers jumped from houseboat, both simultaneously shocked
  - Official Technical Safety BC regulatory investigation confirmed electrical cause
  - Damaged non-metallic sheathed cable shorted to metal device box on houseboat
  - Lack of GFCI protection
  - Unusual mechanism: return path was through neighbor's dock steel cable → guy-wire anchor → neighbor's service ground electrode to the common transformer
- **ESD fit confidence:** **high** (regulatory-confirmed)
- **Source:** Technical Safety BC — https://www.technicalsafetybc.ca/regulatory-resources/incident-investigations/faulty-wiring-energizes-houseboat-exposes-swimmers-electric-shock
- **Dedup check:** Not in dataset; Canadian cases are systemically underrepresented.
- **Follow-up needed:** Canadian news coverage for victim names/ages (try Cowichan Valley Citizen, CBC BC, Times Colonist). File is a primary regulatory document — highest evidentiary quality of any candidate in this batch.
- **Reasoning:** Confirmed-mechanism ESD near-miss in an official Canadian regulatory investigation database. The shared-ground-path-through-neighbor's-dock mechanism is a notable technical variant worth capturing in the dataset independent of whether victims are named.

### SUSP-BATCH-009: Unknown adult male diver — Bull Shoals Lake, AR — pre-2004 (date unknown)
- **Location:** Bull Shoals Lake, Bull Shoals, AR (Marion/Baxter County)
- **Date:** unknown, pre-2004 (documented on Kevin Ritz / Harbor Marine Consultants June 2004 ESD incident list)
- **Victim:** adult male diver (not named in available sources)
- **Outcome:** fatal
- **Red flags present:**
  - Diver found drowned 8 ft from his dock in shallow water
  - **Rescue diver reported feeling shock 20 ft from the dock** — textbook multi-witness ESD
  - **117 VAC measured on metal dock components** after incident
  - Cause confirmed: incorrectly wired dock junction box
- **ESD fit confidence:** **high** (confirmed mechanism in a technical-source incident list)
- **Source:** Harbor Marine Consultants ESD Incident List, June 2004 — https://www.mikeholt.com/documents/mojofiles/DrowningsAtMarina.pdf
- **Dedup check:** Not in dataset. Arkansas has 4 listed incidents (Lake Hamilton 1991/2001/2008, Lake Ouachita 2006); Bull Shoals Lake is not represented.
- **Follow-up needed:** Research primary news coverage to find victim name, exact date (likely 1990s–early 2000s). Try local papers: *Baxter Bulletin*, *Harrison Daily Times*. Coroner records for Marion or Baxter County AR. This is a documented confirmed-ESD that has been missing from the ESDPA-derived list.
- **Reasoning:** Harbor Marine Consultants is the technical source behind many ESDPA-listed incidents; inclusion on their list with measured voltage = confirmed ESD. The absence of this case from the main list is a gap, not an exclusion decision.

## Queries that returned no new candidates

The following queries produced only already-catalogued incidents (or advocacy/educational content without a specific new case):

- `"felt shock" drowning dock marina lake` → Carmen Johnson, Thomas Milner, Jesse Hamric, Michael Knudsen (all in dataset)
- `"tingling in water" drowning dock lake` → only educational/safety pages
- `"paralyzed in water" drowning dock` → dupes (ESDPA list, Bull Shoals, Carmen Johnson)
- `"couldn't move" drowning dock lake` → Christopher Gilbert Louisiana (non-ESD, pushed in), Cabin Lake BC (cold-water, non-ESD)
- `"exceptional swimmer" drowning dock marina` → Donna Berger / Randy Freeney (both already in dataset)
- `"no water in lungs" drowning dock lake` → only medical-education content on dry drowning
- `"two drowned" dock lake electrocution` → Timothy & Michael Miller Lake Pleasant (dataset); Cherokee Lake boys (dataset); Lake of the Ozarks (dataset)
- `"double drowning" marina lake electrocution` → ESDPA list repeats only
- `"father drowned" rescuing child dock lake` → Christopher Schultz (bridge, no dock electricity); Lake Pueblo 2025 (cold water, children); James Everard Whitmore Lake (boat accident, no dock)
- `"jumped in to save" drowned dock lake` → Christopher Gilbert (non-ESD); Silver Lake 13yo hero (non-fatal, non-ESD); mostly non-ESD rescues
- `"initially ruled drowning" electrocution dock` → re-describes Milner, Carmen Johnson, Darling/Whipple (all dataset)
- `"death certificate amended" drowning electrocution` → Lucas Ritz 1999 (already in dataset)
- `"GFCI tested" after drowning dock marina` → Andrew Orvis Lake Conroe 2014 (already in dataset: Piney Shores)
- `"stray voltage" drowning lake dock` → Jesse Hamric Smith Mountain Lake (dataset); Donald Johnson EC&M case study is already documented
- `"electrocuted" drowning "Lake Travis" dock Texas` → Lake Travis 2004 suspected case (ESDPA list); 2016 Annabelle Cooper (non-ESD toddler); 2024 scooter drowning (no dock)
- `"electrocuted" drowning "Lake Conroe" OR "Lake Texoma" dock Texas` → Andrew Orvis 2014 (dataset), Margaritaville 2021 contractor electrocution (workplace, not ESD); Sam Rayburn unnamed extracted to #007
- `"electrocuted" drowning "Lake Norman" OR "Lake Wylie" NC dock` → Crowe extracted to #002; others unrelated drownings
- `"electrocuted" drowning Lake Washington OR Lake Union Pacific Northwest dock` → Lake Washington Kirkland 2016 suicide/accident (weak fit); Lucas Ritz Willamette already in dataset
- `"electrocuted" drowning "Lake Minnetonka" Minnesota dock` → Dan Peterson Big Lake 2013 (already in dataset as Daniel Petersen); Shorewood 2025 burn-body case is suicide
- `"electrocuted" drowning Lake Champlain OR Finger Lakes dock` → only generic ESDPA list content; no specific unlisted NY/Vermont incidents
- `"electrocuted" drowning Lake Havasu OR Lake Mead marina dock` → Lake Mead 1997 and Lake Mohave entries already on ESDPA historical list; no new cases
- `"electrocuted" drowning dock Oregon OR Washington OR Idaho lake` → Lucas Ritz Willamette (dataset); Smith Mountain Lake repeats
- Hebron/Portage IN marina search → Gabriel Gonzalez (dataset)
- Prospect Yacht Club Louisville 2022 diver → dataset
- Put-in-Bay / Lake Erie Miller Marina → Evan Currie / Jeffrey Currie (dataset)
- Lake Powell Bullfrog 2014 → Alec McQueen (dataset)
- Blue Ridge Lake Fannin 2025 13yo → already in dataset as ESD-2025-06-21-1
- Tracy Stewart Lake Lanier 2023 → non-ESD context (no life jacket, mid-lake boat jump)
- `"electric shock" swimmer drowned lake dock 2024 2025 news` → Milner, Hamric, Gonzalez all in dataset

### Pass 2 (2026-04-18): electrical / electrician + inspected / inspection

Added 8 queries combining drowning with electrical-inspection phrasing. Results heavily dominated by (a) advocacy PDFs (BoatUS, ESFI, MN ESD association) we had already mined, and (b) already-in-dataset incidents where an electrical inspection was part of the reported investigation. Two new candidates surfaced (SUSP-BATCH-008, SUSP-BATCH-009 above).

- `drowning "electrical inspection" dock lake` → Carmen Johnson; Smith Mountain Lake dock-code article (Hamric); Lake Lanier Stoddard firm on Milner — all dataset
- `drowned "electrician inspected" dock marina` → dataset repeats + generic ESDPA/BoatUS content
- `drowning "electrical issue" inspection dock lake` → Hamric (SML), Anderson (LotO lawmakers article), Milner (Lake Lanier) — all dataset
- `"nearly drowned" "electrical" "inspected" dock lake` → generic dataset repeats only
- `drowning lake "electrician was called" OR "electrician found" dock` → dataset repeats; Herby Fitzgerald James River 1993 rescue (non-ESD)
- `"dock was inspected" drowning death electrical fault lake` → SML Broughton piece (Hamric), Carmen Johnson repeats
- `drowned "electrical problem" OR "electrical fault" investigation inspection lake` → **Lake Cowichan BC 2018 (new — #008)**; Miller brothers Lake Pleasant (dataset); Raleigh pool pump (dataset)
- `lake drowning "inspector found" electrical dock wiring` → AuGres list + Ritz PDF repeats, from which **Bull Shoals AR (new — #009)** was extracted; Park Township MI 1988 (dataset), Stonewall Jackson WV 2010 (dataset), Lake of the Ozarks 2007 24F (dataset)

## Query performance

| # | Query | Hits | Candidates | Notes |
|---|-------|------|------------|-------|
| 1 | "felt shock" drowning dock marina lake | 6 | 0 | All existing cases |
| 2 | "tingling in water" drowning dock lake | 6 | 0 | Education/advocacy only |
| 3 | "paralyzed in water" drowning dock | 6 | 0 | ESDPA list repeats |
| 4 | "couldn't move" drowning dock lake | 6 | 0 | Non-ESD rescues |
| 5 | "strong swimmer" drowned dock unexplained lake | 6 | 2 | Byrnes (#003), Kolodzinski (#005) |
| 6 | "exceptional swimmer" drowning dock marina | 6 | 0 | Berger/Freeney in dataset |
| 7 | "no water in lungs" drowning dock lake | 6 | 0 | Medical content only |
| 8 | "two drowned" dock lake electrocution | 6 | 0 | All dataset |
| 9 | "double drowning" marina lake electrocution | 6 | 0 | ESDPA repeats |
| 10 | "father drowned" rescuing child dock lake | 6 | 0 | Non-ESD rescues |
| 11 | "jumped in to save" drowned dock lake | 6 | 0 | Non-ESD |
| 12 | "unexplained drowning" marina dock lake | 6 | 2 | Graham (#001), Whitlock (#004) |
| 13 | "initially ruled drowning" electrocution dock | 6 | 0 | Dataset |
| 14 | "death certificate amended" drowning electrocution | 6 | 0 | Lucas Ritz only |
| 15 | "GFCI tested" after drowning dock marina | 6 | 0 | Orvis in dataset |
| 16 | "stray voltage" drowning lake dock | 6 | 0 | Hamric in dataset |
| 17 | Lake Travis electrocution dock | 6 | 0 | Historical only |
| 18 | Lake Conroe/Texoma electrocution | 6 | 1 | Sam Rayburn unnamed (#007) |
| 19 | Lake Norman/Wylie electrocution | 6 | 1 | Crowe (#002) |
| 20 | Lake Washington/Union electrocution | 6 | 0 | None new |
| 21 | Lake Minnetonka electrocution | 6 | 0 | Petersen in dataset |
| 22 | Lake Champlain/Finger Lakes electrocution | 6 | 0 | No new NY/VT specifics |
| 23 | Lake Havasu/Mead electrocution | 6 | 0 | Historical |
| 24 | Oregon/Washington/Idaho electrocution | 6 | 0 | Lucas Ritz only |
| 25 | (follow-up) strong swimmer 2024-2025 lake family | 6 | 0 | Non-ESD drownings |
| 26 | (follow-up) Lake Norman Crowe 2025 | 4 | 0 | Crowe already extracted |

## Notes for reviewers

- No dedicated search query for "Mwungura / Nolin Lake" — it surfaced incidentally during the "strong swimmer" query (ironically, victim was described as NOT a strong swimmer); included as low-confidence triage.
- The Holiday Marina (Lake Lanier) cluster (2018 Graham, 2023 Milner, 2023 Whitlock) is worth a dedicated follow-up investigation even if the new candidates here individually score only medium.
- Perplexity did not return errors on any query; Brave fallback was not needed.
- Output files placed in `drafts/` because `phase2-findings/LOA1-news-archive/` is not writable by my user.
