# ESD Research — Additional Data Sources Report

*Generated via Perplexity AI deep research, March 2026. This report identified 9 additional lines of attack (LOA7–LOA15) beyond the original Phase 2 plan.*

The most important finding is that the **USCG Boating Accident Report Database (BARD)** has already been FOIA'd and is freely available for download — it contains cause-of-death fields for nearly 9,000 boating fatalities across 1995–2023 that can be filtered for electrocution.

The report identifies **9 new lines of attack** organized by timeline:

- **Immediately actionable**: BARD database download/filtering, NEISS online queries, GoFundMe campaign mining
- **Short-term**: NEMSIS EMS dataset, YouTube/Wayback Machine archive recovery
- **Advanced methodology**: CDC National Death Index study (the definitive prevalence tool), medical examiner protocol survey, GIS proximity analysis

The **NDI + capture-recapture methodology** (combining BARD + NEMSIS + NEISS + news + legal records as independent sources) would produce a rigorous multi-source prevalence estimation. The 2025 JMIR paper on AI-powered obituary mining provides published methodological precedent.
<span style="display:none">[^1][^10][^100][^101][^102][^103][^104][^105][^106][^107][^108][^109][^11][^110][^111][^112][^113][^114][^115][^116][^117][^118][^119][^12][^120][^121][^122][^123][^124][^125][^126][^127][^128][^129][^13][^130][^131][^132][^133][^134][^135][^136][^137][^138][^139][^14][^140][^141][^142][^143][^144][^145][^146][^147][^148][^149][^15][^150][^151][^152][^153][^154][^155][^156][^157][^158][^159][^16][^160][^161][^162][^163][^164][^165][^166][^167][^168][^169][^17][^170][^171][^172][^173][^174][^175][^176][^177][^178][^179][^18][^180][^181][^182][^183][^184][^185][^186][^187][^188][^189][^19][^190][^191][^192][^193][^194][^195][^196][^197][^198][^199][^2][^20][^200][^201][^202][^203][^204][^205][^206][^207][^208][^209][^21][^210][^211][^212][^213][^214][^215][^216][^217][^218][^219][^22][^220][^221][^222][^223][^224][^225][^226][^227][^228][^229][^23][^230][^231][^232][^233][^24][^25][^26][^27][^28][^29][^3][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^4][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^5][^50][^51][^52][^53][^54][^55][^56][^57][^58][^59][^6][^60][^61][^62][^63][^64][^65][^66][^67][^68][^69][^7][^70][^71][^72][^73][^74][^75][^76][^77][^78][^79][^8][^80][^81][^82][^83][^84][^85][^86][^87][^88][^89][^9][^90][^91][^92][^93][^94][^95][^96][^97][^98][^99]</span>

<div align="center">⁂</div>

[^1]: https://buttondown.com/data-liberation-project/archive/dlp-dispatch-17/

[^2]: https://github.com/data-liberation-project/boating-accident-reports-1995-2012-muckrock

[^3]: https://www.bespacific.com/tracking-boating-accidents-in-the-united-states/

[^4]: https://www.data-liberation-project.org/requests/uscg-boating-accident-report-database/

[^5]: https://www.data-liberation-project.org/datasets/

[^6]: https://nemsis.org/using-ems-data/request-research-data/

[^7]: https://nemsis.org/media/nemsis_v3/release-3.3.4/DataDictionary/PDFHTML/DEMEMS/NEMSISDataDictionary.pdf

[^8]: https://www.ems.gov/issues/using-ems-data/nationwide-ems-incident-data/

[^9]: https://lhncbc.nlm.nih.gov/CCOI/datasets/NEMSIS/index.html

[^10]: https://www.cpsc.gov/Research--Statistics/NEISS-Injury-Data

