# LOA5-B Summary: Engineering, Standards, and Industry Publications on Electric Shock Drowning

**Task**: Search electrical engineering, safety standards, and industry publications for research on Electric Shock Drowning (ESD), marina electrical safety, and dock electrical hazards.

**Search date**: 2026-03-07

**Files produced**: ACAD-020 through ACAD-039 (new LOA5-B entries); ACAD-051 and ACAD-052 (overflow, ACAD-040 through 050 were pre-existing LOA5-A files)

---

## Annotated Bibliography

### SECTION 1: PEER-REVIEWED ACADEMIC PAPERS

---

#### ACAD-020: Morse, Kotsch, Prussak, Kohl (2020) — IEEE Paper on ESD and Water Conductivity

**Full citation**: Michael S. Morse, Jesse Kotsch, Brandon Prussak, James G. Kohl. "Examining the Risk of Electric Shock Drowning (ESD) as a Function of Water Conductivity." *IEEE Transactions on Industry Applications*, Vol. 56, No. 4, pp. 4324–4328, July–August 2020. DOI: 10.1109/TIA.2020.2982854. (Conference version: *2019 IEEE IAS Electrical Safety Workshop*, DOI: 10.1109/ESW41045.2019.9024720.)

**Summary**: The primary peer-reviewed IEEE paper on ESD physics. Challenged the unexamined assumption that ESD is exclusively a freshwater hazard by modeling ESD risk as a function of water conductivity. Established that in freshwater, the human body is more conductive than the surrounding water, becoming the preferred current return path. In saltwater, high water conductivity disperses current through the water, greatly reducing body current. Used simulation to quantify the "zone of danger" around fault sources. Key finding: ESD risk is highest in low-conductivity fresh water but cannot be categorically dismissed in brackish or salt water at the margins.

**Relevance**: HIGH — Only IEEE peer-reviewed paper specifically on ESD physics.

---

#### ACAD-021: Linja-aho (2020) — IEEE Discussion Paper on ESD and Finnish Experience

**Full citation**: Vesa Linja-aho. "Discussion of 'Examining the Risk of Electric Shock Drowning (ESD) as a Function of Water Conductivity'." *IEEE Transactions on Industry Applications*, Vol. 56, No. 4, 2020. DOI: 10.1109/TIA.2020.3032949.

**Summary**: Response to Morse et al. analyzing 157 Finnish fatal electrical accidents (1980–2019) — finding zero ESD incidents despite abundant Finnish freshwater lakes and boating activity. Attributes the absence to mandatory European RCD (residual current device) requirements for shore power, in place for approximately 30 years. Demonstrates that ESD is preventable through mandatory 30 mA RCD/ELCI requirements. Key comparative policy finding: the US regulatory lag in requiring ELCI/RCD on boats and shore power is the primary reason ESD occurs in the US but not in European countries.

**Relevance**: HIGH — International comparative evidence for ESD preventability.

---

#### ACAD-022: Linja-aho (2020) — Fatal Electrical Accidents in Finland 1980–2019

**Full citation**: Vesa Linja-aho. "Fatal electrical accidents in Finland 1980–2019 — trends and reducing measures." *International Journal of Occupational and Environmental Safety (IJOOES)*, Vol. 4, No. 2, 2020. DOI: https://doi.org/10.24840/2184-0954_004.002_0004.

**Summary**: Full 40-year epidemiological study underlying the IEEE discussion paper. 157 fatal electrical accidents; zero ESD cases. Death rate declined from 0.29 per 100,000 to 0.00–0.07 per 100,000 corresponding to progressive adoption of mandatory RCDs. 37% of all fatalities could probably have been prevented with RCD protection. 76% of fatalities occurred April–September (warm weather), consistent with ESD seasonal patterns.

**Relevance**: HIGH — Empirical basis for the "mandatory RCDs eliminate ESD" argument.

---

#### ACAD-023: Koko, Ayyub, Gallant (2016) — ASME Simulation of ESD Scenarios

**Full citation**: Tamunoiyala S. Koko, Bilal M. Ayyub, Keith Gallant. "Simulation of Electric-Current-Induced Drowning Accident Scenarios for Boating Safety." *ASCE-ASME Journal of Risk and Uncertainty in Engineering Systems, Part B: Mechanical Engineering*, Vol. 2, No. 3, Article 031003, 2016. DOI: 10.1115/1.4032262.

