# Additional Data Sources and Lines of Attack for ESD Incident Discovery

## Executive Summary

The Phase 2 plan in the esd-research repository lays out six well-structured Lines of Attack (LOA1–LOA6) covering news archives, misclassified drownings, legal records, government databases, academic literature, and community sources. This report identifies **nine additional lines of attack** and **several major data sources** that are either absent from the current plan or mentioned but not operationalized. The most impactful additions are the freely available USCG Boating Accident Report Database (BARD), the NEMSIS national EMS dataset, AI-powered obituary mining techniques proven in peer-reviewed research, and state Child Fatality Review Team records. Together, these additions could substantially increase both the number of verified incidents discovered and the rigor of prevalence estimates.

***

## Critical Data Sources Not in the Current Plan

### USCG Boating Accident Report Database (BARD) — Freely Available

This is arguably the single most important data source missing from the Phase 2 plan. The Data Liberation Project obtained the full USCG Boating Accident Report Database through FOIA and has made it publicly available in CSV, SQLite, and Parquet formats. The dataset covers:[^1][^2]

- **2009–2023**: 58,430 boating accidents, 78,316 vessels, 8,935 deaths, and 36,773 injuries[^3]
- **1995–2012**: An earlier release via MuckRock provides overlapping historical data with accidents, deaths, injuries, and vessel tables[^2]

The BARD data comes from CG-3865 forms that boat operators must file when an incident results in a death, disappearance, serious injury, or substantial damage. Each record includes details about the accident, vessel, death, and injury involved. Critically, the cause-of-death field can be filtered for electrocution, and location data can be cross-referenced against marina and dock coordinates. The Phase 2 plan mentions USCG statistics and notes that BARD "may require FOIA" — but the FOIA has already been completed and the data is free to download right now.[^4][^5][^1]

**Action**: Download the BARD CSVs immediately. Filter the Deaths table for electrocution-related cause codes. Cross-reference all results against the ESDPA list. This single step could surface dozens of incidents in hours rather than weeks.

### NEMSIS — National EMS Information System

NEMSIS is the national standardized EMS database containing data from 14,756 EMS agencies across all 54 states and territories. The 2024 public-release research dataset includes 60,298,684 EMS activations. Key features for ESD research:[^6]

- ICD-10 coded cause of injury (can filter for electrocution + drowning)
- Scene location information with enhanced geo-coding[^7]
- Brief narrative fields describing incident circumstances
- Provider impression (diagnosis) based on ICD-10

The public-release dataset is de-identified but retains enough detail to identify incidents by date, general location, and clinical presentation. An EMS response to a dock or marina for a drowning with cardiac arrest in a young healthy person would generate a distinctive data signature.[^8][^9]

**Action**: Request the NEMSIS public-release research dataset. Filter for EMS activations involving electrocution (ICD-10 W86) at or near water bodies, and drowning (W74) with concurrent electrical injury indicators.

### NEISS — National Electronic Injury Surveillance System (Partially Mentioned, Not Operationalized)

The Phase 2 plan mentions NEISS briefly under LOA4 but does not include specific query instructions. NEISS is a free, publicly queryable database covering ~100 hospital emergency departments nationwide. Each record includes a brief narrative describing the injury scenario, which a 2026 study confirmed captures drowning characteristics not available in coded fields alone.[^10][^11]

NEISS data can be queried online at cpsc.gov using product codes for docks, shore power cords, boat lifts, and pool equipment, cross-referenced with electrocution diagnosis codes. The narrative field is particularly valuable — phrases like "dock," "marina," "tingling," or "shock in water" could surface near-miss incidents that never made news.[^12][^13]

**Action**: Run NEISS queries for the past 20 years using electrocution diagnosis + water/pool/dock product codes. Extract and analyze narrative fields for ESD-pattern language.

### CDC National Death Index (NDI)

The NDI is a central computerized index of all U.S. death records since 1979, maintained by NCHS. NDI Plus provides ICD-10 coded cause of death. This is the gold standard for mortality research and is the appropriate tool for a rigorous epidemiological study of ESD prevalence.[^14][^15]

Key capabilities:

