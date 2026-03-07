# ACAD-051: ABB Technical Guide — Electric Shock in Presence of Water

| Field | Value |
|-------|-------|
| **Author/Org** | ABB (ASEA Brown Boveri Ltd.) |
| **Publication** | ABB Technical Guide, Document No. 9AKK107992A4036 |
| **Year** | 2021 (June) |
| **URL/DOI** | URL: https://library.e.abb.com/public/1c1c63dc5cff4bb49588b471ebc8467a/ABB_Electric_Shock_in_Presence_of_Water_9AKK107992A4036.pdf |
| **Type** | Industry Article / Technical Guide |

## Key Technical Content

ABB's technical guide addresses electrical shock hazards in aquatic environments from an IEC/European regulatory perspective, relevant to understanding RCD (equivalent to US GFCI/ELCI) effectiveness and the European model that has virtually eliminated ESD:

- **Three-layer protection model**: RCDs provide "additional protection" (third layer) beyond basic insulation and fault protection. In water-prone areas, RCDs are the critical third layer.
- **30 mA RCD threshold**: IEC 60364-7-701 requires all circuits with bathtubs/showers to use RCDs with rated residual operating current ≤ 30 mA (or separation transformers/Extra Low Voltage alternatives). The 30 mA limit specifically prevents ventricular fibrillation.
- **10 mA RCDs for higher-risk applications**: Recommended for sensitive applications (e.g., 230V appliances near pool zones 1 and 2), accounting for strong muscular contractions, respiratory issues, immobility, and drowning risk — making the case for even more sensitive protection
- **Water's effect on body resistance**: Water reduces body resistance to 300–600 ohms (hand-to-feet, fully wet), implying currents exceeding 500 mA at 230V if protection fails. Wet skin conductance increases to >150 S/m² and enlarges contact surface
- **"Contactless faults"**: Electrified water (puddles, pools, marina water) creates "contactless" fault conditions where the body contact point is the water surface. This is the ESD mechanism — no direct contact with a conductor is required.
- **Zoned aquatic environment rules (IEC 60364-7-701)**: Zone 0 (inside pool): IPX7-rated equipment only; Zone 1: RCDs mandatory; Zone 2: RCDs mandatory. An equivalent zoning framework for marina environments would mirror European practice.
- Saltwater noted as increasing shock severity due to higher conductivity when body-to-water current path is involved

## ESD Incidents Cited

Guide does not cite specific ESD incidents. Focused on technical protection principles from an IEC/European standards perspective.

## Regulatory/Legislative Impact

This guide demonstrates the European regulatory approach to water-environment electrical protection that has effectively eliminated ESD in European countries. The IEC 60364-7-701 requirements (mandatory 30 mA RCDs in all zones near water) correspond to what the US has progressively adopted through NEC Article 555 (2017 onwards) and ABYC E-11. The European experience — near-zero ESD with mandatory 30 mA RCDs — is the primary evidence-based argument for mandatory ELCI requirements on US vessels.

## Relevance Rating

MODERATE — Provides European/IEC technical perspective on water-environment electrical protection. Useful for understanding the regulatory context in which European ESD prevention has been essentially solved. Complements Linja-aho's Finnish fatality data (ACAD-022) showing zero ESD in a country with mandatory RCDs.