**Summary**: First peer-reviewed computational simulation study of current distribution around fault-source boats. Modeled voltage gradients in water around boats with various fault types (battery charger, wiring failure, hull fault) in different water conductivities. Produced current density maps showing danger zones for swimmers at various distances from the hull. Established quantitative basis for the zone-of-danger concept.

**Relevance**: HIGH — First peer-reviewed simulation specifically modeling ESD hazard zones.

---

#### ACAD-024: Ayyub, Koko, Blair, Akpan (2016) — ASME Risk Assessment Methodology

**Full citation**: Bilal M. Ayyub, Tamunoiyala S. Koko, Andrew Nyakaana Blair, U.O. Akpan. "Risk Assessment Methodology for Electric-Current Induced Drowning Accidents." *ASCE-ASME Journal of Risk and Uncertainty in Engineering Systems, Part B: Mechanical Engineering*, Vol. 2, No. 3, Article 031004, 2016. DOI: 10.1115/1.4032308.

**Summary**: Companion paper to ACAD-023. Develops a formal probabilistic risk assessment methodology for ESD using fault trees and event trees. Identifies the three necessary conditions for ESD: (1) electrical fault on vessel or dock, (2) failed/absent GFP, (3) swimmer in energized water. Recommends mandatory GFP/GFCI, vessel leakage testing, no-swimming rules, and improved incident data collection.

**Relevance**: HIGH — Formal risk-assessment framework that informed NFPA FPRF Marina Risk Reduction project.

---

### SECTION 2: STANDARDS

---

#### ACAD-025: IEEE 1695-2016 — Guide to Understanding, Diagnosing, and Mitigating Stray and Contact Voltage

**Org**: IEEE Power and Energy Society. Chair: Chuck DeNardo. ISBN: 978-1-5044-0829-5. Approved January 29, 2016.

**Summary**: IEEE guide covering stray and contact voltage at publicly/privately accessible locations, explicitly including marinas and boat docks. Defines stray voltage (from normal operations, no fault) vs. contact voltage (from fault, requires repair). Provides measurement methodology using 500-ohm resistor to simulate human impedance. Recommends Contact Voltage Detection (CVD) programs for marina environments. Updated version (IEEE 1695-2024) in development with expanded case studies.

**Relevance**: MODERATE — Measurement methodology standard for marina voltage investigation.

---

#### ACAD-028: NFPA 303 — Fire Protection Standard for Marinas and Boatyards

**Org**: NFPA Technical Committee on Marinas. Editions: 2001, 2006, 2011, 2016, 2021, 2026.

**Key 2021 edition changes**: Mandatory AC ground-fault testing of ALL vessels at initial marina connection; vessels denied service if leakage exceeds 30 mA; retroactive applicability within 2 years; annual inspections required; leakage measurement devices where >3 shore power receptacles. Current thresholds: shore power receptacles ≤30 mA GFPE; feeders/branch circuits ≤100 mA GFPE; general receptacles Class A GFCI (4–6 mA).

**Relevance**: HIGH — Primary US marina operational safety standard.

---

#### ACAD-029: NEC Article 555 — Marinas, Boatyards, Floating Buildings, and Docking Facilities

**Org**: NFPA/NEC Technical Committee. Editions: 2011, 2014, 2017, 2020, 2023.

**Evolution summary**:
- 2011: GFPE introduced; 100 mA threshold (inadequate but first code requirement)
- 2014: Committee acknowledges 100 mA insufficient for children; debate begins
- 2017: Reduction to 30 mA for shore power receptacles; 100 mA feeders; critical breakthrough
- 2020: Complete restructuring; tiered approach codified; leakage measurement devices required
- 2023: Section 555.36 added — pre-connection vessel testing; marinas must deny non-compliant vessels

**Incidents that drove changes**: Lucas Ritz (1999); Noah Winstead and Nathan Lynam (July 4, 2012, Cherokee Lake, TN); 2012 Independence Day cluster.

**Relevance**: HIGH — Primary US electrical installation code for marina environments.

---

#### ACAD-030: ABYC E-11 — AC and DC Electrical Systems on Boats

**Org**: American Boat and Yacht Council. Periodically updated; major ELCI addition ~2012–2016.

**Key provisions**: ELCI required at shore power inlet; trip at ≤30 mA within ≤100 ms; individual GFCI at galleys, heads, machinery, weather decks; isolation transformer permitted as alternative; detailed AC grounding requirements. European comparison: mandatory RCD for shore power in Europe for ~30 years; ESD essentially unknown there.

