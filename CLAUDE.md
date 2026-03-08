# CLAUDE.md — Instructions for AI-Assisted Research on This Repository

This file helps Claude Code (or any AI coding assistant) understand the structure, conventions, and rules of this research project so it can guide a researcher in adding to and maintaining the repository correctly.

## Project Overview

This is an epidemiological research project studying **Electric Shock Drowning (ESD)** — deaths and injuries caused by AC electricity leaking from dock/marina wiring into fresh water. The project independently verifies, corrects, and expands the ESDPA incident list using only primary public sources.

**Current state:** 193 documented incidents in a consolidated dataset (`esd-dataset/`), drawn from 175 ESDPA entries plus 18 net-new incidents found through 14 Lines of Attack (LOA1–LOA14). The dataset spans 1981–2025.

## Repository Structure

```
esd-research/
├── README.md                    # Project overview and key findings
├── DATA-GOVERNANCE.md           # Privacy, ethics, data source policies
├── CLAUDE.md                    # This file
├── research-summary.md          # Phase 1 ESDPA verification statistics
├── phase2-plan.md               # Research plan with LOA execution status
│
├── esd-dataset/                 # THE PRIMARY OUTPUT
│   ├── SCHEMA.md                # Data dictionary — READ THIS FIRST
│   ├── ESD-YYYY-MM-DD-N.md      # 193 incident files (YAML frontmatter + markdown)
│   ├── export_dataset.py        # Generates CSV/XLSX from YAML
│   ├── extract_issues.py        # Extracts ESDPA data quality issues
│   └── exports/                 # Pre-built CSV and XLSX files
│
├── source-data/                 # ESDPA PDF extraction (175 files)
│   └── methodology/             # Extraction prompt, source PDF, orchestration script
│
├── verification/                # Independent verification of each ESDPA entry (175 files)
│
├── phase2-findings/             # Unlisted incident search results
│   ├── PHASE2-META-ANALYSIS.md  # Cross-LOA synthesis
│   ├── LOA1-news-archive/       # 21 NEW files
│   ├── LOA2-misclassified-drownings/  # 25 SUSP files
│   ├── LOA3-legal-records/      # 20 LEGAL files
│   ├── LOA4-government-records/ # 12 GOV files
│   ├── LOA5-academic/           # 34 ACAD files
│   ├── LOA6-community/          # 52 LEAD files
│   ├── LOA7-structured-databases/
│   ├── LOA7C-nchs-mortality/
│   ├── LOA8-obituary-mining/    # 21 research files
│   ├── LOA11-youtube/           # 35 VID files
│   └── LOA13-wayback/
│
└── reference/                   # Supporting docs, search strategies, BARD data
```

## Critical Rules

### Source Exclusion Rule

**NEVER use these as independent verification sources:**
- ESDPA.org (electricshockdrowning.org)
- MikeHolt.com (forum reposts of the ESDPA list)
- OnTimeService.com
- Any website that reproduces the ESDPA list verbatim

These are the **subject of study**, not independent sources. Using them as verification creates circular sourcing. All verification must come from primary sources: news articles, obituaries, court records, government reports, etc.

### Data Governance

- Read `DATA-GOVERNANCE.md` before adding any data
- All data must come from **publicly available sources** (news, obituaries, court records, government data)
- Data from restricted sources (NDI, NEMSIS, state ME records) goes in the **private** repo: `hexapax/esd-research-restricted`
- The dataset contains names of deceased persons including minors — this is standard epidemiological practice for public-record data, but treat it with appropriate care

## How to Add a New Incident

### Step 1: Check for duplicates

Before creating a new entry, verify the incident isn't already in the dataset:

```bash
# Search by victim name
grep -rl "LastName" esd-dataset/

# Search by date
ls esd-dataset/ESD-YYYY-MM-DD-*.md

# Search by location
grep -rl "Lake Name" esd-dataset/
```

Many incidents appear under multiple IDs across source files (FI-, SUSP-, LEAD-, VID-, GOV-, NEW-, LEGAL-). The `project_refs` field in each dataset file lists all cross-references. Check those too.

### Step 2: Create the dataset file

File naming: `esd-dataset/ESD-YYYY-MM-DD-N.md`
- Use `00` for unknown month or day
- N = sequence number (1 unless another incident exists on that date)

Follow the schema in `esd-dataset/SCHEMA.md` exactly. The file must have:

1. **YAML frontmatter** between `---` markers with all required fields
2. **Markdown body** with a summary section

Here is a minimal template:

```yaml
---
incident_id: ESD-YYYY-MM-DD-N
date: "YYYY-MM-DD"
year: YYYY
date_precision: exact

state: XX
county:
city:
body_of_water:
facility_name:
coordinates:
  lat:
  lon:

incident_type: fatal
fatality_count: 0
injury_count: 0
near_miss_count: 0

victims:
  - first_name: Unknown
    last_name: Unknown
    age:
    gender:
    race:
    outcome: fatal
    role: primary
    cause_of_death:

electrical_source: unknown
water_type: fresh
voltage:
fault_description:

verification_level: UNVERIFIED
esdpa_listed: false
esdpa_entry_numbers: []
esdpa_date_correct:
esdpa_data_issues: []

discovery_source: LOA1
additional_sources: []
independent_source_count: 0

project_refs: []

sources: []

legal_outcome:

notes: ""
research_notes: ""
---

# ESD-YYYY-MM-DD-N: [Victim or Description] — [Location]

## Summary

[1-3 sentence description of the incident]
```

