# ESD Research Session: April 10, 2026

## How to Use Claude Code for Deep Research — A Worked Example

This document captures a full research session between Jeremy and Claude Code, showing the prompts, approach, and findings. It's written both as a research deliverable and as a teaching tool for Nicole on how to use Claude Code for investigative research.

---

## TL;DR for Email

**In one session, we:**
- Ran 15+ search agents across Perplexity and Brave covering every US state, waterparks, pools, fountains, storm/flood electrocutions, electric fish barriers, insurance/liability, and residential dock regulatory gaps
- Found **~55 distinct electricity-in-water incidents**, with **~15-20 not in our existing 193-entry dataset**
- Created **3 new dataset entries** (Statesboro GA wave pool, Logansport IN pool, Palm Beach Gardens FL splash pad) and **updated 1** (Jupiter FL fountain)
- Confirmed **3 major geographic gaps**: South Carolina (zero incidents ever), Oregon (zero), Wisconsin (1 from 1986)
- Documented the **marina vs residential dock regulatory chasm** — marina incidents declining after NEC 555 reforms; residential dock incidents are NOT declining because no state requires private dock inspections
- Found the **storm electrocution surveillance gap**: electrocution = 11% of indirect hurricane deaths, but unlike CO poisoning, there's zero dedicated CDC surveillance
- Built the **insurance case**: $2.3M-$100M verdicts, pool/trampoline insurance precedent, proposed "electrified dock rider" structure, de-grandfathering models from Tennessee, Missouri, and Oklahoma
- Generated **15 presentation charts** including a "Save Our Summers" hook slide comparing brain-eating amoeba to ESD
- Discovered that **electric fish barriers in recreational lakes** (Rathbun Lake, Iowa) are an emerging risk category

**Bottom line**: Regulation works at commercial marinas. Residential docks are the growing share of ESD deaths. The insurance angle and de-grandfathering strategy have strong precedent. The data supports everything Nicole needs for her presentations and the law firm engagement.

---

## The Prompts and What They Produced

### Prompt 1: The Kickoff

> Review this project and then I want to kick off a fresh broad internet search for recent incidents of ESD fatalities or near misses. I'm particularly interested in anything having to do with electricity in water (including lakes, waterparks, rivers, etc.) causing injuries or fatalities or the threat of either. I'm particularly interested in GA. Nicole, my partner on this research, thinks that Gemini can do a better job than you. I told her that you can sweet talk Perplexity and Brave into finding anything. You should review existing lines of attack and look for search terms or methods to build upon.

**What Claude did:**
1. Explored both repos (esd-research and esd-research-restricted) to understand the full project context
2. Read the search strategy docs, existing GA incidents, and search term guides
3. Launched 7 parallel searches across Perplexity Research (deep dives) and Brave (news + web):
   - Perplexity deep research on ESD incidents 2023-2026 with GA focus
   - Perplexity deep research on waterpark/pool/fountain electrocutions
   - Brave news: electrocution drowning lake dock 2024-2026
   - Brave news: Georgia electrocution water
   - Brave web: "electric shock drowning" 2024-2026
   - Brave web: Georgia lake electrocution + specific lake names
   - Brave web: waterpark pool fountain electrocution

**Key lesson for Nicole:** Start broad, name what you already know so Claude doesn't waste time re-finding it, and tell it what tools to use. The competitive framing ("Nicole thinks Gemini can do better") wasn't necessary but it was fun.

### What the First Search Found

**New Georgia incident:**
- **Splash in the Boro Wave Pool, Statesboro, GA (May 26, 2025)** — Memorial Day, ~5 swimmers shocked in wave pool, Statesboro Fire classified as "arcing, shorted electrical equipment"

**New national incidents:**
- Jupiter FL fountain (Oct 2023) — Nate Davenport killed saving kids (turned out to already be in dataset, but with updates needed)
- Logansport IN pool (Aug 2025) — 5 people shocked by submersible pump
- Palm Beach Gardens FL splash pad (2022) — 12yo Jaelyn Velez shocked
- New Rochelle NY marina (Jul 2023) — 2 shocked at boat ramp
- Lake Conroe TX (May 2024) — 3 electrocuted by downed power line

