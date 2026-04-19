---
note_id: NOTE-2026-04-18-Holiday-Marina
date: 2026-04-18
related_incidents:
  - SUSP-BATCH-001 (Teresa Ann Graham, 2018-07-17)
  - SUSP-BATCH-004 (Gavrie Alexander Whitlock, 2023-09-02)
  - ESD-2023-07-27-1 (Thomas "Shep" Milner — NOT at Holiday Marina, see correction below)
---

# Holiday Marina (Lake Lanier) — mitigations and post-incident response

Focused investigation, 2026-04-18, on whether any electrical-safety changes were made at Holiday Marina after the 2023 Lake Lanier ESD/drowning deaths.

## Correction to earlier framing

The SUSP-BATCH-2026-04-18 triage file and subsequent FINDINGS discussion characterized Holiday Marina as a three-fatality cluster (Graham 2018, Milner 2023, Whitlock 2023). **That was wrong.** Milner 2023 was at a **private family dock "near Little Ridge Park" in Forsyth County**, not at Holiday Marina. The three coverage outlets (AJC, WSB-TV, FOX5) all place Milner at the family's long-held private dock near Dove Trail / Lanier Beach South Road, Forsyth County — a different geography and a different ownership model from Holiday Marina.

The Holiday Marina cluster is therefore **two incidents**, both "suspected" and neither officially ruled ESD:

| Incident | Date | Location | Official ruling |
|---|---|---|---|
| Teresa Ann Graham (51F) | 2018-07-17 | Holiday Marina Dock Q, Hall County | "Suspected accidental drowning; no foul play" |
| Gavrie Alexander Whitlock (23M) | 2023-09-02 | Holiday Marina, Hall County | Drowning — slipped while running, found in 17 ft water |

The Milner 2023 confirmed ESD is **not** at Holiday Marina. Treat it as a separate private-dock incident.

## Holiday Marina profile

