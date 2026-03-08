# Dataset Conversion Plan

## Scope

Convert all unique ESD incidents from across the project into the unified `esd-dataset/` schema.

## Source File Inventory

| Source | Files | Unique Incidents (est.) | Notes |
|--------|-------|------------------------|-------|
| incident-research/ (ESDPA) | 175 FI/NM files | ~170 | Some may be phantoms/duplicates |
| LOA1 (news archive) | 21 NEW files | ~15-20 | Some overlap with ESDPA |
| LOA2 (misclassified) | 25 SUSP files | ~20 | Some overlap with ESDPA |
| LOA3 (legal records) | 20 LEGAL files | ~15 | Mostly overlap with ESDPA |
| LOA4 (government) | 12 GOV files | ~5 | Some overlap |
| LOA6 (community) | 42 LEAD files | ~15-20 | Significant overlap with ESDPA |
| LOA11 (YouTube) | 35 VID files | ~5-10 new | Mostly documents known incidents |
| **Total unique incidents** | | **~200-250** | After deduplication |

## Conversion Batches

### Batch 1: ESDPA Base List (incident-research/)
- 175 files (FI-YYYY-NNN.md, NM-YYYY-NNN.md)
- These are the base entries; most will have ESDPA as discovery_source
- Need to cross-reference with LOA findings to enrich data
- Split into 4 agent batches of ~44 files each

### Batch 2: Net-New Phase 2 Incidents
- Incidents found by LOAs that are NOT in the ESDPA list
- LOA1 new incidents, LOA2 SUSP files not in ESDPA, LOA6 LEAD files not in ESDPA
- Requires careful deduplication

### Batch 3: Quality Review
- Verify no duplicates across all converted files
- Check that all cross-references are correct
- Generate summary statistics

## Deduplication Strategy

1. Use victim names as primary deduplication key
2. Use date + state as secondary key
3. Use body_of_water + year as tertiary key
4. When multiple project files describe the same incident, merge data from all into one consolidated file

## ID Assignment

Format: ESD-YYYY-MM-DD-N (Nicole's preferred format)

For incidents with unknown dates:
- Month unknown: ESD-YYYY-00-00-N
- Day unknown: ESD-YYYY-MM-00-N
- Approximate: Use best estimate with date_precision: approximate
