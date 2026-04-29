---
name: nba-news
description: Track, verify, and summarize NBA news with dated sources. Use when Codex is asked for latest NBA news, daily NBA briefings, team or player updates, injuries, trades, transactions, rumors, standings context, playoff implications, game takeaways, or other current NBA reporting.
---

# NBA News

## Overview

Use this skill to produce accurate, source-backed NBA news briefings. Current NBA information changes quickly, so verify recent claims with live sources before answering.

This skill now includes:

- `scripts/nba_official.py` — stdlib-only helper for official NBA scoreboard context.
- `references/source-guide.md` — source priority, claim-handling, and citation rules.
- `templates/daily-brief.md` — structure for league-wide daily briefs.
- `templates/player-team-update.md` — structure for focused team/player updates.

## Quick official scoreboard check

Before writing daily briefs or game-context answers, run:

```bash
python3 nba-news/scripts/nba_official.py
```

This fetches the official NBA CDN live scoreboard and prints a concise game summary with the source URL. Use it for scoreboard context only; still search current reporting for news, injuries, transactions, and quotes.

## Workflow

1. Resolve the scope: league-wide, team, player, game, injury, transaction, rumor, fantasy angle, or date range.
2. For current, recent, latest, today, yesterday, this week, trade, injury, lineup, standings, schedule, or playoff queries, search live sources before answering.
3. Run the official scoreboard helper when game results, upcoming games, or daily context matter:
   ```bash
   python3 nba-news/scripts/nba_official.py
   ```
4. Prefer primary and official sources first: NBA.com, team sites, official league/team communications, transaction logs, injury reports, box scores, and schedule or standings data.
5. Use reputable reporting to add context: established national outlets, local beat coverage, wire services, and direct named reporter posts when available.
6. Cross-check major claims. For trades, injuries, suspensions, lineup changes, and rumors, avoid presenting a claim as final unless an official source confirms it.
7. Include concrete dates. Convert relative dates such as today, tomorrow, and yesterday into absolute dates when useful, especially if the user may be in a different time zone.
8. Summarize the news; do not produce a link dump. Explain why each item matters for teams, players, standings, playoffs, fantasy, or roster construction when relevant.

## Source Rules

- Cite sources for news claims, including publication dates when available.
- Label unconfirmed items as `reported`, `rumored`, or `not yet official`.
- If sources conflict, state the conflict plainly and favor official confirmation over anonymous or secondary reports.
- Do not rely on memory for current rosters, standings, injuries, schedules, odds, or recent transactions.
- Use older sources only for background, and make clear when they are background rather than fresh news.
- See `references/source-guide.md` for source priority and claim-handling rules.

## Output Patterns

For a daily or latest-news brief, use `templates/daily-brief.md` and include:

- `As of`: date and, when useful, time zone.
- `Top stories`: 3-7 concise items with source links.
- `Scoreboard context`: official scoreboard helper output when relevant.
- `Why it matters`: short impact notes.
- `Watch next`: games, reports, injury designations, deadlines, or official confirmations to monitor.

For a team or player update, use `templates/player-team-update.md` and include:

- `Status`: current confirmed state.
- `Latest reporting`: newest source-backed developments.
- `Official data`: scoreboard, schedule, standings, injury, or transaction context.
- `Impact`: rotation, standings, playoff, fantasy, or contract implications.
- `Uncertainty`: what is not confirmed yet.

## Examples

- "Give me today's NBA news" -> Run official scoreboard helper, search current sources, then produce a dated league-wide brief.
- "What's the latest on the Lakers injuries?" -> Verify official injury reports and reputable beat coverage before summarizing.
- "Did that trade happen?" -> Separate official confirmation from reports and rumors.
- "What changed after last night's Celtics game?" -> Combine official scoreboard data with postgame reporting and standings context.

## Verification before answering

- Did you check live/current sources for current claims?
- Are official and reported/rumored claims clearly separated?
- Are dates explicit?
- Are links and source names included?
- Does the answer explain why each item matters rather than only listing headlines?