**Relevance**: HIGH — Primary standard for vessel-side ESD protection (ELCI requirement).

---

### SECTION 3: GOVERNMENT REPORTS

---

#### ACAD-026: Shafer and Rifkin (2008) — USCG Grant Report on In-Water Shock Hazard Mitigation

**Authors**: James D. Shafer and Capt. David E. Rifkin, USN (Ret.), Society of Accredited Marine Surveyors. USCG FY2006 Grant, final report October 1, 2008.

**Summary**: Foundational government-funded engineering study. Controlled field testing using variac to inject calibrated fault currents through vessels' bonding systems into water across multiple sites with varying freshwater conductivity. Key finding: freshwater's high resistivity makes the swimmer's body the preferred current path. Recommendations: ELCI (30 mA, 100 ms) at shore power inlet; individual GFCI on galleys/heads/machinery; proper bonding per ABYC E-11; no swimming near powered boats. Directly informed ABYC E-11 revisions and NEC 2017 30 mA threshold.

**Relevance**: HIGH — Primary government-funded technical study on ESD; foundational for all subsequent standards work.

---

#### ACAD-027: Park and Meacham (2017) — NFPA FPRF Marina Risk Reduction Final Report

**Authors**: Woojung Park and Brian Meacham (principal investigators). Technical Panel: Ken Bush, Donny Cook, John Hall, Dean Hunter, Capt. David Rifkin. NFPA Fire Protection Research Foundation, August 11, 2017.

**Summary**: NFPA-commissioned risk reduction report. Develops ESD Concepts Tree (ESDCT) decision framework for risk evaluation across water environments. Applies socio-technical systems approach. Identifies critical research gaps in incident data, private dock exposure, inspection effectiveness. Recommends quantitative risk assessments and field validation of mitigation measures. Directly influenced NFPA 303 2021 edition vessel testing requirements.

**Relevance**: HIGH — Official NFPA research report that drove NFPA 303 2021 major revisions.

---

#### ACAD-052: State Legislation — ESD Prevention Acts (Tennessee, Missouri, West Virginia, Pennsylvania)

**Summary**: Tennessee's "Noah Dean and Nate Act" (2014, named for victims of July 4, 2012 Cherokee Lake fatalities): requires GFCIs, inspections every 5 years, warning signage. Missouri's "Alexandra and Brayden Anderson ESD Prevention Act" (SB 622, 2018): similar requirements. West Virginia: "Michael Cunningham Act." Pennsylvania: Legislation reintroduced 2025, not yet passed. No comprehensive federal legislation enacted as of 2026.

**Relevance**: HIGH — Direct regulatory consequence of specific ESD fatalities; maps named victims to legislation.

---

### SECTION 4: INDUSTRY ARTICLES AND TECHNICAL GUIDES

---

#### ACAD-031: Morse (2018) — "The Science Behind Electric Shock Drowning" (EC&M Magazine)

**Full citation**: M.S. Morse. "The Science Behind Electric Shock Drowning." *EC&M Magazine*, November 2018. URL: https://www.ecmweb.com/safety/shock-electrocution/article/20904099/the-science-behind-electric-shock-drowning

**Summary**: Industry-accessible companion to the 2020 IEEE paper. Uses finite element analysis to define the "Zone of Danger" — the spatial region where current density in water exceeds the swimmer incapacitation threshold. Demonstrates that voltage gradient per unit distance (V/ft), not just fault voltage, determines the hazard zone. Explains why fresh water creates wider danger zones than saltwater. Explains the drowning mechanism: at 5–12 mA, voluntary muscle control is lost; victim cannot swim or call for help; bystanders see unexplained submersion.

**Relevance**: HIGH — Definitive public-facing technical explanation of ESD physics using FEA.

---

#### ACAD-032: Domitrovich (2022) — "Safety in Marinas" (IAEI Magazine)

**Author**: Thomas A. Domitrovich, P.E., LEED AP. *IAEI Magazine*, July/August 2022. URL: https://iaeimagazine.org/electrical-fundamentals/safety-in-marinas-2/

**Summary**: Authoritative electrical inspector perspective tracing NEC Article 555 from 1968 to 2020. Explains why 100 mA threshold (2011) was insufficient. Documents the tiered 2020 NEC approach. References Lucas Ritz case. Emphasizes collaborative standards process driven by shared recognition that "lives were at stake."

**Relevance**: HIGH — Authoritative inspector perspective on NEC Article 555 regulatory history.