- Researchers can submit a list of study subjects and receive matching death records[^16]
- NDI Plus provides cause-of-death codes without needing to contact individual state vital statistics offices
- NIH has an agreement with NCHS that simplifies access for researchers and covers costs[^16]

A researcher with IRB approval through an academic institution could cross-reference W86 (electric current exposure) deaths with location data near water bodies and marinas. This would provide the most rigorous estimate of ESD prevalence ever attempted.[^15]

**Action**: This is a medium-term play requiring institutional affiliation. The researcher would need to develop a study protocol, obtain IRB approval, and submit an NDI application. The payoff — a comprehensive national count of electrocution deaths near water — would be the definitive epidemiological contribution.

***

## Additional Lines of Attack Beyond LOA1–LOA6

### LOA7: Structured Database Mining (BARD + NEMSIS + NEISS)

None of the current six LOAs involve downloading and querying structured databases with filtering and cross-referencing. This is qualitatively different from the web-search and document-review approaches in LOA1–LOA6. Structured databases allow:

- **Exact filtering** by cause-of-death codes (electrocution), location types (marina, dock), and date ranges
- **Statistical analysis** of drowning patterns near electrical infrastructure
- **Completeness checks** — how many boating electrocution deaths appear in BARD but not in the ESDPA list?

| Database | Records | Coverage | Cost | Effort |
|----------|---------|----------|------|--------|
| BARD (USCG) | 8,935 deaths (2009–2023) | Boating accidents nationwide | Free | Low — download and filter CSVs[^1] |
| BARD (MuckRock) | 1995–2012 deaths | Earlier boating accidents | Free | Low — download and filter[^2] |
| NEMSIS | 60M+ EMS activations/year | All EMS responses | Free (public release) | Medium — request dataset, filter[^6] |
| NEISS | 20 years of ER visits | ~100 hospital EDs | Free (online query) | Low — run queries on cpsc.gov[^10] |
| NDI | All US deaths since 1979 | Complete national mortality | Fee-based, requires IRB | High — academic protocol needed[^14] |
| NFIRS | Fire dept. incident reports | Voluntary, national | Free (PDR download) | Medium — CSV format, filter for electrocution[^17] |

### LOA8: AI-Powered Obituary and Memorial Mining

A 2025 peer-reviewed study in JMIR demonstrated that LLM-based NLP pipelines can extract mortality information from publicly available sources with high accuracy:[^18][^19]

- **Obituaries**: 7,375,229 records mined, 96.5% accuracy for primary cause of death identification
- **GoFundMe campaigns**: 23,615 mortality-related campaigns, 95.9% accuracy
- **Memorial websites** (EverLoved, TributeArchive): 733,754 records, 98.0% accuracy

The methodology uses transformer-based models (RoBERTa achieving F1 of 0.88) to extract decedent names, dates, and cause of death, then few-shot learning with LLMs to classify cause of death. This approach is directly applicable to ESD research:[^18]

- Mine Legacy.com, EverLoved, and TributeArchive for obituaries mentioning drowning + dock/marina/electrocution
- Search GoFundMe for campaigns describing dock/marina electrocutions (a real ESD survivor campaign was found during this research — Eric Hancock, 2012 boat lift electrocution)[^20]
- Use LLM classification to flag obituaries with ESD-pattern language ("strong swimmer," "drowned at dock," "tragic accident at marina")

This approach scales to millions of records and could surface incidents that never appeared in news coverage, particularly for the pre-internet era where obituaries were the primary public record of deaths.

### LOA9: State Child Fatality Review Team Data

Every U.S. state maintains a Child Fatality Review Team (CFRT) that conducts detailed multidisciplinary reviews of child deaths. These reviews go far beyond death certificate data:[^21]

- Virginia's CFRT reviewed 52 drowning deaths (2014–2016) with detailed circumstantial analysis including supervision status, location specifics, and contributing factors[^21]
- Florida's review system documented 60 unintentional drowning deaths with similar detail[^22]
- Washington State's CDR data was used specifically for drowning surveillance research[^23]

