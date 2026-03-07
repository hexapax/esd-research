# ACAD-034: Understanding AC Leakage Current (for NEC Panel)

| Field | Value |
|-------|-------|
| **Author/Org** | Dolan, Norton, Loftis (Maffett Loftis Engineering, LLC); prepared for Association of Marina Industries |
| **Publication** | Technical report for Association of Marina Industries (AMI), April 8, 2018 |
| **Year** | 2018 |
| **URL/DOI** | URL: https://marinaassociation.org/files/Dolan,%20Norton,%20Loftis%20-%20National%20Electrical%20Code%20Panel%20Understanding%20AC%20Leakage%20Current.pdf |
| **Type** | Industry Article / Technical Report |

## Key Technical Content

A technical paper prepared to inform NEC code panel deliberations on AC leakage current thresholds for marina environments. This is a practitioner-oriented document that synthesizes the engineering basis for the 30 mA threshold:

- **Definition of AC leakage current**: Imbalance between hot and neutral currents; the unaccounted current is flowing to ground through water, dock structures, or other unintended paths
- **Measurement methodology**: Must clamp around hot and neutral conductors together (not full cord including ground); current flowing through ground conductor will not be detected by clamping around all conductors. This is a critical point: fault current through the ground conductor evades standard GFCI measurement
- **Typical vessel leakage values**: Normal vessels: 5–20 mA; ABYC/NEC limit: 30 mA single vessel
- **Current thresholds (from Dalziel and others)**:
  - 0.5–2 mA: Perception/tingle
  - 4–6 mA: Class A GFCI trip; muscle control loss
  - 10–20 mA: Let-go threshold (cannot release grip)
  - 30 mA: NEC marina GFPE maximum for shore power receptacles
  - 100 mA: Original NEC/USCG limit (deemed inadequate)
- **Critical insight on fault current detection**: Fault current found through ground conductors would NOT trip dock receptacle ground-fault protection or boat ELCI protection. This explains why standard protection devices do not catch all fault conditions — a ground fault that routes current through the grounding conductor to water bypasses both GFCI and ELCI devices.
- **NEC evolution summary**: 2011/2014: 100 mA; 2017: reduced to 30 mA for marina supply; further reductions discussed
- **Recommendation**: GFP installation, routine logging of vessel leakage, qualified personnel only for testing

## ESD Incidents Cited

References general ESD incident data; notes that the USCG 2008 report found that "if AC leakage current is kept to less than 100 milliamps, a dangerous condition should not result" — and notes this was later revised downward to 30 mA.

## Regulatory/Legislative Impact

This technical brief was prepared specifically for NEC code panel use in 2018 — between the 2017 NEC adoption and the 2020 NEC development cycle. It provided technical justification for the tiered GFP approach adopted in NEC 2020 Article 555. The AMI (Association of Marina Industries) used this document to engage with the NEC technical committee.

## Relevance Rating

HIGH — Technical document prepared specifically to influence NEC marina electrical code. Contains the key insight about fault current through ground conductors bypassing GFCI/ELCI protection, which explains many ESD incidents where protection devices were present but did not prevent the hazard.
