# ESD Incident Extraction — Claude Prompt Documentation

This document records the exact instructions used to extract ESD incidents from the ESDPA source PDF into structured individual files. Kept here for repeatability and audit purposes.

**Executed:** 2026-03-01
**Source PDF:** `esd_list_-_updated_8.15.25__1_.pdf`
**Model:** Claude (via claude_code MCP tool)
**Output:** `incidents-raw/` directory — one `.md` file per unique incident

---

## Prompt Given to Claude

### Overview

Clone the repository at https://github.com/hexapax/esd-research, add the ESDPA ESD Incident List PDF (Rev. 8/15/2025) to the root, then extract all ESD incidents into individual files in a new `incidents-raw/` folder. Each incident gets a file ID based on year, prefixed with `FI` (Fatal Incident — ≥1 human died from ESD/in-water electrocution) or `NM` (Near Miss — ESD conditions present, all humans survived or hazard found before anyone entered water).

### File Naming Convention

```
{PREFIX}-{YEAR}-{NNN}.md
```

- `FI` = Fatal Incident
- `NM` = Near Miss
- `YEAR` = 4-digit year (use `XXXX` for unknown)
- `NNN` = zero-padded sequential counter within that PREFIX+YEAR group, ordered chronologically

### Source Document Structure

The PDF "Electric Shock Drowning Incidents – Marinas©" by James D. Shafer & Capt. David E. Rifkin (Quality Marine Services, LLC, Rev. 8/15/2025) contains two sections:

1. **ELECTRIC SHOCK DROWNINGS** — Items 1–116 (item #65 explicitly removed; items #8, #49, #69, #76, #82, #93, #107 unlabeled in PDF but inferred from context)
2. **ELECTRIC SHOCK – NEAR MISSES** — Items 1–75 (header notes "Additional ones included above" — many are deliberate cross-references to drowning section entries)

### Key Disambiguation Rules

1. **One file per real-world incident** — ~16 incidents appear in both sections with date discrepancies; create one file using ESD section as primary, note NM item number and discrepancy.
2. **Classification in NM section is survivor-focused** — some NM entries describe incidents where people died (they're in NM because a rescuer or bystander survived); classify as FI if any human died.
3. **Item #65** is explicitly "Removed" — do not create a file.
4. **Item #85** (Allatoona Lake GA, 2003) is wildlife-only (6 ducks killed); classify as FI but note no human fatalities.
5. **Item #113** contains two sub-incidents on same date (July 29, 1986) — create two files.
6. **Date discrepancies**: Several cross-section duplicates have significant date discrepancies (up to 394 days). Use the ESD section date as primary. See ISSUES.md for full analysis.
7. **ESD #36 vs NM #29** (Palm Springs FL/CA) — may be two different incidents or one with major data errors; create one file and flag heavily.

### Classification Edge Cases

| Situation | Rule |
|-----------|------|
| All survived but listed in ESD Drownings (e.g., #31 Tennessee Lake) | NM |
| "Last known in critical condition" (items #32, #34) | FI — in Drownings section implies likely fatality; note uncertainty |
| Wildlife-only fatality (#85) | FI — note no human fatalities |
| Items in NM section involving confirmed deaths | FI |
| International incidents (Turkey #21, Canada NM #17, #23, #57) | Include, note international |

### File Template

```markdown
# {INCIDENT-ID}

| Field | Value |
|-------|-------|
| **Date** | {exactly as in PDF} |
| **Location** | {city, state/location} |
| **Classification** | Fatal Incident OR Near Miss |
| **Outcome** | {Dead: N, Injured: N, Shocked/survived: N} |
| **Source Section** | Electric Shock Drownings / Near Misses / Both |
| **PDF Item Number(s)** | #{n} |

## Description

{Full verbatim text from PDF}

## Classification Notes

{Reasoning, discrepancies, uncertainties}

---
*Source: "Electric Shock Drowning Incidents – Marinas©"*
*James D. Shafer & Capt. David E. Rifkin, Quality Marine Services, LLC — Rev. 8/15/2025*
```

### Expected Output

Approximately 174 unique incident files:
- ~130 FI files
- ~44 NM files

See `ISSUES.md` for all identified data quality issues in the source document.