**New search angles discovered:**
- Waterparks/wave pools/splash pads — a whole category missing from ESD literature
- Public fountains — the Jupiter case is major
- Hurricane/storm flood electrocutions — Helene killed 37 in GA, how many were electrocution?

---

### Prompt 2: Scale It Up

> Create an email I can send to Nicole with my initial prompt and your response. Then also kick off more searches in other states and using a continuously evolving set of search terms as you find what produces results and then try it in different locations and scales. At the same time, update the dataset with the new entries. Kick off additional agents to flesh out the details of new events, also make sure they aren't duplicates.

**What Claude did:** Launched 8 parallel agents:

| Agent | Task | Key Findings |
|-------|------|-------------|
| Email draft | Gmail draft to Nicole | Created and ready to send |
| TX/FL/AL/SC/NC search | Known geographic gaps | Lake Conroe TX fatal, Bradenton Beach FL (Tropical Storm Eta), Florence AL pool. **South Carolina: ZERO incidents.** |
| MN/WI/WA/OR/AZ/NY/PA search | Underrepresented states | Lake Pleasant AZ double fatal (2020), Puyallup River WA (irrigation pump ESD), Cole Grad WA. **Oregon: ZERO.** |
| Waterpark/pool/fountain nationwide | Emerging category | ~24 incidents found. MGM National Harbor MD (child paralyzed), Universal Volcano Bay FL, Palm Springs CA, El Paso TX, Citrus Heights CA. |
| Statesboro GA entry | Dataset creation | ESD-2025-05-26-1.md created, no duplicate |
| Jupiter FL entry | Dataset creation | Duplicate found! Updated existing entry with ESDPA flag + 7 new sources |
| Logansport IN entry | Dataset creation | ESD-2025-08-25-1.md created, no duplicate |
| Palm Beach Gardens FL entry | Dataset creation | ESD-2022-00-00-1.md created. Agent discovered incident was actually 2022, not 2024 |

**Key lesson for Nicole:** When you have a lot of independent work to do, tell Claude to launch agents in parallel. Each agent gets its own context and search budget. The duplicate-checking instruction ("make sure they aren't duplicates") saved us from creating a redundant Jupiter FL entry.

---

### Prompt 3: Nicole's ICD Code Work + Trends + Fish Fences

> Update the email draft with storm findings. Nicole hopes to get ICD code updates to add ESD and more detailed water electrocution coding to help illuminate and then mitigate dangers. But I also want to prioritize residential dock-related incidents. I also want to see if there are trends in the data that show marina vs residential dock-related incidents are increasing/decreasing at different rates driven by different regulatory and enforcement contexts. Let's also do a search for electric fish nets and the risks of people accidentally falling in water that a fish fence is electrifying.

**What Claude did:** Launched 3 more agents + updated email:

