import tweepy
import json
import os
import logging
from datetime import datetime, timezone
from dotenv import load_dotenv

# === Base Directory (for absolute file paths) ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# === Load environment variables ===
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

# === Set up logging ===
LOG_FILE = os.path.join(BASE_DIR, "trend_fetcher.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === Twitter API Credentials ===
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# === Authenticate with Twitter API using OAuth1 ===
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# === File Paths ===
CACHE_FILE = os.path.join(BASE_DIR, "trend_cache.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "trending_topics.txt")

# === Keywords to match relevant stock-related trends ===
KEYWORDS = [
    "small cap", "gainers", "breakouts", "pre-market",
    "momentum", "surge", "bullish", "rally"
]

# WOEID for Madrid, Spain
SPAIN_WOEID = 766273

def load_cache():
    """Load the cached trends from the file."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(data):
    """Save the cached trends to the file."""
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def format_trend_name(name):
    """Format the trend name for URL encoding."""
    return name.replace("$", "%24").replace(" ", "+")

def get_trending_topics(woeid=SPAIN_WOEID):
    """Fetch trending topics for a given WOEID using the Twitter API."""
    try:
        logging.info("Fetching trending topics via Tweepy...")
        trends = api.get_place_trends(id=woeid)
        logging.info(f"Fetched {len(trends[0]['trends'])} trends.")
        return trends[0]['trends']
    except Exception as e:
        logging.error(f"Error fetching trends with Tweepy: {e}")
        return []

def enhance_trends(raw_trends, old_cache):
    """Enhance the raw trend data with calculated metrics."""
    current_time = datetime.now(timezone.utc)
    enhanced = []

    for trend in raw_trends:
        name = trend['name']
        if not any(k.lower() in name.lower() for k in KEYWORDS):
            continue

        volume = trend.get('tweet_volume', 0) or 0
        url = f"https://twitter.com/search?q={format_trend_name(name)}"

        previous = old_cache.get(name, {})
        prev_volume = previous.get("volume", 0)
        first_seen = previous.get("first_seen") or current_time.isoformat()

        velocity_pct = ((volume - prev_volume) / prev_volume * 100) if prev_volume else 0
        velocity_str = f"(+{int(velocity_pct)}% in 1h)" if velocity_pct > 0 else "(Steady)"
        velocity_tag = " *[High Velocity]*" if velocity_pct >= 100 else ""

        seen_time = datetime.fromisoformat(first_seen)
        minutes_ago = int((current_time - seen_time).total_seconds() / 60)
        if minutes_ago <= 60:
            novelty = f"{minutes_ago}m ago *[Novel]*"
        elif minutes_ago < 240:
            novelty = f"{int(minutes_ago / 60)}h ago"
        else:
            novelty = f"{int(minutes_ago / 60)}h ago *[Less Novel]*"

        enhanced.append({
            "name": name,
            "volume": volume,
            "velocity": velocity_str + velocity_tag,
            "first_seen": novelty,
            "url": url
        })

    logging.info("Enhancing trends...")
    return sorted(enhanced, key=lambda x: x['volume'], reverse=True)[:10]

def save_to_file(trends):
    """Write the enhanced trend data to a readable plain text file."""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("=== Trending Stocks (Madrid, Spain) ===\n\n")
        for i, t in enumerate(trends, start=1):
            f.write(f"{i}. {t['name']}\n")
            f.write(f"   - 📊 Volume: {t['volume']} tweets {t['velocity']}\n")
            f.write(f"   - ⏳ First seen: {t['first_seen']}\n")
            f.write(f"   - 🔗 URL: {t['url']}\n\n")
    logging.info(f"✅ Output saved to {OUTPUT_FILE}")

def update_cache(trends):
    """Update the cache with the latest trend volumes."""
    now = datetime.now(timezone.utc).isoformat()
    new_cache = {}
    for t in trends:
        new_cache[t["name"]] = {
            "volume": t["volume"],
            "first_seen": now if "*[Novel]*" in t["first_seen"] else t["first_seen"]
        }
    save_cache(new_cache)
    logging.info("✅ Cache updated.")

# === Main Execution ===
if __name__ == "__main__":
    logging.info("🔍 Script started: Fetching and analyzing trending stock topics...")
    raw = get_trending_topics()
    if raw:
        cache = load_cache()
        processed = enhance_trends(raw, cache)
        save_to_file(processed)
        update_cache(processed)
    else:
        logging.warning("⚠️ No trends found.")