CFRT reviews are critical for ESD because child drownings near docks are a recognized high-suspicion pattern (from the Phase 2 plan's own LOA2 criteria), and CFRTs capture the detailed circumstances needed to identify ESD indicators. Many states publish annual reports; others make data available through FOIA.

**Action**: File FOIA requests to CFRTs in the top 10 boating states (Tennessee, Arkansas, Michigan, Florida, Texas, Minnesota, Wisconsin, Virginia, North Carolina, South Carolina). Request drowning death reviews involving docks, marinas, or boat facilities.

### LOA10: GIS Proximity Analysis of Drowning Deaths and Electrical Infrastructure

Spatial analysis has been validated as a drowning prevention tool. Australian researchers used GIS-based hotspot analysis on 391 drowning deaths to identify statistically significant geographic clusters. UK researchers applied DBSCAN clustering to drowning fatalities within 500m of water networks, identifying high-priority areas.[^24][^25]

The same methodology could be applied to ESD detection:

1. Obtain drowning death coordinates from CDC WONDER (W65–W74 codes) or state vital statistics
2. Obtain marina/dock locations from USACE reservoir data, state marina permit databases, and NOAA nautical charts
3. Calculate proximity: flag all drowning deaths within 500m of registered marina or dock facilities
4. Identify statistical anomalies: locations with drowning rates significantly above expected for the water body type
5. Cross-reference anomalies with electrical infrastructure age and inspection records

This approach could quantify the "dark figure" of misclassified ESD by demonstrating that drowning rates near electrified docks are statistically elevated compared to similar water bodies without electrical infrastructure.

### LOA11: Video News Archive Mining

Many local TV news stories are preserved on YouTube but do not appear in text-based news archives. During this research, multiple ESD incidents were found with video coverage but limited or no text-based web presence. YouTube's auto-generated transcripts make this content searchable.[^26][^27]

The YouTube Data API allows programmatic searching by keyword, date range, and geographic region. A systematic search for terms like "electrocuted dock," "electric shock drowning," "marina electrocution," and "drowned dock" could surface local TV coverage of incidents that never appeared in newspaper databases. America's Boating Channel has also produced ESD-specific educational content referencing incidents.[^28]

### LOA12: Insurance and Liability Claims Data

Marina liability insurance claims represent a largely untapped source. The NFPA Fire Protection Research Foundation's Marina Risk Reduction report explicitly identified the need to "create a category in data collection databases to include injury and deaths attributable to ESD" and recommended collecting data on stray voltage at marinas. This confirms the data gap is recognized at the industry level.[^29]

Potential sources include:

- **State insurance commissioner databases**: Some states make liability claim data publicly available
- **Marina insurance underwriters**: Companies specializing in marina liability insurance track electrocution claims
- **NFIP flood insurance**: FEMA's National Flood Insurance Program documentation explicitly warns about electrocution risk during flooding, and claims data may capture flood-related electrocutions[^30]

### LOA13: Internet Archive / Wayback Machine Recovery of Deleted News Articles

Local newspaper websites frequently delete or paywall older articles. The Internet Archive's Wayback Machine has APIs that allow programmatic searching for archived versions of specific URLs or keyword-matching across archived domains. The CDX Server API allows querying by URL pattern and date range, making it possible to recover deleted articles from local news outlets in hotspot regions.[^31][^32][^33]

This is particularly valuable for the 1990s and early 2000s gap years identified in the Phase 2 plan, where local newspaper websites may have published articles online that were later removed during platform migrations.

### LOA14: Medical Examiner Training and Protocol Gap Analysis

NASBLA (National Association of State Boating Law Administrators) has developed an ESD Response and Investigation Checklist, but adoption is not universal. A systematic survey of medical examiner and coroner offices to determine whether they routinely test for electrical current in water during dock/marina drowning investigations could:[^34]

- Quantify the diagnostic gap (what percentage of jurisdictions test for ESD?)
- Identify states where ESD is most likely to be missed
- Provide evidence for policy advocacy

This would be an original research contribution and would complement the incident-finding work by explaining *why* incidents are missed.

***

## Integration with Formal Epidemiological Research

Several of these additions align with the rigor required for peer-reviewed epidemiological research:

| Research Component | Relevant LOA | Potential Output |
|-------------------|-------------|-----------------|
| Prevalence estimation | LOA7 (BARD/NEMSIS), NDI study | True ESD incidence estimate |
| Case ascertainment methodology | LOA8 (NLP mining), LOA10 (GIS) | Methods paper on ESD case finding |
| Surveillance gap analysis | LOA14 (ME/coroner survey) | Policy paper on diagnostic gaps |
| Risk factor identification | LOA10 (GIS proximity) | Spatial epidemiology study |
| Misclassification rate estimation | LOA7 + LOA10 combined | Capture-recapture prevalence model |

The BARD database is immediately actionable and could produce results within days. The NDI study would take 6–12 months to set up but would produce the most rigorous prevalence estimate possible. The NLP obituary mining approach has been peer-reviewed and published, providing methodological precedent for replication.[^1][^14][^18]

***

## Priority Recommendations

### Immediate (This Week)

1. **Download BARD data** from the Data Liberation Project — filter for electrocution deaths in boating accidents[^5][^1]
2. **Run NEISS online queries** for electrocution + water/dock/pool product codes[^10]
3. **Search GoFundMe** for "electric shock drowning," "electrocuted dock," "electrocuted marina" — mine narrative details from campaigns[^20]

### Short-Term (1–4 Weeks)

4. **Request NEMSIS public-release dataset** and filter for ESD-pattern EMS activations[^6]
5. **Download NFIRS Public Data Release** and filter for electrocution incidents near water[^17]
6. **Run YouTube API searches** for local TV coverage of dock/marina drownings[^26]
7. **Begin Wayback Machine recovery** of deleted local news articles from hotspot regions[^33]

### Medium-Term (1–3 Months)

8. **File FOIA requests** to state Child Fatality Review Teams in top 10 boating states[^21]
9. **Develop GIS proximity analysis** overlaying drowning deaths with marina locations[^24]
10. **Adapt JMIR NLP methodology** for systematic obituary mining across Legacy.com and memorial sites[^18]

### Long-Term (PhD Timeline)

11. **Design and submit NDI study protocol** for comprehensive national ESD prevalence estimation[^14]
12. **Conduct ME/coroner survey** on ESD testing protocols in dock drowning investigations[^34]
13. **Build capture-recapture model** using multiple independent data sources (BARD + NEMSIS + NEISS + news + legal) to estimate true ESD incidence

***

## Summary of All Accessible Data Sources

| Source | Type | Access | Cost | ESD Relevance |
|--------|------|--------|------|---------------|
| BARD (USCG via Data Liberation Project) | Structured DB | Public download | Free | **Very High** — direct cause-of-death filtering[^1] |
| NEMSIS | Structured DB | Research request | Free | High — EMS response data with ICD-10 codes[^6] |
| NEISS (CPSC) | Structured DB | Online query | Free | High — ER visits with narrative fields[^10] |
| NFIRS (USFA/FEMA) | Structured DB | Public download | Free | Moderate — fire dept. electrocution incidents[^17] |
| CDC WONDER | Statistical DB | Online query | Free | High — drowning/electrocution death counts by state/year |
| CDC WISQARS | Statistical DB | Online query | Free | High — electrocution fatality data |
| National Death Index | Research DB | IRB + application | Fee-based | **Very High** — definitive national mortality data[^14] |
| State CFRT Reports | Reports/data | FOIA or published | Free–Low | High — detailed child drowning circumstances[^21] |
| Legacy.com / Memorial Sites | Unstructured text | Web scraping | Free | Moderate — obituary narratives with cause-of-death[^18] |
| GoFundMe | Unstructured text | Web search | Free | Moderate — survivor/victim campaign narratives[^20] |
| YouTube (Local TV News) | Video/transcript | API search | Free | Moderate — visual coverage often not in text archives[^26] |
| Internet Archive / Wayback Machine | Archived web | API access | Free | Moderate — recovery of deleted news articles[^33] |
| Common Crawl | Archived web | Public download | Free | Low-Moderate — massive but requires significant processing[^35] |
| CourtListener | Legal records | Online search | Free | High — already in LOA3 |
| PACER | Legal records | Online search | $0.10/page | High — already in LOA3 |
| OSHA Fatality Reports | Government DB | Online search | Free | High — already in LOA4 |
| SaferProducts.gov (CPSC) | Consumer reports | Online search | Free | Moderate — already in LOA4 |
| NASBLA ESD Resources | Industry resources | Online | Free | Reference — investigation checklists[^34] |
| NDPA Research Directory | Research index | Online | Free | Reference — drowning prevention literature[^36] |
| NFPA 303 / NEC 555 Standards | Technical standards | Purchase/library | Moderate | Reference — marina electrical safety requirements |

---

## References

1. [DLP Dispatch #17](https://buttondown.com/data-liberation-project/archive/dlp-dispatch-17/) - Hello, and welcome to the 17th edition of the Data Liberation Project’s newsletter. Inside: New data...

2. [data-liberation-project/boating-accident-reports-1995-2012-muckrock](https://github.com/data-liberation-project/boating-accident-reports-1995-2012-muckrock) - The records cover accidents, deaths, injuries, and involved vessels from 1995–2012. The Coast Guard ...

3. [Tracking Boating Accidents in the United States](https://www.bespacific.com/tracking-boating-accidents-in-the-united-states/)

4. [Boating Accident Report Database](https://www.data-liberation-project.org/requests/uscg-boating-accident-report-database/) - The US Coast Guard (USCG) maintains the Boating Accident Report Database (BARD), which serves as a c...

5. [The Data Liberation Project — Datasets](https://www.data-liberation-project.org/datasets/) - Below you can find the datasets the Data Liberation Project has obtained and published. September 20...

6. [Request Research Data - NEMSIS](https://nemsis.org/using-ems-data/request-research-data/)

7. [[PDF] Data Dictionary - NEMSIS](https://nemsis.org/media/nemsis_v3/release-3.3.4/DataDictionary/PDFHTML/DEMEMS/NEMSISDataDictionary.pdf) - The NEMSIS data dictionary was developed through a collaborative effort with the EMS industry includ...

8. [Nationwide EMS Incident Datawww.ems.gov › issues › using-ems-data › nationwide-ems-incident-data](https://www.ems.gov/issues/using-ems-data/nationwide-ems-incident-data/) - Learn how the National EMS Information System (NEMSIS) does its work.

9. [NEMSIS - NIH](https://lhncbc.nlm.nih.gov/CCOI/datasets/NEMSIS/index.html)

10. [National Electronic Injury Surveillance System (NEISS)](https://www.cpsc.gov/Research--Statistics/NEISS-Injury-Data) - The primary purpose of NEISS is to collect data on consumer product-related injuries occurring in th...

11. [Usability of Emergency Department Narratives for ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC12804064/) - Objective: To determine the usability of National Electronic Injury Surveillance System All Injury P...

12. [National Electronic Injury Surveillance System](https://datacatalog.med.nyu.edu/dataset/10737) - Search the NYU Data Catalog to discover datasets generated by NYU researchers and local expertise on...

13. [[PDF] NEISS Coding Manual JULY 2023](https://www.cpsc.gov/cgibin/NEISSQuery/Data/Info%20Docs/2023%20NEISS%20Coding%20Manual.pdf) - CPSC uses a public health approach for the prevention of fatal and nonfatal injuries, including educ...

14. [National Death Index | NDI - CDC](https://www.cdc.gov/nchs/ndi/index.html) - NDI connects researchers with death records for their study participants

15. [National Death Index (NDI)](https://health.gov/healthypeople/objectives-and-data/data-sources-and-methods/data-sources/national-death-index-ndi) - The National Death Index (NDI) is a central computerized index of death record information on file i...

16. [News You Can Use: National Death Index](https://irp.nih.gov/catalyst/28/6/news-you-can-use-national-death-index)

17. [Access NFIRS data - USFA.FEMA.gov](https://www.usfa.fema.gov/nfirs/access-data/) - How to access a free, publicly-released compilation of National Fire Incident Reporting System incid...

18. [Automated Extraction of Mortality Information From Publicly Available Sources Using Large Language Models: Development and Evaluation Study](https://www.jmir.org/2025/1/e71113/) - Background: Background: Mortality is a critical variable in healthcare research, but inconsistencies...

19. [Automated Extraction of Mortality Information From Publicly ...](https://www.jmir.org/2025/1/e71113) - In this study, we developed and evaluated a pipeline combining transformer-based NLP models and FSL ...

20. [ERIC'S FAMILY REBOOT FROM TRAGEDY - GoFundMe](https://www.gofundme.com/f/erics-family-reboot-from-tragedy) - I SURVIVED EXTENDED UNDERWATER ELECTROCUTION. YES YOU READ THIS CORRECTLY. My story is complicated, ...

21. [Microsoft Word - Virginia CFRT_Drowning Review_Report Draft_V7_07.30.2019_JT.docx](https://www.vdh.virginia.gov/content/uploads/sites/18/2021/10/2019-Drowning-Report.pdf)

22. [ANNUAL REPORT - State Child Abuse Death Review Systemwww.flcadr.com › documents › 2023-FLCADR-Annual-Report](https://www.flcadr.com/documents/2023-FLCADR-Annual-Report.pdf)

23. [What CDR Does and Does Not Tell Us About Lethal Drowning Injury](https://pubmed.ncbi.nlm.nih.gov/21278094/) - Child death review (CDR) data provide the unique opportunity to identify regional risk factors and o...

24. [DROWNING RISK ASSESSMENT AND COMMUNICATION USING SPATIAL ANALYSIS](https://injuryprevention.bmj.com/content/18/Suppl_1/A70.2) - Background Spatial analysis is a widely accepted injury prevention and safety promotion tool. Dr Joh...

25. [1](https://pure.port.ac.uk/ws/portalfiles/portal/79530622/Investigating_the_spatial_clustering.pdf)

26. [Man dead after electrocution at Smith Mountain Lake dock, 2 injured trying to save him](https://www.youtube.com/watch?v=ueu_pjUDQFg) - One person is dead after a situation early Thursday morning involving electrocution at a dock at Smi...

27. [One man dead after electrocution at Virginia dock, two injured trying to save him](https://www.youtube.com/watch?v=JTD24DFphdk) - One person is dead after a situation early Thursday morning involving electrocution at a dock at Smi...

28. [Electric Shock Drowning (ESD) - YouTube](https://www.youtube.com/watch?v=BKmjWk5YZdU) - The new “Electric Shock Drowning (ESD)” video shows how ESD causes deaths and injuries at marinas na...

29. [[PDF] Marina Risk Reduction](https://www.electricshockdrowning.org/uploads/4/8/5/6/48564375/rfmarinariskreduction.pdf) - The Fire Protection Research Foundation plans, manages, and communicates research on a broad range o...

30. [[PDF] NFIP Claims Handbook](https://agents.floodsmart.gov/sites/default/files/media/document/2025-07/fema-nfip-claims-handbook-08-2024.pdf)

31. [How to access Wayback Machine programmatically? - Stack Overflow](https://stackoverflow.com/questions/33811582/how-to-access-wayback-machine-programmatically) - They key thing to understand about the Wayback Machine APIs is that there are (from what I can tell)...

32. [Access Archive-It's Wayback index with the CDX/C API](https://support.archive-it.org/hc/en-us/articles/115001790023-Access-Archive-It-s-Wayback-index-with-the-CDX-C-API) - Background Archive-It’s Wayback CDX is the index of all archived content that the Wayback browsing i...

33. [Wayback Machine APIs | Internet Archive](https://archive.org/help/wayback_api.php) - The Internet Archive Wayback Machine supports a number of different APIs to make it easier for devel...

34. [Electric Shock Drowning (ESD) Resources - NASBLA](https://www.nasbla.org/nasblamain/lighthouse/get-equipped/esd-resources) - Electric shock drownings are identified when a source of AC leakage is discovered within a given ran...

35. [Common Crawl - Open Repository of Web Crawl Data](https://commoncrawl.org) - Common Crawl is a 501(c)(3) non–profit founded in 2007. We make wholesale extraction, transformation...

36. [IMPACT ASSESSMENT STUDY](https://ndpa.org/wp-content/uploads/2023/11/NDPA-Impact-Study_Final-Report.pdf)

