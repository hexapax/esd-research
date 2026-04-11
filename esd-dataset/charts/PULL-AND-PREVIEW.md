# Pull Latest Research and Preview Results

## Quick Start (for Claude Code Desktop App on Windows)

Open Claude Code desktop app, then paste this prompt:

```
Pull the latest changes from the esd-research repo at hexapax/esd-research,
then show me the charts in esd-dataset/charts/ and give me a summary of
what's new. Start with the research-session-2026-04-10.md file for context,
then show me the key charts: save_our_summers.png, pure_esd_key_stats.png,
pure_esd_residential_vs_marina.png, and pure_esd_period_trend.png.
```

## If You Need to Clone First

```
cd ~ && git clone https://github.com/hexapax/esd-research.git
```

Then ask Claude Code:
```
Read the file research-session-2026-04-10.md in the esd-research repo
and show me all the charts in esd-dataset/charts/ one by one.
```

## Regenerating Charts After Dataset Changes

```
cd esd-research
python3 esd-dataset/charts/generate_presentation_charts.py
python3 esd-dataset/charts/generate_pure_esd_charts.py
```
