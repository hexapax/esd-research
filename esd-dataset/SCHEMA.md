# ESD Incident Dataset Schema

**Version:** 1.0
**Created:** 2026-03-08
**Purpose:** Unified incident dataset merging ESDPA list entries and all Phase 2 research findings into a single structured format suitable for Excel export and epidemiological analysis.

---

## File Naming Convention

**Format:** `ESD-YYYY-MM-DD-N.md`

- `YYYY` = Year of incident (required)
- `MM` = Month (use `00` if unknown)
- `DD` = Day (use `00` if unknown)
- `N` = Sequence number for same-date incidents (1, 2, 3...)

**Examples:**
- `ESD-2012-07-04-1.md` — First incident on July 4, 2012
- `ESD-2012-07-04-2.md` — Second incident on same date
- `ESD-1993-08-00-1.md` — August 1993, day unknown
- `ESD-1988-00-00-1.md` — 1988, month and day unknown

**Remapping note:** These IDs may be remapped to align with Nicole's existing Excel dataset. All files also carry cross-reference IDs linking back to every project file that documents the same incident.

---

## File Structure

Each file uses **YAML frontmatter** (between `---` markers) for structured data, followed by a **markdown body** for narrative and notes. The YAML is designed to be machine-parseable for CSV/Excel export.

---

## YAML Frontmatter Fields

### Incident Identification

```yaml
incident_id: ESD-2012-07-04-1        # Primary ID (matches filename)
date: "2012-07-04"                    # ISO 8601 date (use YYYY-MM or YYYY if partial)
year: 2012                            # Separate year column (Nicole's request)
date_precision: exact                 # exact | month | year | approximate
```

### Location

```yaml
state: MO                             # Two-letter state code
county: Camden                        # County name (if known)
city: Lake of the Ozarks              # City/town/area name
body_of_water: Lake of the Ozarks     # Lake, river, canal, pool, fountain name
facility_name: "Private dock, Gravois Arm, 6.5 Mile Marker"  # Marina, dock, pool name
coordinates:                          # GPS if available
  lat:
  lon:
```

### Incident Summary

```yaml
incident_type: fatal                  # fatal | non-fatal | near-miss
fatality_count: 2                     # Total deaths in this incident
injury_count: 1                       # Total injuries (shocked/hospitalized)
near_miss_count: 0                    # People who felt shock but were not injured
```

### Victims

Each victim is a list entry. This allows generating either incident-level rows (one row per incident with counts) or victim-level rows (one row per person).

```yaml
victims:
  - first_name: Alexandra
    last_name: Anderson
    age: 13
    gender: F                         # M | F | Unknown
    race:                             # If mentioned in sources; leave blank if not
    outcome: fatal                    # fatal | injured | near-miss | rescued
    role: primary                     # primary | rescuer | bystander
    cause_of_death: "Electric shock drowning"  # As stated in official records

  - first_name: Brayden
    last_name: Anderson
    age: 8
    gender: M
    race:
    outcome: fatal
    role: primary
    cause_of_death: "Electric shock drowning"
```

**When victim name is unknown:** Use `first_name: Unknown` and `last_name: Unknown`. Include whatever identifying details are available in the `notes` field (e.g., "10-year-old boy").

### Electrical Details

```yaml
electrical_source: dock_wiring        # dock_wiring | boat_lift | shore_power |
                                      # pool_pump | fountain | overhead_line |
                                      # extension_cord | charger | other | unknown
water_type: fresh                     # fresh | salt | brackish | pool | fountain
voltage:                              # If measured/reported (e.g., "120V AC")
fault_description: "Faulty junction box between house panel and dock disconnect"
```

### Verification and Provenance

```yaml
verification_level: VERIFIED          # See Verification Levels below
esdpa_listed: true                    # Is this incident in the ESDPA list?
esdpa_entry_numbers:                  # ESDPA list entry numbers across revisions
  - "#52 (Rev. 5/9/16)"
  - "#61 (Rev. 5/6/20)"
esdpa_date_correct: false             # Does ESDPA have the right date?
esdpa_date_listed: "2012-07-05"       # ESDPA's date if different from actual
esdpa_data_issues:                    # List of known errors in ESDPA entry
  - "Date off by 1 day"
  - "Location listed as 'Lake of the Ozarks' without mile marker"

discovery_source: ESDPA               # Where this incident was FIRST found in our project
                                      # ESDPA | LOA1 | LOA2 | LOA3 | LOA4 | LOA5 |
                                      # LOA6 | LOA7 | LOA8 | LOA11 | LOA13
additional_sources:                   # Other LOAs that independently found this
  - LOA3
  - LOA6
  - LOA11
independent_source_count: 7           # Number of non-ESDPA sources found
```