1. **Residential dock ESD search** — Found 23 documented residential dock incidents with full details, common failure modes (boat lift corrosion #1), victim patterns (children/teens most frequent)

2. **Marina vs residential dock trend analysis** — The key finding:

   | Feature | Commercial Marina | Residential Dock |
   |---------|------------------|-----------------|
   | NEC 555 applicability | Clear, mandatory | Ambiguous |
   | 30mA GFCI | Required | Often absent |
   | Periodic inspections | Required in TN, WV | **Not required anywhere** |
   | Incidents declining? | **Yes** (post-NEC 555) | **No** |

3. **Electric fish fences/barriers** — Chicago barrier: 27.6 V/foot, >50% cardiac arrest probability. No injuries (industrial canal). **Emerging risk: Rathbun Lake, Iowa — first recreational lake barrier.**

---

### Prompt 4: Insurance Strategy

> Nicole is also hoping to work from an insurance angle. Getting an insurance company to offer an electrified dock rider (with inspection and code requirements) along with trying to get states to do more aggressive de-grandfathering and then requirement with penalty for not getting docks up to code and inspected every X years.

**What the insurance agent found:**

- **No US insurer offers a dock electrical safety product.** Market gap.
- **Verdicts: $2.3M-$100M** range
- **Pool/trampoline precedent** directly applicable (mandatory fencing, inspections, safety devices as conditions of coverage)
- **Proposed "Electrified Dock Rider":** GFCI required, annual inspection, detection devices for premium discount, cancellation for non-compliance
- **De-grandfathering models:** Osage Beach MO (any modification triggers compliance), Oklahoma GRDA (ownership transfer triggers certification)
- **International gap:** Every other developed country mandates 30mA RCDs + periodic inspections. US is the outlier.

---

### Prompt 5: Charts That Don't Dilute the Data

> I need to help her make some charts and graphs... basically slides for her presentations. She wants to make sure that the numbers are as accurate as possible. Or I should say, complete as possible. So some balance of counting everything we can to try to find some trends but also wanting to not dilute the real ESD cases.

**Solution:** Two chart sets:
- **Full dataset (196 incidents):** For legislators and public health audiences
- **Pure ESD only (151 incidents):** For dock regulators and insurers — excludes pools, fountains, power lines, storms

The pure ESD filter made the residential dock story **stronger**. Marina incidents clearly declining; residential dock incidents not declining.

---

### Prompt 6: The Hook Slide

> Can we make a slide about how the brain-eating amoeba were kind of giving us pause, but now that we have seen this data I don't want to go swimming in a lake. We need to save our summers.

**Result:** `save_our_summers.png` — side-by-side Naegleria fowleri vs ESD. Punchline: *"ESD kills 10x more people — and it's 100% preventable. Save our summers."*

---

## Files Created/Modified This Session

### New Dataset Entries
- `esd-dataset/ESD-2025-05-26-1.md` — Splash in the Boro, Statesboro GA
- `esd-dataset/ESD-2025-08-25-1.md` — Logansport IN backyard pool
- `esd-dataset/ESD-2022-00-00-1.md` — Palm Beach Gardens FL splash pad

### Updated Dataset Entries
- `esd-dataset/ESD-2023-10-22-1.md` — Jupiter FL fountain (esdpa_listed, sources, legal)

### Presentation Charts (15 total)
```
esd-dataset/charts/
  save_our_summers.png               # Hook slide: amoeba vs ESD
  key_stats.png                      # Hero: 196 | 162 | 30 | 20-30 | 75%
  fatalities_by_year.png             # Stacked by category
  monthly_distribution.png           # The July spike
  electrical_source.png              # Dock wiring #1
  residential_vs_marina.png          # The divergence
  state_distribution.png             # Top 20 states
  underreporting_stack.png           # The iceberg
  outcomes.png                       # 68% fatal
  pure_esd_key_stats.png             # Hero: 151 | 120 | 41 | 32 | 0
  pure_esd_fatalities_by_year.png    # With moving average
  pure_esd_monthly.png               # July = 34%
  pure_esd_residential_vs_marina.png # The money chart
  pure_esd_electrical_source.png     # Dock wiring dominates
  pure_esd_period_trend.png          # Rate per year
```

### Chart Generators (regenerable)
```
python3 esd-dataset/charts/generate_presentation_charts.py
python3 esd-dataset/charts/generate_pure_esd_charts.py
```

---

## Search Strategy: What Worked

| Search Approach | What It Found |
|----------------|---------------|
| `"wave pool" OR "splash pad" OR fountain + electric shock` | Statesboro GA, Jupiter FL, Palm Beach Gardens FL |
| `waterpark electrocution swimming pool submersible pump` | Logansport IN |
| `"electric shock drowning" + [state name]` | State-by-state discovery |
| `"dock electrocution" + [specific lake name]` | Residential dock incidents |
| `Hurricane [name] electrocuted flood water [state]` | Storm data |
| `"dock insurance" OR "dock liability" electrocution` | Insurance landscape |
| `NEC Article 555 + residential dock` | Regulatory gap |
| Evolving: findings from one search → terms for the next | Best technique |

---

*Session conducted April 10, 2026. Claude Opus 4.6 with Perplexity and Brave Search MCP tools. ~15 search agents, ~55 incidents found, 4 dataset changes, 15 charts, 2 email drafts.*