---

#### ACAD-033: Hunter (2025) — "History of Marina Ground-Fault Protection" (IAEI Magazine)

**Author**: Dean Hunter, Minnesota Department of Labor and Industry. *IAEI Magazine*, March 31, 2025. URL: https://iaeimagazine.org/electrical-safety/history-of-marina-ground-fault-protection/

**Summary**: First-person account of NEC Article 555 evolution from a standards committee participant. Documents: 2011 (100 mA, first GFP requirement); 2014 (committee acknowledgment of inadequacy for children); 2017 ("breakthrough" — 30 mA for shore power receptacles); 2020 (complete restructuring, tiered approach); 2023 (equipment replacement compliance; pre-connection vessel testing added for 2026).

**Relevance**: HIGH — Insider regulatory history from a standards committee participant.

---

#### ACAD-034: Dolan, Norton, Loftis (2018) — "Understanding AC Leakage Current" (AMI Technical Paper)

**Authors**: Dolan, Norton, Loftis (Maffett Loftis Engineering, LLC) for Association of Marina Industries, April 8, 2018. URL: https://marinaassociation.org/files/Dolan,%20Norton,%20Loftis%20-%20National%20Electrical%20Code%20Panel%20Understanding%20AC%20Leakage%20Current.pdf

**Summary**: Technical paper for NEC code panel deliberations. Key insight: fault current flowing through ground conductors does NOT trip dock receptacle GFP or boat ELCI protection — this explains many ESD incidents where protection devices were present but did not prevent the hazard. Documents leakage measurement methodology, current thresholds (perception: 0.5–2 mA; GFCI trip: 4–6 mA; let-go: 10–20 mA; NEC limit: 30 mA).

**Relevance**: HIGH — Contains the critical insight about ground-conductor fault current bypassing GFCI/ELCI.

---

#### ACAD-035: Coté (2019) — "How to Identify and Eliminate Stray Electrical Currents in Your Marina" (IMBC)

**Author**: James Coté. International Marina and Boatyard Conference (IMBC) 2019, published by Association of Marina Industries. URL: https://marinaassociation.org/files/James%20Cote%20IMBC%202019%20Stray%20Current%20Testing%2020190109%20final.pdf

**Summary**: Practical marina operator guide on AC (ESD hazard) and DC (corrosion) stray current testing protocols. Systematic testing procedure: check polarity, clamp-on milliammeter testing with circuit breakers on and off, energize boat loads circuit-by-circuit while monitoring. Critical finding: fault current through ground conductors evades standard GFCI/ELCI measurement — must test individual conductors to detect all fault paths.

**Relevance**: HIGH — Definitive practitioner testing protocol; complements ACAD-034 on detection limitations.

---

#### ACAD-036: Cavallaro and Johnson — EC&M Forensic Engineering Case Studies (2004, 2009, 2010)

**Authors**: John Cavallaro, P.E. (Forensic Engineering, Inc.); Donald R. Johnson, P.E. (Johnson Engineering). *EC&M Magazine*. eBook: https://www.ecmweb.com/e-books-library/whitepaper/20903470/electric-shock-drowning-the-truth-behind-the-tragedies

**Summary**: Three forensic case studies:
- "Hot Marina" (2004): Inadequate boat grounding energizes dock water
- "Stray Voltage in a Lake" (November 2009): Faulty utility concentric neutrals killed a teenage swimmer, injured two others with brain damage — notably a utility infrastructure fault, not marina wiring
- "Floating Dock" (July 2010): Fatal electrocution from severed ground wire and water intrusion in floating dock junction box

**Relevance**: HIGH — Engineering-verified forensic analyses of specific fatal incidents, including one involving utility infrastructure rather than marina wiring (expanding the ESD source typology).

---

#### ACAD-037: Boivin (2022) — "ESD in Swimming Pools: The Risks and Regulations" (IAEI Canada)

**Author**: Jean-Pierre Boivin, P. Eng., CSA Group. *IAEI Magazine*, July 1, 2022. URL: https://iaeimagazine.org/columns/canadian/electric-shock-drowning-in-swimming-pools-the-risks-and-regulations/

**Summary**: Canadian regulatory comparison for ESD in pools. CPSC data cited: 33 pool electrocution deaths, 33 injuries in US 2002–2018. Canadian CEC Rule 78-050 requires 5 mA Class A GFCI — more protective than US 30 mA GFPE threshold. IEC/NEC comparison shows Canada mandates more sensitive protection.