### Cross-References

```yaml
project_refs:                         # All project files documenting this incident
  - FI-2012-009                       # incident-research/ ESDPA file
  - LEGAL-2012-001                    # LOA3 legal records
  - LEAD-047                          # LOA6 community
  - VID-2012-025                      # LOA11 YouTube
  - LOA8-LOTOZ-2015-2017              # LOA8 research file
```

### Key Sources

```yaml
sources:
  - url: "https://www.lakeexpo.com/news/example"
    type: news                        # news | obituary | court | government |
                                      # academic | video | memorial | legal | other
    outlet: "Lake Expo"
    date: "2012-07-06"

  - url: "https://www.youtube.com/watch?v=example"
    type: video
    outlet: "ABC News"
    date: "2012-07-05"
```

### Notes

```yaml
notes: "Brief summary description of event. Include key details not captured in structured fields."
research_notes: "Internal notes on data quality, follow-up needed, etc."
```

---

## Verification Levels

| Level | Definition | Criteria |
|-------|-----------|----------|
| **VERIFIED** | Independently confirmed ESD incident | Multiple independent sources confirm electrical cause + water drowning; coroner/ME ruling consistent |
| **CONFIRMED** | At least one independent source confirms ESD | One non-ESDPA source confirms electrical involvement |
| **PROBABLE** | Strong circumstantial evidence of ESD | Multiple simultaneous shocks, electrical fault found post-mortem, stray voltage measured |
| **SUSPECTED** | Circumstantial evidence suggests ESD | Dock proximity, skilled swimmer, no autopsy evidence of natural cause, but no electrical investigation |
| **UNVERIFIED** | In ESDPA list but no independent sources | ESDPA entry exists but no non-ESDPA documentation found |
| **EXCLUDED** | Investigated and determined not classic ESD | Pool pump, fountain, overhead power line, or other non-dock/marina mechanism; OR ruled out by investigation |

**Note on EXCLUDED:** Some incidents (pool electrocutions, fountain deaths, overhead power line contacts) involve the same physics as ESD but are outside the traditional dock/marina scope. These are included in the dataset with `EXCLUDED` status and a note explaining why — they're relevant for epidemiological analysis of all in-water electrocution deaths even if they're not "classic" ESD.

---

## Incident Type Classification

| Type | Definition |
|------|-----------|
| `dock_marina_esd` | Classic ESD — AC current from dock/marina wiring leaks into natural water |
| `boat_lift_esd` | Boat lift motor or wiring energizes water |
| `shore_power_esd` | Shore power connection fault energizes hull/water |
| `pool_electrocution` | Pool pump, light, or wiring fault — same mechanism, different venue |
| `fountain_electrocution` | Decorative fountain electrical fault |
| `overhead_line` | Overhead power line contact with water or watercraft |
| `extension_cord` | Extension cord or temporary wiring fault near water |
| `other_in_water` | Other in-water electrocution not fitting above categories |

---

## Generating Excel Output

The YAML frontmatter is designed to produce two types of Excel rows:

### Incident-Level Row (one row per incident)
Use: `incident_id`, `date`, `year`, `state`, `county`, `city`, `body_of_water`, `facility_name`, `fatality_count`, `injury_count`, `near_miss_count`, `verification_level`, `notes`, first source URL

Victim names: concatenate all victims' names into a single cell (e.g., "Alexandra Anderson (13F), Brayden Anderson (8M)")

### Victim-Level Row (one row per person)
Expand the `victims` array: one row per victim, duplicating incident-level fields across rows. Add: `first_name`, `last_name`, `age`, `gender`, `race`, `outcome`, `role`

---

## Example File

See `ESD-2006-03-18-1.md` for a complete example (Nicholas Harbison, DeSoto MO).

---

*This schema is part of the esd-research project. Files conforming to this schema live in `esd-dataset/`.*