### Step 3: Set the verification level

| Level | When to use |
|-------|------------|
| VERIFIED | Multiple independent sources confirm electrical cause + drowning |
| CONFIRMED | One independent source confirms the incident |
| PROBABLE | Strong circumstantial evidence (simultaneous shocks, electrical fault found) |
| SUSPECTED | Circumstantial (dock proximity, skilled swimmer) but no electrical investigation |
| UNVERIFIED | In ESDPA list but no independent sources found |

### Step 4: Regenerate exports

After adding or modifying incidents:

```bash
python3 esd-dataset/export_dataset.py
```

This regenerates the CSV and XLSX files in `esd-dataset/exports/`.

### Step 5: Commit

Stage only the specific files you changed:

```bash
git add esd-dataset/ESD-YYYY-MM-DD-N.md
git add esd-dataset/exports/
git commit -m "Add ESD-YYYY-MM-DD-N: [Victim Name], [Location]"
```

## How to Update an Existing Incident

Common updates:
- **Victim name identified** — Update `first_name`/`last_name` in the victims array
- **New source found** — Add to `sources` list, increment `independent_source_count`, consider upgrading `verification_level`
- **Date correction** — Update `date`, set `esdpa_date_correct: false`, add the old date to `esdpa_date_listed`, document in `esdpa_data_issues`
- **Cross-reference found** — Add the LOA file ID to `project_refs` and LOA name to `additional_sources`

Always regenerate exports after changes.

## How to Add Phase 2 Research Results

Phase 2 findings go in `phase2-findings/` subdirectories, organized by LOA:

| LOA | Directory | File prefix | Description |
|-----|-----------|-------------|-------------|
| LOA1 | LOA1-news-archive/ | NEW-YYYY-NNN | News archive search results |
| LOA2 | LOA2-misclassified-drownings/ | SUSP-YYYY-NNN | Suspected misclassified drownings |
| LOA3 | LOA3-legal-records/ | LEGAL-YYYY-NNN | Legal/court findings |
| LOA4 | LOA4-government-records/ | GOV-YYYY-NNN | OSHA, CPSC, CDC, USCG records |
| LOA6 | LOA6-community/ | LEAD-NNN | Community/forum leads |
| LOA8 | LOA8-obituary-mining/ | LOA8-* | Obituary research files |
| LOA11 | LOA11-youtube/ | VID-YYYY-NNN | YouTube video documentation |

After adding Phase 2 findings, also create or update the corresponding `esd-dataset/ESD-*.md` entry so the consolidated dataset stays current.

Each LOA directory should have a summary file (e.g., `LOA1-A-summary.md`) documenting what was searched, what was found, and what was not found.

## Key Files to Read Before Starting

1. `esd-dataset/SCHEMA.md` — The data dictionary. Understand the YAML fields.
2. `DATA-GOVERNANCE.md` — Privacy and source rules.
3. `phase2-plan.md` — The research plan. Check what's done vs. remaining.
4. `phase2-findings/PHASE2-META-ANALYSIS.md` — Cross-LOA analysis and priority actions.
5. `research-summary.md` — Phase 1 verification results and patterns.

## Common Research Tasks

### "Search for a specific incident"
1. Search news archives (Perplexity, Brave) for victim name + location + date
2. Search obituaries (Legacy.com, funeral home websites)
3. Search court records (FindLaw, PACER)
4. Check YouTube for local TV coverage
5. Cross-reference against existing dataset entries

### "Verify an ESDPA entry"
1. Read the source-data/ file for what ESDPA claims
2. Read the verification/ file for what independent research found
3. Search for additional sources not yet found
4. Update the esd-dataset/ entry with any new information

### "Find new incidents in a state"
1. Read `reference/search-strategy.md` for the search methodology
2. Use keyword combinations from `reference/esd-search-terms.md`
3. Focus on states with known geographic gaps: TX, MN, WI, WA, OR, NC, SC, NY, PA, MD
4. Create Phase 2 finding files and corresponding dataset entries

### "Analyze the dataset"
```bash
# Generate fresh exports
python3 esd-dataset/export_dataset.py

# Extract ESDPA data quality issues
python3 esd-dataset/extract_issues.py --out issues-report.md

# Quick stats
grep -c "verification_level: VERIFIED" esd-dataset/ESD-*.md
grep -c "verification_level: UNVERIFIED" esd-dataset/ESD-*.md
grep -c "incident_type: fatal" esd-dataset/ESD-*.md
```

## What NOT to Do

- Do not use ESDPA/MikeHolt/OnTimeService as verification sources
- Do not store restricted-access data (NDI, NEMSIS, state ME records) in this repo — use `esd-research-restricted`
- Do not commit large binary files (PDFs > 10MB, datasets > 50MB) — use `.gitignore`
- Do not modify `source-data/` files — those are the original ESDPA extraction and should remain unchanged
- Do not delete dataset entries — if an entry is wrong, update its `verification_level` and add notes explaining why
