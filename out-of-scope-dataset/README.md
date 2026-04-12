# Out-of-Scope Dataset

This directory holds incidents that involve electricity in water but are **not currently included** in the main `esd-dataset/` for one of these reasons:

## Categories

### 1. Storm/Flood Electrocution (`storm-*`)
Deaths and injuries from downed power lines in standing water, flood water, or wet ground during/after severe weather events. These follow the same physical mechanism as ESD (current through water/wet ground paralyzing victims) but the source is utility infrastructure failure rather than dock/marina wiring.

**Why separate:** Different regulatory context (utility vs. NEC 555), different prevention strategies (storm preparedness vs. dock inspection), different fatality classification (NHC "indirect" deaths vs. unclassified). However, these incidents are critical evidence for the **storm electrocution surveillance gap** thesis.

### 2. International (`intl-*`)
Electricity-in-water incidents that occurred outside the United States. The main dataset is US-focused for regulatory consistency.

**Why separate:** Different electrical codes, different jurisdictional context. Some involve US victims (e.g., El Paso couple at Mexican resort) and may be relevant for US litigation tracking.

### 3. Adjacent/Edge Cases (`adj-*`)
Incidents that involve electricity and water but don't fit the classic ESD pattern — e.g., on-land electrocution in standing water, work-related electrofishing accidents, electric fish barrier hazards.

## File Naming

`{category}-YYYY-MM-DD-N.md` where category is `storm`, `intl`, or `adj`.

## Schema

Same as main `esd-dataset/SCHEMA.md` with one additional field:

```yaml
out_of_scope_reason: storm | international | adjacent
out_of_scope_notes: "Why this incident isn't in the main dataset"
```

## Promotion to Main Dataset

Some out-of-scope incidents may eventually be promoted to the main dataset if scope changes or if they turn out to involve the classic ESD mechanism (e.g., a storm victim discovered to have been electrocuted by dock wiring rather than a downed line).
