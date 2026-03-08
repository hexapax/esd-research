# Data Governance

This document describes the data sources, privacy considerations, and governance policies for the esd-research project.

---

## Data Sources and Legal Basis

All data in this repository derives from **publicly available sources**. No data was obtained from protected health information systems, covered entities under HIPAA, or sources requiring Data Use Agreements.

### Source Categories

| Source Type | Examples | Public Availability Basis |
|-------------|----------|--------------------------|
| Published news articles | Local and national newspapers, TV news websites | Published for public consumption; Fair Use for research |
| Obituaries and memorials | Legacy.com, funeral home websites, Find a Grave | Published by families for public viewing |
| Court records and legal filings | FindLaw, PACER, state court databases, law firm case summaries | Public judicial records |
| Federal government data | OSHA accident reports, CDC MMWR, NCHS public-use mortality files, USCG BARD (via FOIA) | Public domain (17 U.S.C. § 105) |
| State government records | Coroner press conferences, state agency reports, legislative records | Public records under state sunshine laws |
| Advocacy organization data | ESDPA incident list (Rev. 8/15/2025) | Published on electricshockdrowning.org for public distribution |
| Video archives | YouTube (local TV news uploads) | Publicly posted by news organizations |
| Academic literature | Peer-reviewed journal articles, conference proceedings | Published research |
| Community sources | Reddit posts, boating forum discussions, GoFundMe campaigns | Publicly posted by users |

### Third-Party Dataset Attributions

| Dataset | Source | License/Terms | Files |
|---------|--------|---------------|-------|
| USCG Boating Accident Report Database (BARD) | Data Liberation Project (via FOIA from USCG) | Public domain (federal data) | `reference/BARD-dataset-2009-2023-csv/` |
| NCHS Multiple Cause of Death | National Center for Health Statistics | Public-use research files (de-identified) | Not in repo (2.4 GB; gitignored) |
| ESDPA Incident List | James D. Shafer & Capt. David E. Rifkin, Quality Marine Services, LLC | Published for public distribution | `source-data/methodology/esd_list_-_updated_8.15.25__1_.pdf` |

---

## Privacy Considerations

### Personally Identifiable Information in This Dataset

This dataset contains the names, ages, genders, and locations of individuals involved in Electric Shock Drowning incidents, including **minor children** (both deceased and survivors). This information was collected exclusively from published public sources as enumerated above.

### Legal Framework

- **HIPAA** does not apply. No data was obtained from covered entities (healthcare providers, health plans, or healthcare clearinghouses). All health-related information (cause of death, injury descriptions) comes from published news reports, public coroner statements, or public court records.
- **Common Rule (45 CFR 46)** — Deceased persons are generally not considered "human subjects." Secondary analysis of publicly available data about deceased individuals does not constitute human subjects research under the Common Rule. However, some near-miss survivors in this dataset are living persons.
- **State privacy laws** — All information was obtained from sources published within the respective states' public records frameworks.

### Ethical Considerations

While legally permissible, the aggregation of publicly available information about identifiable individuals — particularly minor children — into a searchable research database warrants careful consideration:

1. **Deceased victims:** Names of deceased persons (including minors) published in news coverage and obituaries are part of the public record. Epidemiological research routinely includes named decedent information from public sources (see CDC MMWR case reports as precedent). This project follows that standard practice.

2. **Living survivors (near-miss incidents):** A small number of entries describe non-fatal incidents where individuals experienced electric shock but survived. These individuals' names appear in published news coverage. The dataset includes these names because they are essential for deduplication and cross-referencing across sources. Researchers using this data should consider whether re-identification of living survivors serves their research purpose.

3. **Aggregation effect:** Individual news articles about drowning incidents are published in isolation. This dataset aggregates information across sources, creating a searchable collection that did not previously exist. While no non-public information is included, the aggregation itself increases the practical accessibility of this information.

### Researcher Responsibilities

Users of this dataset should:

- Obtain appropriate institutional review (IRB exemption determination or approval) before using this data in formal research
- Consider whether individual-level identifiers are necessary for their specific analysis — aggregate statistics may suffice
- Follow their institution's data governance policies for research involving publicly available PII
- Not attempt to contact victims' families unless doing so is part of an IRB-approved research protocol
- Cite this dataset and its sources appropriately in any publications

---

## IRB Status

This project has not yet undergone formal IRB review. When affiliated with a research institution, this project is expected to qualify for **exempt status** under 45 CFR 46.104(d)(4): "Secondary research for which consent is not required — research involving the use of identifiable private information [...] if the information is publicly available."

Researchers at academic institutions should submit this project for an IRB exemption determination before using the data in formal research or publications.

---

## Restricted Data Policy

The following data sources are planned for future phases of this research and will **not** be stored in this public repository:

| Data Source | Access Mechanism | Expected Restrictions |
|-------------|-----------------|----------------------|
| CDC National Death Index (NDI) | IRB approval + formal application to NCHS | Data Use Agreement; no redistribution; secure storage required; destruction timeline |
| NEMSIS (National EMS dataset) | Research data request | Data Use Agreement; de-identified but restricted redistribution |
| State ME/coroner records | FOIA requests | May contain protected information; state-specific restrictions |
| NewspaperArchive.com content | Institutional API agreement | Terms of service may restrict redistribution of article text |

When restricted data is obtained, it will be maintained in a **separate, private repository** ([hexapax/esd-research-restricted](https://github.com/hexapax/esd-research-restricted)) with:
- Repository access limited to named researchers on the applicable DUA
- Compliance with all DUA terms including destruction timelines
- Only aggregate or de-identified results published back to this public repository

---

## Data Quality and Completeness

This dataset is a research work product, not a definitive registry. Known limitations:

- **73% of ESDPA entries had at least one data quality issue** (wrong date, wrong location, misclassification, etc.)
- **39% of ESDPA entries could not be independently verified** from any non-ESDPA source
- The true number of ESD incidents in the United States is unknown and likely substantially higher than the 193 documented here
- Verification status reflects the availability of public sources at the time of research (March 2026), not a definitive determination of whether an incident occurred
- Incident classification (ESD vs. direct electrocution vs. ordinary drowning) is based on available evidence and may be revised as additional information becomes available

---

## Contact

For questions about data governance, privacy concerns, or responsible use of this dataset, please open an issue on this repository.

---

## License

The research work product (analysis, code, schema, documentation) in this repository is released under **CC0 1.0 Universal** (see [LICENSE](LICENSE)). This license applies to the original analytical work, not to the underlying facts or third-party source materials, which retain their original terms.
