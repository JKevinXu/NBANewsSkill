#!/usr/bin/env python3
"""Fetch and format official NBA scoreboard data.

Uses the public NBA CDN live scoreboard endpoint. The script is intentionally
stdlib-only so the skill can run in lightweight agent environments.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from datetime import date
from typing import Any

TODAYS_SCOREBOARD_URL = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"


def team_name(team: dict[str, Any]) -> str:
    city = str(team.get("teamCity") or "").strip()
    name = str(team.get("teamName") or "").strip()
    return " ".join(part for part in [city, name] if part)


def parse_scoreboard(payload: dict[str, Any]) -> list[dict[str, Any]]:
    scoreboard = payload.get("scoreboard") or {}
    games = scoreboard.get("games") or []
    summaries: list[dict[str, Any]] = []

    for game in games:
        away_team = game.get("awayTeam") or {}
        home_team = game.get("homeTeam") or {}
        summaries.append(
            {
                "status": str(game.get("gameStatusText") or game.get("gameClock") or "TBD").strip(),
                "away": team_name(away_team),
                "home": team_name(home_team),
                "away_score": int(away_team.get("score") or 0),
                "home_score": int(home_team.get("score") or 0),
            }
        )

    return summaries


def format_scoreboard(payload: dict[str, Any], source_url: str = TODAYS_SCOREBOARD_URL) -> str:
    scoreboard = payload.get("scoreboard") or {}
    game_date = scoreboard.get("gameDate") or date.today().isoformat()
    games = parse_scoreboard(payload)

    lines = [f"As of official NBA scoreboard date: {game_date}", ""]
    if not games:
        lines.append("No NBA games are listed on the official scoreboard.")
    else:
        for game in games:
            if game["away_score"] or game["home_score"]:
                lines.append(
                    f"- {game['status']}: {game['away']} {game['away_score']} @ "
                    f"{game['home']} {game['home_score']}"
                )
            else:
                lines.append(f"- {game['status']}: {game['away']} @ {game['home']}")

    lines.extend(["", f"Source: {source_url}"])
    return "\n".join(lines)


def fetch_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "NBANewsSkill/1.0 (+https://github.com/JKevinXu/NBANewsSkill)",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fetch and format the official NBA scoreboard.")
    parser.add_argument("--url", default=TODAYS_SCOREBOARD_URL, help="NBA scoreboard JSON URL")
    parser.add_argument("--json", action="store_true", help="Print raw JSON instead of formatted text")
    args = parser.parse_args(argv)

    try:
        payload = fetch_json(args.url)
    except Exception as exc:  # pragma: no cover - network failure path
        print(f"Failed to fetch NBA scoreboard: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(format_scoreboard(payload, source_url=args.url))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
