import unittest

from nba_official import format_scoreboard, parse_scoreboard


SAMPLE_SCOREBOARD = {
    "scoreboard": {
        "gameDate": "2026-04-29",
        "games": [
            {
                "gameId": "001",
                "gameStatusText": "Final",
                "gameClock": "",
                "homeTeam": {"teamCity": "Boston", "teamName": "Celtics", "score": 112},
                "awayTeam": {"teamCity": "New York", "teamName": "Knicks", "score": 108},
            },
            {
                "gameId": "002",
                "gameStatusText": "8:30 pm ET",
                "gameClock": "",
                "homeTeam": {"teamCity": "Los Angeles", "teamName": "Lakers", "score": 0},
                "awayTeam": {"teamCity": "Denver", "teamName": "Nuggets", "score": 0},
            },
        ],
    }
}


class TestNbaOfficial(unittest.TestCase):
    def test_parse_scoreboard_extracts_game_summaries(self):
        games = parse_scoreboard(SAMPLE_SCOREBOARD)

        self.assertEqual(
            games,
            [
                {
                    "status": "Final",
                    "away": "New York Knicks",
                    "home": "Boston Celtics",
                    "away_score": 108,
                    "home_score": 112,
                },
                {
                    "status": "8:30 pm ET",
                    "away": "Denver Nuggets",
                    "home": "Los Angeles Lakers",
                    "away_score": 0,
                    "home_score": 0,
                },
            ],
        )

    def test_format_scoreboard_includes_as_of_and_official_source(self):
        output = format_scoreboard(SAMPLE_SCOREBOARD, source_url="https://cdn.nba.com/example.json")

        self.assertIn("As of official NBA scoreboard date: 2026-04-29", output)
        self.assertIn("- Final: New York Knicks 108 @ Boston Celtics 112", output)
        self.assertIn("- 8:30 pm ET: Denver Nuggets @ Los Angeles Lakers", output)
        self.assertIn("Source: https://cdn.nba.com/example.json", output)

    def test_parse_scoreboard_handles_empty_schedule(self):
        games = parse_scoreboard({"scoreboard": {"gameDate": "2026-04-29", "games": []}})

        self.assertEqual(games, [])


if __name__ == "__main__":
    unittest.main()
