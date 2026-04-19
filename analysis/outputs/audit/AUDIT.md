# ESD Dataset Audit — Top-Level Summary

**Generated:** 2026-04-19
**Scope:** Every one of the 201 incident files in `esd-dataset/`
**Purpose:** Pre-presentation confidence check before Nicole King Allen's
NCL (April 20, 2026), HOA, and NFPA Expo (June 22, 2026, with Kevin Ritz) talks.

---

## The short answer

> We have 201 incidents. 175 came from the ESDPA compilation; 26 are new to us.
> We independently verified 128 of them (63.7%) — meaning we found a
> non-ESDPA primary source that confirmed the incident. Every one of the
> remaining 73 is transparently labeled at its actual evidence level.
>
> We documented specific deviations from the ESDPA list in **127 entries**:
> dates corrected, locations refined, victim ages fixed, mechanism details
> added. This is the paper trail proving we did not simply copy the list.
>
> A skeptical reviewer could target ~92 entries on evidence strength. Every
> one of those is classified, explained, and carries a suggested next step.

---

## 1. Counts

| Group | Count | % |
|---|---:|---:|
| Incidents in dataset | 201 | 100% |
| Drawn from ESDPA compilation | 175 | 87.1% |
| Added independently (novel) | 26 | 12.9% |

**Discovery source — where we first found each incident:**

| Source | Count |
|---|---:|
| ESDPA | 170 |
| LOA1 (news archive) | 17 |
| LOA4 (government records) | 6 |
| LOA2 (misclassified drownings) | 5 |
| LOA11 (YouTube / local TV) | 2 |
| LOA3 (legal records) | 1 |

> Note: some ESDPA-listed entries were rediscovered via LOA searches and
> have multiple `additional_sources` entries — that's independent confirmation,
> not replacement of provenance.

---

## 2. Independent verification

| Verification level | Count | % |
|---|---:|---:|
| VERIFIED (≥2 independent sources) | 80 | 39.8% |
| CONFIRMED (1 independent source) | 46 | 22.9% |
| PROBABLE (strong circumstantial) | 2 | 1.0% |
| SUSPECTED (circumstantial only) | 10 | 5.0% |
| UNVERIFIED (on ESDPA trust only) | 63 | 31.3% |

**128 of 201 (63.7%) carry at least one non-ESDPA primary source.**

Mean primary sources per entry: 1.87. Maximum on a single entry: 10.

---

## 3. Deviations from ESDPA — the independent-verification paper trail

| Metric | Count |
|---|---:|
| ESDPA entries where we documented ≥1 correction or addition | **127** |
| Entries where we changed the date | 86 |
| Entries where we changed or refined the location | (see `esdpa_deviations.md`) |
| Entries where we added victim name, age, or gender | (see `esdpa_deviations.md`) |

Every deviation is tied to the primary source that drove the change.
Browse by state: see `esdpa_deviations.md`.

---

## 4. Weak-evidence triage — the 92 entries most likely to be questioned

| Tier | Count | Framing |
|---|---:|---|
| Novel + thin (we added, ≤1 source) | 13 | "Leads we surfaced; cautious level pending more sources" |
| ESDPA-only, pre-2000 | ~30 | "Pre-digital-archive; carried as UNVERIFIED" |
| ESDPA-only, post-2000 | ~33 | "Still working to independently confirm" |
| Fatal, no named victim | 54 (overlaps) | "Flagged for obituary/coroner follow-up" |

Full detail with suggested follow-up actions: `weak_evidence.md`.

---

## 5. Geographic and temporal spread

- Year span: **1981–2025** (45 years)
- 199 / 201 entries have a usable year
- Top states: TX (21), MO (16), FL (12), KY (10), GA (10), OK (9), NY (9),
  CA (9), MI (8), AL (8), TN (7), NC (7), SC (6), AZ (6), MN (5)

---

## 6. Incident type / mechanism

| Incident type | Count |
|---|---:|
| Fatal | 136 |
| Near-miss | 59 |
| Non-fatal (injured, survived) | 6 |

---

## 7. Where to look for full detail

| Report | What it gives you |
|---|---|
| `inventory.md` | Top-level counts, all 201 in one grid |
| `inventory.csv` | Machine-readable per-incident audit grid — sortable in Excel |
| `esdpa_deviations.md` | All 127 cases where we changed ESDPA's data, grouped by state |
| `esdpa_deviations.csv` | Same, machine-readable |
| `novel_incidents.md` | All 26 non-ESDPA incidents, with provenance per entry |
| `novel_incidents.csv` | Same, machine-readable |
| `weak_evidence.md` | 92 entries needing closer review, with suggested follow-up |
| `weak_evidence.csv` | Same, machine-readable |
| `audit_flags.md` | Flag-grouped list for pattern spotting |

---

## 8. Honest limitations (what to say if asked)

1. **ESDPA is the subject of study, not a source.** We never cite ESDPA
   itself as verification. The compilation pointed us at incidents; we
   independently verified where we could.

2. **UNVERIFIED is not "probably fake."** For 63 entries we could not
   find independent documentation — some are genuinely old (pre-digital),
   some had anonymized coverage, some had coverage that has since
   disappeared from the web. We chose transparency over trimming the list.

3. **Our IRR / trend analysis uses all incidents with a usable year.**
   Removing UNVERIFIED entries would bias toward recent and high-media-
   profile cases. Sensitivity analysis restricted to VERIFIED+CONFIRMED
   shows the same directional signal (marina flat, private dock rising).

4. **"Not in ESDPA" does not mean "we have bulletproof evidence."**
   Of our 26 novel incidents, 13 rest on only 0–1 independent sources.
   These carry SUSPECTED or CONFIRMED labels to reflect that.

5. **This audit is as of 2026-04-19.** New sources may be found at any
   time; entries can move up (to a higher verification level) as evidence
   accumulates.

---

## 9. Reproducibility

Every script is in `analysis/` and every output is in
`analysis/outputs/audit/`. Re-run at any time:

```bash
cd /opt/repos/esd-research
python3 analysis/audit_inventory.py
python3 analysis/audit_deviations.py
python3 analysis/audit_novel.py
python3 analysis/audit_weak_evidence.py
```

The dataset itself is the single source of truth — these reports are
always-derivable views of it.
