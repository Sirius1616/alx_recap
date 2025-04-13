import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
from datetime import datetime, timedelta, timezone

# Import the functions to test (make sure the path is correct)
from get_trending_topic import (
    load_cache,
    save_cache,
    format_trend_name,
    get_trending_topics,
    enhance_trends,
    save_to_file,
    update_cache
)

class TestGetTrendingTopics(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"trend": {"volume": 100}}')
    @patch("os.path.exists", return_value=True)
    def test_load_cache(self, mock_exists, mock_file):
        cache = load_cache()
        self.assertIn("trend", cache)
        self.assertEqual(cache["trend"]["volume"], 100)

    @patch("builtins.open", new_callable=mock_open)
    def test_save_cache(self, mock_file):
        data = {"trend": {"volume": 200}}
        save_cache(data)
        mock_file().write.assert_called()  # Ensure write was called

    def test_format_trend_name(self):
        self.assertEqual(format_trend_name("small cap"), "small+cap")
        self.assertEqual(format_trend_name("$stock"), "%24stock")

    @patch("get_trending_topic.api.get_place_trends")
    def test_get_trending_topics(self, mock_get):
        # Mocking a successful response from the Twitter API
        mock_get.return_value = [
            {
                'trends': [
                    {"name": "Small Cap Gainers", "tweet_volume": 5000},
                    {"name": "Market Surge", "tweet_volume": 10000}
                ]
            }
        ]

        trends = get_trending_topics(766273)  # Use Madrid WOEID for testing
        self.assertEqual(len(trends), 2)
        self.assertEqual(trends[0]['name'], "Small Cap Gainers")
        self.assertEqual(trends[0]['tweet_volume'], 5000)

    def test_enhance_trends(self):
        now = datetime.now(timezone.utc)
        raw_trends = [{"name": "Small Cap Rally", "tweet_volume": 500}]
        old_cache = {
            "Small Cap Rally": {
                "volume": 250,
                "first_seen": (now - timedelta(minutes=30)).isoformat()
            }
        }
        enhanced = enhance_trends(raw_trends, old_cache)
        self.assertEqual(len(enhanced), 1)
        self.assertIn("velocity", enhanced[0])
        self.assertIn("*[High Velocity]*", enhanced[0]["velocity"])

    @patch("builtins.open", new_callable=mock_open)
    def test_save_to_file(self, mock_file):
        trends = [
            {
                "name": "Small Cap Gainers",
                "volume": 5000,
                "velocity": "(+10% in 1h)",
                "first_seen": "5m ago",
                "url": "https://twitter.com/search?q=Small+Cap+Gainers"
            }
        ]
        save_to_file(trends)
        mock_file().write.assert_called()  # Ensure write was called

    @patch("get_trending_topic.save_cache")
    def test_update_cache(self, mock_save_cache):
        trends = [{"name": "Momentum Surge", "volume": 800, "first_seen": "10m ago *[Novel]*"}]
        update_cache(trends)
        mock_save_cache.assert_called_once()
        saved_data = mock_save_cache.call_args[0][0]
        self.assertIn("Momentum Surge", saved_data)
        self.assertIn("volume", saved_data["Momentum Surge"])

if __name__ == "__main__":
    unittest.main()
