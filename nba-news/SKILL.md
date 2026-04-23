---
name: nba-news
description: Track, verify, and summarize NBA news with dated sources. Use when Codex is asked for latest NBA news, daily NBA briefings, team or player updates, injuries, trades, transactions, rumors, standings context, playoff implications, game takeaways, or other current NBA reporting.
---

# NBA News

## Overview

Use this skill to produce accurate, source-backed NBA news briefings. Current NBA information changes quickly, so verify recent claims with live sources before answering.

## Workflow

1. Resolve the scope: league-wide, team, player, game, injury, transaction, rumor, fantasy angle, or date range.
2. For current, recent, latest, today, yesterday, this week, trade, injury, lineup, standings, schedule, or playoff queries, search live sources before answering.
3. Prefer primary and official sources first: NBA.com, team sites, official league/team communications, transaction logs, injury reports, box scores, and schedule or standings data.
4. Use reputable reporting to add context: established national outlets, local beat coverage, wire services, and direct named reporter posts when available.
5. Cross-check major claims. For trades, injuries, suspensions, lineup changes, and rumors, avoid presenting a claim as final unless an official source confirms it.
6. Include concrete dates. Convert relative dates such as today, tomorrow, and yesterday into absolute dates when useful, especially if the user may be in a different time zone.
7. Summarize the news; do not produce a link dump. Explain why each item matters for teams, players, standings, playoffs, fantasy, or roster construction when relevant.

## Source Rules

- Cite sources for news claims, including publication dates when available.
- Label unconfirmed items as `reported`, `rumored`, or `not yet official`.
- If sources conflict, state the conflict plainly and favor official confirmation over anonymous or secondary reports.
- Do not rely on memory for current rosters, standings, injuries, schedules, odds, or recent transactions.
- Use older sources only for background, and make clear when they are background rather than fresh news.

## Output Patterns

For a daily or latest-news brief, use:

- `As of`: date and, when useful, time zone.
- `Top stories`: 3-7 concise items with source links.
- `Why it matters`: short impact notes.
- `Watch next`: games, reports, injury designations, deadlines, or official confirmations to monitor.

For a team or player update, use:

- `Status`: current confirmed state.
- `Latest reporting`: newest source-backed developments.
- `Impact`: rotation, standings, playoff, fantasy, or contract implications.
- `Uncertainty`: what is not confirmed yet.

## Examples

- "Give me today's NBA news" -> Search current sources, then produce a dated league-wide brief.
- "What's the latest on the Lakers injuries?" -> Verify official injury reports and reputable beat coverage before summarizing.
- "Did that trade happen?" -> Separate official confirmation from reports and rumors.
- "What changed after last night's Celtics game?" -> Combine box score or schedule data with postgame reporting and standings context.