**Relevance**: MODERATE — Provides CPSC pool electrocution data and US-Canadian regulatory comparison.

---

#### ACAD-038: D'Antonio (2018) — "Electric Shock Drowning and Electrocution Prevention" (Waterway Explorer)

**Author**: Steve D'Antonio (Steve D'Antonio Marine Consulting). *Waterway Explorer Magazine*, 2018. URL: https://stevedmarineconsulting.com/wp-content/uploads/2014/03/DAntonio_WaterwayExplorerMag18.pdf

**Summary**: Technical and incident-documentation article for the boating community. Specifically documents the July 4, 2012 ESD cluster: Brayden Anderson (age 8) and Alexandra Anderson (age 13); Noah Winstead (age 10) and Nathan Lynam (age 11) at Cherokee Lake, TN; Jennifer Lankford (age 26). Also documents 2016–2017 Alabama incidents. Challenges the "ESD only in freshwater" myth.

**Relevance**: HIGH — Specific incident documentation with names, ages, dates, and locations for the 2012 Independence Day cluster; widely read in the boating community.

---

#### ACAD-039: Dalziel (1943–1972) — Foundational Electric Shock Physiology Research

**Author**: Charles F. Dalziel, University of California, Berkeley. "Electric Shock Hazard" *IEEE Spectrum*, February 1972; "Effect of Frequency on Let-Go Currents" (with Ogden, 1943); "Reevaluation of Lethal Electric Currents" (1968).

**Summary**: The experimental foundation for all electrical safety thresholds. Key findings: 1 mA (perception); 5 mA (muscle control interference — basis for Class A GFCI 5 mA threshold); 10–15.87 mA men / 10.5 mA women (let-go threshold); 100 mA (ventricular fibrillation). 60 Hz AC is among the most dangerous frequency bands. Based on human volunteer testing. Directly informed GFCI standard development; 1971 UL study (Smoot) calculated 81% of home electrocutions preventable with GFCIs.

**Relevance**: HIGH — Scientific foundation for all current thresholds in NEC Article 555, NFPA 303, and ABYC E-11.

---

#### ACAD-051: ABB (2021) — "Electric Shock in Presence of Water" Technical Guide

**Org**: ABB Ltd., Document 9AKK107992A4036, June 2021. URL: https://library.e.abb.com/public/1c1c63dc5cff4bb49588b471ebc8467a/ABB_Electric_Shock_in_Presence_of_Water_9AKK107992A4036.pdf

**Summary**: European/IEC perspective on water-environment electrical protection. Mandatory 30 mA RCDs (IEC 60364-7-701); recommends 10 mA for highest-risk zones. Explains "contactless fault" mechanism (electrified water). Body resistance drops to 300–600 ohms when fully wet. Three-layer protection model: RCDs as critical third layer. Demonstrates the European regulatory framework that has eliminated ESD in countries where it is applied.

**Relevance**: MODERATE — European technical perspective; complements Linja-aho's zero-ESD finding.

---

## KEY TECHNICAL FINDINGS SYNTHESIZED

### Current Thresholds (from Dalziel, USCG 2008, NEC/NFPA):
| Current Level | Effect | Protection Implication |
|---------------|--------|----------------------|
| 1 mA | Perception/tingle | Below all protection thresholds |
| 4–6 mA | Class A GFCI trip; muscle control interference | Class A GFCI trip point |
| 5 mA | ESD incapacitation in freshwater swimmers | ABYC E-11 minimum for individual circuits |
| 10–20 mA | Let-go threshold; respiratory muscle paralysis | Below 30 mA GFPE threshold |
| 30 mA | NEC 555 shore power receptacle limit; ELCI trip point | Current NEC/NFPA/ABYC protection threshold |
| 100 mA | Ventricular fibrillation; original NEC limit (2011–2017) | Superseded; now feeder-level limit only |

### Why Freshwater Creates Greater ESD Risk Than Saltwater:
- Freshwater resistivity: >900,000 ohm-cm
- Saltwater resistivity: <8,000 ohm-cm (approximately 50–1,000x more conductive)
- In freshwater: voltage gradient per unit distance is high; human body (~70% ionic water) is more conductive than surrounding water → preferred current path
- In saltwater: current disperses through conductive water; body current is reduced; protection devices more likely to trip
- Result: All documented ESD fatalities occurred in freshwater environments