- **Operator:** Suntex Marinas (per https://suntex.com/locations/holiday-on-lake-lanier/)
- **Address:** 6900 Lanier Islands Parkway, Buford, GA 30518
- **Size:** ~1,300 wet slips; oldest and largest floating marina on Lake Lanier
- **Location:** south end of Lake Lanier, near Lanier Islands
- **Counties touched:** Hall (marina itself) and Gwinnett (some adjacent waters)

Not owned by Safe Harbor (which operates Aqualand Marina on Lake Lanier and the Lanier Islands resort marinas, not Holiday).

## Regulatory mitigations that exist (all predate the incidents)

### USACE "Exhibit C" electrical inspection regime
US Army Corps of Engineers, Mobile District, requires every Lake Lanier dock with electrical service to pass a licensed-electrician inspection every 5 years. Source: USACE brochure at `sam.usace.army.mil/Portals/46/docs/recreation/OP-SL/Brochures/Exhibit_C.pdf`.

Required elements:
- All installations must meet or exceed **NEC Article 555** (Marinas and Boatyards)
- Shore-power receptacles: **30 mA GFCI** protection
- Feeder circuits: **100 mA GFCI** protection
- UF or USE cable only; minimum 24" burial depth; warning tape at 12"
- Service pole: wooden, 6"×6" max, at elevation ≥1073 MSL
- Shoreline panel box: hardwired, eye level, min 5' above ground
- All metal dock components must be bonded and grounded
- Receptacles: locking/grounding type, weatherproof enclosures, self-closing caps, 20A min for shore power
- Max 2 single or 1 duplex receptacle on dock
- Conduit-enclosed wiring rated for wet locations
- Lights aimed downward, 150 W max

**Critical weakness** — per a USACE public affairs officer quoted in the Stoddard Firm's May 2024 piece on Milner: *"that inspection simply consists of checking that a licensed electrician has signed off on them."* It is a **paperwork compliance check**, not a physical voltage-or-leakage measurement. A dock can pass Exhibit C with latent faults that develop between the 5-year intervals.

### Georgia "restricted use area" designation
GA Comp. R. & Regs. R. 391-4-5-.20 lists **Holiday Marina** as one of several Lake Lanier marinas where swimming is prohibited in the immediate vicinity. This is a pre-existing blanket regulation, not a post-incident change.

### Lake Lanier Association recommendations
`lakelanier.org/our-work/safe-lake/safe-initiatives/dock-safety/` — the association's dock-safety page recommends (but cannot mandate) a stray-voltage detection device like **Dock Lifeguard** for any electrified dock. No published figures on adoption rate.

## Mitigations that were NOT found

After searching for post-2023 actions specific to Holiday Marina or Lake Lanier, I could not locate any of the following:

1. **No announced Suntex/Holiday Marina retrofit.** No press release, no news coverage, no Lake Lanier Association bulletin about electrical upgrades at Holiday Marina after Whitlock's 2023 death.
2. **No wrongful-death lawsuit filed.** The Stoddard Firm's May 2024 piece is a solicitation aimed at Martha Milner; no complaint has been filed on the Milner case as of available coverage. No suit against Suntex for Graham or Whitlock.
3. **No change to the Exhibit C frequency or methodology.** Still 5 years, still a paperwork check. USACE has not added a physical voltage-measurement requirement.
4. **No Georgia state-level dock-electrical legislation post-2023.** Missouri tried (and failed) similar legislation after the Anderson 2012 deaths at Lake of the Ozarks; Georgia has not publicly mirrored that effort for Lake Lanier.
5. **No Hall County or Forsyth County dock-electrical ordinance update.** In sharp contrast, Smith Mountain Lake VA (Franklin, Bedford, Pittsylvania counties) moved to a uniform updated dock-inspection code within weeks of the Hamric death in July 2024 (Cardinal News, 2024-08-07; Tri-County Lakes, 2024-08-16). Lake Lanier's counties have not done the analogous update.
6. **No mandatory stray-voltage monitoring at marina slips.** Dock Lifeguard and similar sensors remain voluntary.
7. **No official Graham autopsy conclusion is public.** Body was sent to DeKalb County ME in July 2018; no follow-up coverage found. Cause of death is unpublished.
8. **No official Whitlock follow-up.** Initial reporting framed it as a slip-and-fall drowning; no subsequent coverage indicates an electrical investigation was done.

## Why mitigation hasn't been driven by the Holiday Marina cases

The Graham and Whitlock incidents were ruled (or framed in news coverage as) non-electrical drownings. Without an official ESD determination at Holiday Marina, there's no regulatory or PR trigger for electrical remediation. Compare:

| Venue | Incident | Ruling | Response |
|---|---|---|---|
| Holiday Marina, GA | Graham 2018 | "Suspected accidental drowning" | None specific |
| Holiday Marina, GA | Whitlock 2023 | "Slipped running; drowning" | None specific |
| Private dock, Forsyth County, GA | Milner 2023 | **Electric shock (confirmed)** | Stoddard Firm solicitation; no suit filed; no regulatory change |
| Private dock, Huddleston, VA | Hamric 2024 | **Electric shock (confirmed)** | 3-county uniform code update + new signage mandate within ~1 month |

The Virginia response was driven by official ESD determination *and* active building-official coordination. The Georgia response to Milner (despite the confirmed ESD ruling) did not produce a similar coordinated code update. This is a governance gap more than an information gap.

## What would shift the picture

If the Graham and/or Whitlock files can be matched to evidence of electrical contributory cause (autopsy language, police body-cam footage showing responder voltage readings, dock-inspection records around the time of each incident), the picture changes. Concretely:

1. **Hall County Coroner / DeKalb County ME records** for Graham (2018-07-17) — need FOIA for COD language
2. **Hall County Fire Rescue incident reports** for Whitlock (2023-09-02) — any voltage readings taken during body recovery?
3. **USACE Exhibit C history** for Holiday Marina's slips — when was each slip last inspected? Any corrections noted?
4. **Hall County building inspection records** — was any electrical work done on Holiday Marina docks after July 2018 or September 2023?
5. **Suntex Marinas internal electrical-inspection records** — what does their maintenance regime look like beyond the 5-year Exhibit C?

## Follow-up tasks for this incident pair

- [ ] FOIA the Hall County Coroner for Graham's cause of death and autopsy summary
- [ ] FOIA DNR/DNR Law Enforcement for Whitlock incident report, including any on-scene voltage testing
- [ ] Request USACE Exhibit C records for Holiday Marina slips Q and adjacent (2013–2024)
- [ ] Search GA secretary of state / Fulton / Hall County court records for any litigation involving "Suntex" + "Lake Lanier" + "dock" post-2018
- [ ] Contact Lake Lanier Association board members (they publish a newsletter — check 2019 and 2024 issues for any Holiday Marina-specific language)
- [ ] Check Channel 2 Action News "9 Investigates" archives for any Lake Lanier dock safety series post-2023

## Sources

- AJC 2018-07-19 — Graham at Holiday Marina Dock Q: https://www.ajc.com/news/local/suspected-drowning-victim-fell-off-dock-into-lake-lanier-sheriff-says/nzBlWapEwJ08XESyeDhJ4L/
- AJC 2023-08-01 — Milner (note: Forsyth County PRIVATE dock, not Holiday): https://www.ajc.com/news/2-dead-by-drowning-1-swimmer-still-missing-after-weekend-at-lake-lanier/PDZRH7UM7BFUFG3CJ5WNIMPUXA/
- FOX5 2023-09 — Whitlock at Holiday Marina: https://www.fox5atlanta.com/news/24-year-old-man-dies-after-slipping-on-dock-at-lake-lanier
- Stoddard Firm 2024-05-09 — USACE "paperwork only" admission: https://thestoddardfirm.com/dock-electrocution/
- Suntex Marinas — Holiday Marina operator: https://suntex.com/locations/holiday-on-lake-lanier/
- USACE Exhibit C brochure: https://www.sam.usace.army.mil/Portals/46/docs/recreation/OP-SL/Brochures/Exhibit_C.pdf
- GA Comp. R. & Regs. R. 391-4-5-.20: https://www.law.cornell.edu/regulations/georgia/Ga-Comp-R-Regs-R-391-4-5-.20
- LLA Dock Safety: https://lakelanier.org/our-work/safe-lake/safe-initiatives/dock-safety/
- Cardinal News on SML response (contrast case): https://cardinalnews.org/2024/08/07/stray-voltage-dangers-back-in-spotlight-following-smith-mountain-lake-death/
- Tri-County Lakes on SML code update (contrast case): https://tricountylakes.org/building-inspectors-discussing-code-changes-after-teens-death-at-smith-mountain-lake/
