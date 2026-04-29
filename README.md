# NBANewsSkill

A reusable Hermes/Codex skill for producing accurate, source-backed NBA news briefings.

## What it does

- Guides agents to verify current NBA claims with live sources.
- Separates official news, reported items, and rumors.
- Adds official scoreboard context using NBA CDN data.
- Provides templates for daily league-wide briefs and team/player updates.

## Contents

```text
nba-news/
  SKILL.md
  agents/openai.yaml
  references/source-guide.md
  scripts/nba_official.py
  templates/daily-brief.md
  templates/player-team-update.md
tests/
  test_nba_official.py
```

## Official scoreboard helper

Run from the repository root:

```bash
python3 nba-news/scripts/nba_official.py
```

Example output:

```text
As of official NBA scoreboard date: 2026-04-28

- Final: Philadelphia 76ers 113 @ Boston Celtics 97
- Final: Atlanta Hawks 97 @ New York Knicks 126

Source: https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json
```

Raw JSON mode:

```bash
python3 nba-news/scripts/nba_official.py --json
```

## Tests

```bash
PYTHONPATH=nba-news/scripts python3 -m unittest tests/test_nba_official.py -v
```

## How to use the skill

Ask an agent to use `$nba-news`, for example:

- "Use $nba-news to summarize today's NBA news with dated sources."
- "Use $nba-news to check the latest Lakers injury situation."
- "Use $nba-news to explain what changed after last night's Celtics game."

The skill should not answer current NBA questions from memory. It should verify claims with live sources and include source names, dates, and links.