### Why Standard Protection Devices Sometimes Fail to Prevent ESD:
- Fault current routed through ground conductors (rather than hot-to-neutral return) does NOT trip GFCI or ELCI protection devices (key finding: Dolan/Norton/Loftis ACAD-034; Coté ACAD-035)
- Floating dock movement can sever ground wires, creating undetected fault paths (Cavallaro case study ACAD-036)
- Multiple simultaneous vessel leakage currents can sum to trip protection devices even when individual vessels are within limits
- Pre-code wiring (pre-2011) at marinas has no GFP at all — the majority of US marina infrastructure

### International Comparison:
- Europe: Mandatory 30 mA RCDs for all shore power; ~0 ESD fatalities documented
- Finland (Linja-aho, ACAD-022): Zero ESD cases in 40 years of data despite abundant freshwater
- US: Approximately 2–5 documented ESD fatalities per year in databases; unknown number misclassified as drowning

---

## SEARCHES CONDUCTED

All 15 specified queries were run plus additional follow-up searches:
1. "electric shock drowning" IEEE electrical engineering research ✓ (found ACAD-020, 021)
2. "stray voltage" marina dock freshwater electrocution engineering ✓ (found ACAD-025, 034, 035)
3. "ground fault" marina dock drowning electrical safety ✓ (found ACAD-028, 029)
4. "GFCI" effectiveness marina freshwater dock electrocution prevention ✓ (found ACAD-029, 030, 039)
5. "shore power" safety fault current marina electrical standard ✓ (found ACAD-026, 030)
6. "equipotential bonding" marina dock electrical safety ✓ (found ACAD-028, 029, 034)
7. "NEC Article 555" marina electrical code electrocution history ✓ (found ACAD-029, 033)
8. "NFPA 303" marina fire protection electrical safety drowning ✓ (found ACAD-028, 027)
9. "electric shock drowning" NFPA OR NEC OR ABYC electrical standard ✓ (found ACAD-028, 029, 030)
10. "Marina Dock Age" "electric shock drowning" OR electrocution ✓ (found one article: Port Clinton Yacht Club)
11. BoatUS ABYC "electric shock drowning" safety report OR study ✓ (found BoatUS Seaworthy 2019, ABYC ELCI)
12. "leakage current" freshwater marina dock electrocution ✓ (found ACAD-034, 035)
13. "alternating current" freshwater swimming death marina ✓ (found current threshold literature)
14. "equipotential zone" marina shore power ESD ✓ (found ACAD-025, 034)
15. "electric shock drowning" congressional testimony OR hearing OR legislation ✓ (found ACAD-052: state legislation; no federal legislation found)

---

## SOURCE GAPS AND LIMITATIONS

1. **IEEE Xplore access**: Full text of ACAD-020 and related IEEE papers not directly accessible; findings synthesized from abstracts, ResearchGate descriptions, and citing sources

2. **ASME full text**: Koko/Ayyub simulation papers (ACAD-023, 024) not directly accessible; findings from abstracts and citing literature

3. **Marina Dock Age magazine**: Only one ESD-specific article found (Port Clinton Yacht Club). Broader Marina Dock Age ESD coverage likely exists but not accessible in search

4. **Federal legislation**: No federal ESD legislation found. The Wasserman Schultz document found was the Virginia Graeme Baker Pool Safety Act (suction entrapment, not ESD)

5. **ESDPA incident database**: Not used as primary source per task instructions; Rifkin/Shafer USCG grant report (ACAD-026) used as the engineering source

6. **NPS symposium paper** (SYM-AM-16-020): Referenced in search results but too large for WebFetch retrieval; described as a 2016 naval symposium paper on ESD

7. **EC&M full eBook**: Binary PDF not accessible via WebFetch; individual article URLs confirmed and used

---

## RECOMMENDATIONS FOR FURTHER RESEARCH

1. Obtain full text of Morse et al. 2020 IEEE paper (DOI: 10.1109/TIA.2020.2982854) for specific FEA methodology and numerical Zone of Danger dimensions
2. Obtain Koko/Ayyub 2016 simulation paper (DOI: 10.1115/1.4032262) for quantitative current density maps around fault-source boats
3. Search IEEE Xplore directly for additional ESD papers citing Morse 2020
4. Review complete EC&M ESD eBook for additional forensic case studies
5. Review IAEI Magazine archives for additional ESD articles beyond those found
6. Confirm status of NEC 2026 Article 555.36 vessel pre-connection testing requirement
7. Check whether NFPA 303 2026 edition has been formally adopted by major marina-heavy states