[^11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12804064/

[^12]: https://datacatalog.med.nyu.edu/dataset/10737

[^13]: https://www.cpsc.gov/cgibin/NEISSQuery/Data/Info Docs/2023 NEISS Coding Manual.pdf

[^14]: https://www.cdc.gov/nchs/ndi/index.html

[^15]: https://health.gov/healthypeople/objectives-and-data/data-sources-and-methods/data-sources/national-death-index-ndi

[^16]: https://irp.nih.gov/catalyst/28/6/news-you-can-use-national-death-index

[^17]: https://www.usfa.fema.gov/nfirs/access-data/

[^18]: https://www.jmir.org/2025/1/e71113/

[^19]: https://www.jmir.org/2025/1/e71113

[^20]: https://www.gofundme.com/f/erics-family-reboot-from-tragedy

[^21]: https://www.vdh.virginia.gov/content/uploads/sites/18/2021/10/2019-Drowning-Report.pdf

[^22]: https://www.flcadr.com/documents/2023-FLCADR-Annual-Report.pdf

[^23]: https://pubmed.ncbi.nlm.nih.gov/21278094/

[^24]: https://injuryprevention.bmj.com/content/18/Suppl_1/A70.2

[^25]: https://pure.port.ac.uk/ws/portalfiles/portal/79530622/Investigating_the_spatial_clustering.pdf

[^26]: https://www.youtube.com/watch?v=ueu_pjUDQFg

[^27]: https://www.youtube.com/watch?v=JTD24DFphdk

[^28]: https://www.youtube.com/watch?v=BKmjWk5YZdU

[^29]: https://www.electricshockdrowning.org/uploads/4/8/5/6/48564375/rfmarinariskreduction.pdf

[^30]: https://agents.floodsmart.gov/sites/default/files/media/document/2025-07/fema-nfip-claims-handbook-08-2024.pdf

[^31]: https://stackoverflow.com/questions/33811582/how-to-access-wayback-machine-programmatically

[^32]: https://support.archive-it.org/hc/en-us/articles/115001790023-Access-Archive-It-s-Wayback-index-with-the-CDX-C-API

[^33]: https://archive.org/help/wayback_api.php

[^34]: https://www.nasbla.org/nasblamain/lighthouse/get-equipped/esd-resources

[^35]: https://commoncrawl.org

[^36]: https://ndpa.org/wp-content/uploads/2023/11/NDPA-Impact-Study_Final-Report.pdf

[^37]: phase2-plan.md

[^38]: esd-search-terms.md

[^39]: search-strategy.md

[^40]: README.md

[^41]: https://nationalwatersafety.org.uk/evidence-and-data

[^42]: https://www.cpsc.gov/s3fs-public/Electrocutions-2011-to-2020.pdf

[^43]: https://en.wikipedia.org/wiki/National_Violent_Death_Reporting_System

[^44]: https://theodi.org/insights/impact-stories/the-water-incident-dataset-waid-saving-lives-with-collaborative-water-data/

[^45]: https://www.cpsc.gov/Research--Statistics/Electrocutions1

[^46]: https://www.cdc.gov/nvdrs/about/index.html

[^47]: https://www.nationalwatersafety.org.uk/evidence-and-data

[^48]: https://www.cpsc.gov/recall-hazards/electrocution

[^49]: https://www.cdc.gov/comec/data-systems/nvdrs.html

[^50]: https://www.thewirh.com/blog/waid-wirh-comparison

[^51]: https://www.cpsc.gov/Newsroom/FOIA/Guide-to-Public-Information

[^52]: https://www.cdc.gov/nvdrs/media/pdfs/2025/03/nvdrs-coding-manual-version-6.1_508.pdf

[^53]: https://d-nb.info/1247877698/34

[^54]: https://www.cdc.gov/niosh/docs/98-131/default.html

[^55]: https://www.sheriffs.org/CDC’s-National-Violent-Death-Reporting-System-NVDRS

[^56]: https://www.data-liberation-project.org/datasets/uscg-boating-accident-report-database/

[^57]: https://mscnews.net/local-news/814639/drowning-concerns-grow-as-summer-approaches

[^58]: https://www.forensicmag.com/3594-All-News/619974-Genealogy-Identifies-2007-Drowning-Victim/

[^59]: https://uscgboating.org/recreational-boaters/accident-reporting.php

[^60]: https://www.nwd.usace.army.mil/media/news-releases/article/4177177/early-spate-of-drownings-raises-concerns-before-heart-of-recreation-season/

[^61]: https://www.bia.gov/service/mmu/national-missing-and-unidentified-persons-system-namus

[^62]: https://www.dco.uscg.mil/Our-Organization/Assistant-Commandant-for-Prevention-Policy-CG-5P/Inspections-Compliance-CG-5PC-/Office-of-Investigations-Casualty-Analysis/Marine-Casualty-Reports/

[^63]: https://www.cdc.gov/mmwr/preview/mmwrhtml/00016687.htm

[^64]: https://namus.nij.ojp.gov/<front>

[^65]: https://bard.knightpoint.systems/PublicInterface/Report1.aspx

[^66]: https://www.cdc.gov/MMWR/preview/mmwrhtml/00016687.htm

[^67]: https://www.namus.gov/UnidentifiedPersons/Search

[^68]: https://uscgboating.org/statistics/accident_statistics.php

[^69]: https://corpslakes.erdc.dren.mil/employees/watersafety/pdfs/FY98-23 USACE Public Recreation Fatalities Summary.pdf

[^70]: https://nij.ojp.gov/namus

[^71]: https://www.povertyactionlab.org/admindatacatalog/national-death-index

[^72]: https://www.cpsc.gov/cgibin/NEISSQuery/CaseDetail.aspx

[^73]: https://www.merrimacins.com/electric-shock-drowning-in-marinas-and-commercial-docks/

[^74]: https://injuryprevention.bmj.com/content/30/Suppl_1/A131.3

[^75]: https://www.jdsupra.com/post/fileServer.aspx?fName=5ddb6a10-9515-4ac3-b34d-199d1e8967aa.pdf

[^76]: https://www.electricshockdrowning.org/uploads/4/8/5/6/48564375/electric_shock_drowning_incident_list_5-17-22.pdf

[^77]: https://www.royallifesaving.com.au/__data/assets/pdf_file/0004/85324/RLS_NationalDrowningReport2024_WEB.pdf

[^78]: https://www.cpsc.gov/cgibin/NEISSQuery/UserCriteria.aspx

[^79]: https://www.mikeholt.com/files/PDF/Electric_Shock_Drowning_Incident_List_4-4-19.pdf

[^80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12522868/

[^81]: https://www.cpsc.gov/s3fs-public/January-2024-NEISS-CPSC-only-Coding-Manual.pdf

[^82]: http://www.augresmaritimemuseum.org/esd-hazards-learn-more-here/carmen-johnson-alabama-15-year-old-lewis-smith-lake-esd-april-16-2016/summary-of-esd-victims-74-from-1986-to-2015/

[^83]: https://www.sciencedirect.com/science/article/pii/S0379073824003335

[^84]: https://wisqars.cdc.gov/about/nonfatal-injury-data/

[^85]: https://www.mikeholt.com/files/PDF/Electric_Shock_Drowning_Incident_List_%201-30-18.pdf

[^86]: https://www.royallifesaving.com.au/sa_archive/research-and-policy/drowning-research/national-fatal-drowning-database

[^87]: https://newsinitiative.withgoogle.com/resources/trainings/google-news-archive-access-the-past/

[^88]: https://media.defense.gov/2025/Jan/10/2003626426/-1/-1/0/FOIA LOG JANUARY 1 2024 - MARCH 31 2024_REDACTED.PDF

[^89]: https://www.royallifesaving.com.au/nt/research-and-policy/drowning-research/national-fatal-drowning-database

[^90]: https://libguides.fau.edu/historical-us-newspapers/miscellaneous-newspapers

[^91]: https://www.reginfo.gov/public/do/DownloadDocument?objectID=1286401

[^92]: https://www.royallifesavingwa.com.au/research-and-impact/drowning-research/national-fatal-drowning-database

[^93]: https://www.libraryvisit.org/wp-content/uploads/sites/122/2022/07/Searching-and-Browsing-the-Google-News-Archive-REV.pdf

[^94]: https://www.reginfo.gov/public/do/DownloadDocument?objectID=27667401

[^95]: https://enddrowning.org/steps/step-1/analysis-of-secondary-data/mortuary-records-and-coroners-reports/using-coronial-data-to-investigate-drowning-deaths

[^96]: https://www.youtube.com/watch?v=OpLaSc7uxh8

[^97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6474448/

[^98]: https://www.libraryvisit.org/blogs/post/searching-and-browsing-the-google-news-archive/

[^99]: https://www.dco.uscg.mil/Our-Organization/Assistant-Commandant-for-Prevention-Policy-CG-5P/Inspections-Compliance-CG-5PC-/Office-of-Investigations-Casualty-Analysis/2692-Reporting-Forms-NVIC-01-15/

[^100]: https://marypatcampbell.substack.com/p/geeking-out-querying-the-multiple

[^101]: https://nemsis.org/wp-content/uploads/2025/08/NEMSIS-End-of-Year-Report-2024.pdf

[^102]: https://milawyersweekly.com/news/2014/06/09/personal-injury-municipal-defendants-immune-after-electrocution-death-at-marina/

[^103]: https://wonder.cdc.gov/mcd.html

[^104]: https://nemsis.org/wp-content/uploads/2025/09/2024-NEMSIS-RDS-350-User-Manual-v3.pdf

[^105]: https://wonder.cdc.gov/wonder/help/mcd.html

[^106]: https://nemsis.org/media/nemsis_v3/release-3.5.0/DataDictionary/PDFHTML/EMSDEMSTATE/NEMSISDataDictionary.pdf

[^107]: https://schaferandschaferlaw.com/blog/tragic-electrical-shock-incident-at-marina-shores-schafer-schafer-llp-files-wrongful-death-complaint/

[^108]: https://www.cdc.gov/nchs/nvss/manuals/2b-sectionv-2021.htm

[^109]: https://www.usfa.fema.gov/downloads/pdf/statistics/v22i1-fire-department-run-profile.pdf

[^110]: http://www.mmwr.com/wp-content/uploads/2017/02/7-Hartford-Fire-Insurance-Company-v-Harborview-Marina-And-Yacht-Club-Community-Ass.pdf

[^111]: https://wonder.cdc.gov/wonder/help/mcd-expanded.html

[^112]: https://nemsis.org/wp-content/uploads/2018/02/NEMSIS-RDS-221-2016-User-Manual.pdf

[^113]: https://www.linkedin.com/posts/shocktracker_insurance-lawsuit-maritime-activity-7395137149488156672-yxcp

[^114]: http://www.electricshockdrowning.org/uploads/4/8/5/6/48564375/electric_shock_drowning_incident_list_5-21-16.pdf

[^115]: https://cardinalnews.org/2024/08/07/stray-voltage-dangers-back-in-spotlight-following-smith-mountain-lake-death/

[^116]: https://www.fire-police-ems.com/books/nfpa303-2016.shtml

[^117]: https://www.gofundme.com/f/2tbpewqc

[^118]: https://stacks.cdc.gov/view/cdc/163529/cdc_163529_DS1.pdf

[^119]: https://standards.globalspec.com/std/14328130/nfpa-303

[^120]: https://www.tn.gov/commerce/news/2020/5/22/sfmo--learn-the-signs-of-electric-shock-drowning-before-boating-on-the-memorial-day-holiday.html

[^121]: https://www.fire-police-ems.com/NFPA303-2026.shtml

[^122]: http://www.electricshockdrowning.org/uploads/4/8/5/6/48564375/esd_incident_list_-_updated_5.9.16.pdf

[^123]: https://www.tn.gov/commerce/news/2021/7/7/sfmo--avoid-the-risks-of-electric-shock-drowning-when-spending--time-on-the-water-this-summer.html

[^124]: https://hsenk.ir/nfpa-303-fire-protection-standard-for-marinas-and-boatyards/

[^125]: https://www.facebook.com/groups/473790629298801/posts/6765307953480339/

[^126]: https://dbw.parks.ca.gov/crlea/Files/Electric-Shock-Drowning-The-Invisible-Killer-CRLEA.pdf

[^127]: https://docinfofiles.nfpa.org/files/AboutTheCodes/303/303_A2020_MAR_AAA_SD_SRStatements.pdf

[^128]: https://cris.biu.ac.il/en/publications/conceptualizing-social-media-sub-platforms-the-case-of-mourning-a

[^129]: https://www.linkedin.com/posts/shocktracker_esd-marinasafety-watersafety-activity-7313545868597469184-7wBj

[^130]: https://www.browse.ai

[^131]: https://academic.oup.com/jcmc/article/28/1/zmac021/6808785

[^132]: https://www.shocktracker.com

[^133]: https://thunderbit.com

[^134]: https://orca.cardiff.ac.uk/id/eprint/121377/3/Scourfield_Are%20youth%20suicide%20memorial%20sites%20on%20Facebook%20different%20from%20those%20for%20other%20sudden%20deaths.pdf

[^135]: https://safeelectricity.org/safety-tips/prevent-deadly-shocks/

[^136]: https://www.firecrawl.dev

[^137]: https://public.websites.umich.edu/~enicole/marwick\&ellison2012.pdf

[^138]: https://www.shockalert.com

[^139]: https://www.facebook.com/groups/iloveexmouth/posts/33970370419220648/

[^140]: http://chaimnoy.com/Articles/Article_Social_Network_Sites_as_Networked_Publics_Navon\&Noy2021.pdf

[^141]: https://www.practical-sailor.com/marine-electronics/preventing-electric-shock-at-the-dock/

[^142]: https://www.reddit.com/r/libraryofshadows/

[^143]: https://en.wikipedia.org/wiki/National_Fire_Incident_Reporting_System

[^144]: https://www.nfic.org/docs/osNFIRSIncidentType.pdf

[^145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10408144/

[^146]: https://apxdata.com/wp-content/uploads/2023/04/NFIRS_Spec_2015.pdf

[^147]: https://ndpa.org/drowning-facts-and-data/

[^148]: https://www.usfa.fema.gov/downloads/pdf/nfirs/nfirs_complete_reference_guide_2015.pdf

[^149]: https://www.boatsafetyscheme.org/professionals/supporting-information/risk-references/recorded-incidents/

[^150]: https://ncfrp.org/resource/data-driven-strategies-for-drowning-prevention/

[^151]: https://www.uscgboating.org/library/accident-statistics/Recreational-Boating-Statistics-2024.pdf

[^152]: https://ndpa.org/directory-drowning_lit/categories/research-study/

[^153]: https://www.clevescene.com/news/19-year-old-electrocuted-after-trying-to-save-dad-and-dog-in-put-in-bay-marina-8137076/

[^154]: http://www.electricshockdrowning.org/uploads/4/8/5/6/48564375/esdpa_incident_list_-_updated_8.15.16.pdf

[^155]: https://www.facebook.com/groups/616885411769284/posts/23947942288236934/

[^156]: https://www.electricshockdrowning.org/uploads/4/8/5/6/48564375/electric_shock_drowning_incident_list_4-4-19_-_google_docs.pdf

[^157]: http://arxiv.org/pdf/1901.09692.pdf

[^158]: https://img.ecmweb.com/files/base/ebm/ecmweb/document/2021/02/eBook_ECM_ElectricShockDrowning_EB_2018.6017f9a293bd6.pdf?dl=eBook_ECM_ElectricShockDrowning_EB_2018.6017f9a293bd6.pdf

[^159]: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0308452

[^160]: https://health.maryland.gov/phpa/Documents/Health General Article Section 5-704(b)(12)_MDH_%20Maryland%20State%20Child%20Fatali.pdf

[^161]: https://ijrpr.com/uploads/V6ISSUE8/IJRPR52258.pdf

[^162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9859480/

[^163]: https://www.ovid.com/00063364-201102001-00007

[^164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12866734/

[^165]: https://www.sciencedirect.com/science/article/pii/S2949761223000780

[^166]: https://stackoverflow.com/questions/38869741/commoncrawl-how-to-find-a-specific-web-page

[^167]: https://aclanthology.org/P13-1135.pdf

[^168]: https://www.firefightingincanada.com/nfpa-impact-august-2017-24968/

[^169]: https://www.viristar.com/post/sup-incident-illuminates-regulatory-gaps/

[^170]: https://docinfofiles.nfpa.org/files/AboutTheCodes/303/303_A2025_MAR_AAA_FDagenda_10_23.pdf

[^171]: https://commoncrawl.org/blog/web-archiving-file-formats-explained

[^172]: https://aspe.hhs.gov/enhancing-data-resources-researching-patterns-mortality-patient-centered-outcomes-research

[^173]: https://www.intertekinform.com/en-us/standards/nfpa-303-2021-829192_saig_nfpa_nfpa_3016884/

[^174]: https://www.youtube.com/watch?v=OeaI973gFjo

[^175]: https://www.infarmbureau.com/inside-story/articles/how-to-respond-to-flood-damage

[^176]: http://wayback.archive.org

[^177]: https://agents.floodsmart.gov/sites/default/files/media/document/2025-07/fema-nfip-summary-coverage-brochure-12-2023.pdf

[^178]: https://www.youtube.com/watch?v=tQgpyZuG-eo

[^179]: https://help.archive.org/help/using-the-wayback-machine/

[^180]: https://www.govinfo.gov/content/pkg/GOVPUB-FEM1-PURL-LPS19310/pdf/GOVPUB-FEM1-PURL-LPS19310.pdf

[^181]: https://www.youtube.com/watch?v=AdOQlssnAyg

[^182]: https://researchonline.ljmu.ac.uk/id/eprint/17374/8/GIS-based analysis on the spatial patterns of global maritime accidents.pdf

[^183]: https://shura.shu.ac.uk/35633/8/Hobbs-InvestigatingTheSpatialClustering(AM).pdf

[^184]: https://easts.info/2003journal/papers/0778.pdf

[^185]: https://rg3l3dr.github.io/hex-paper/

[^186]: https://github.com/continue-revolution/sd-webui-segment-anything

[^187]: https://hexatomic.github.io/static/pdf/hexatomic_project_description_website.pdf

[^188]: https://github.com/zonedb/zonedb

[^189]: https://alerenda.github.io/assets/pdf/merluzzi2023hexa.pdf

[^190]: https://gist.github.com/jeetsukumaran/1291836

[^191]: https://github.com/topics/hexapod?l=javascript\&o=asc\&s=updated

[^192]: https://github.com/okbob/pspg

[^193]: https://github.com/rasheeddo/hexapod_dev_esp32

[^194]: https://github.com/j4mie/idiorm

[^195]: https://github.com/liuzhenqi77/awesome-stars

[^196]: https://github.com/coleygroup/rxn-ebm

[^197]: https://gist.github.com/0f063223eb6cca79b947

[^198]: https://github.com/raml-org/raml-spec/blob/master/versions/raml-10/raml-10.md/

[^199]: https://gist.github.com/0xd33pstack/0f6b29b408d82c4a9f0903c70db2fe7b

[^200]: https://www.electricshockdrowning.org/esd--faq.html

[^201]: https://www.thewirh.com/blog/wir-structure

[^202]: https://bmbplawyers.com/boating-accidents-blog/how-to-protect-your-family-from-electric-shock-drowning-or-esd/

[^203]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8474860/

[^204]: https://smlassociation.org/water-safety-council-electric-shock-drowning/

[^205]: https://www.cdc.gov/Mmwr/preview/mmwrhtml/00042081.htm

[^206]: https://www.mikeholt.com/newsletters.php?action=display\&letterID=1705

[^207]: https://www.safeopedia.com/what-you-need-to-know-about-electric-shock-drowning-esd/2/4829

[^208]: https://www.techrxiv.org/users/662805/articles/676067/master/file/data/09237124/09237124.pdf?inline=true

[^209]: https://cbw.llc/wp-content/uploads/2025/02/eBook_ECM_ElectricShockDrowning_EB_2018.6017f9a293bd6.pdf

[^210]: https://www.cpsc.gov/s3fs-public/Pool-or-Spa-Submersion-Estimated-Nonfatal-Drowning-Injuries-and-Reported-Drownings-2024-Report_0.pdf

[^211]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2858216/

[^212]: https://www.cpsc.gov/s3fs-public/Pool_or_Spa_Submersion_Estimated_Nonfatal_Drowning_Injuries_and_Reported_Drownings_May_2021.pdf

[^213]: https://homeport.uscg.mil/Lists/Content/Attachments/542/Dock Allision Data.pdf

[^214]: https://www.cpsc.gov/s3fs-public/Pool-or-Spa-Submersion-Estimated-Nonfatal-Drowning-Injuries-and-Reported-Drownings-2025-Report.pdf

[^215]: https://www.youtube.com/watch?v=7y4Ru_jkBuc

[^216]: https://www.mass.gov/doc/massachusetts-boat-accident-report/download

[^217]: https://wonder.cdc.gov/wonder/help/ucd.html

[^218]: https://www.uscgboating.org/library/bui-study/BUI_Study_Final.pdf

[^219]: https://www.meowmeowfoundation.org/drowning-databases

[^220]: https://wonder.cdc.gov/deaths-by-underlying-cause.html

[^221]: https://sfm.nebraska.gov/sites/default/files/doc/nfirs50crg.pdf

[^222]: https://www.lockstownpractice.co.uk/_common/getdocument?id=332273

[^223]: https://www.electricshockdrowning.org/uploads/4/8/5/6/48564375/esd_list_-_updated_10.17.17.pdf

[^224]: https://dfs.dps.mo.gov/documents/nfirs-reference-guide.pdf

[^225]: https://s1.sos.mo.gov/Records/Archives/ArchivesMVC/Coroners/

[^226]: https://www.mikeholt.com/files/PDF/Electric_Shock_Drowning_Incident_List_5-24-24.pdf

[^227]: https://enddrowning.org/steps/step-1/analysis-of-secondary-data/mortuary-records-and-coroners-reports

[^228]: https://www.electricshockdrowning.org/uploads/4/8/5/6/48564375/esd_list_-_updated_8.15.25.pdf

[^229]: https://www.responserack.com/neris/incident-type-codes/

[^230]: https://www.miamidade.gov/global/service.page?Mduid_service=ser1469546267759560

[^231]: https://www.mikeholt.com/files/PDF/Electric_Shock_Drowning_Incident_List_5-3-23.pdf

[^232]: https://www.england.nhs.uk/patient-safety/medical-examiners/the-national-medical-examiner-system/

[^233]: https://www.osha.gov/ords/imis/accidentsearch.search?sic=\&sicgroup=\&naics=\&acc_description=\&acc_abstract=\&inspnr=\&fatal=\&officetype=\&office=\&startmonth=\&startday=\&startyear=\&endmonth=\&endday=\&endyear=\&p_start=\&p_finish=3100\&p_sort=event_date\&p_desc=ASC\&p_direction=Next\&p_show=20

