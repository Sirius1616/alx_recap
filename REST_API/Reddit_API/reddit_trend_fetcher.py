#!/usr/bin/env python
import os
import json
import logging
from datetime import datetime, timezone
from dotenv import load_dotenv
import praw

# === Base Directory ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# === Load Environment Variables ===
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

# === Set Up Logging ===
LOG_FILE = os.path.join(BASE_DIR, "reddit_trend_fetcher.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === Reddit API Credentials ===
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# === Initialize Reddit Client ===
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)



# === Subreddits and Keywords ===
SUBREDDITS = ["stocks", "wallstreetbets", "investing"]
KEYWORDS = [
    "small cap", "gainers", "breakouts", "pre-market",
    "momentum", "surge", "bullish", "rally"
]

CACHE_FILE = os.path.join(BASE_DIR, "reddit_cache.json")
OUTPUT_FILE = os.path.join(BASE_DIR, "reddit_trending.txt")


def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=4)


def fetch_trending_posts():
    logging.info("Fetching trending Reddit posts...")
    results = []
    now = datetime.now(timezone.utc).isoformat()

    for sub in SUBREDDITS:
        subreddit = reddit.subreddit(sub)
        for post in subreddit.hot(limit=50):
            title = post.title.lower()
            if any(keyword in title for keyword in KEYWORDS):
                results.append({
                    "title": post.title,
                    "score": post.score,
                    "url": post.url,
                    "subreddit": sub,
                    "created_utc": datetime.fromtimestamp(post.created_utc, timezone.utc).isoformat(),
                    "id": post.id
                })
    logging.info(f"Fetched {len(results)} relevant posts.")
    return results


def enhance_posts(posts, old_cache):
    enhanced = []
    now = datetime.now(timezone.utc)

    for post in posts:
        post_id = post["id"]
        score = post["score"]
        created_time = datetime.fromisoformat(post["created_utc"])

        # Cache and Velocity logic
        previous = old_cache.get(post_id, {})
        prev_score = previous.get("score", 0)
        first_seen = previous.get("first_seen") or created_time.isoformat()

        velocity = ((score - prev_score) / prev_score * 100) if prev_score else 0
        velocity_str = f"(+{int(velocity)}% upvote velocity)" if velocity > 0 else "(steady)"
        velocity_tag = " *[High Velocity]*" if velocity >= 100 else ""

        minutes_ago = int((now - created_time).total_seconds() / 60)
        novelty = f"{minutes_ago}m ago" if minutes_ago < 60 else f"{int(minutes_ago / 60)}h ago"
        if minutes_ago <= 60:
            novelty += " *[Novel]*"

        enhanced.append({
            "title": post["title"],
            "score": score,
            "url": post["url"],
            "subreddit": post["subreddit"],
            "first_seen": novelty,
            "velocity": velocity_str + velocity_tag,
            "id": post_id
        })

    return sorted(enhanced, key=lambda x: x["score"], reverse=True)[:10]


def save_to_file(posts):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("=== Trending Reddit Posts (Stocks/Finance) ===\n\n")
        for i, p in enumerate(posts, 1):
            f.write(f"{i}. {p['title']}\n")
            f.write(f"   - 🔥 Score: {p['score']} {p['velocity']}\n")
            f.write(f"   - ⏳ First Seen: {p['first_seen']}\n")
            f.write(f"   - 🗨️ Subreddit: r/{p['subreddit']}\n")
            f.write(f"   - 🔗 URL: {p['url']}\n\n")
    logging.info(f"✅ Output saved to {OUTPUT_FILE}")


def update_cache(posts):
    now = datetime.now(timezone.utc).isoformat()
    new_cache = {}
    for p in posts:
        new_cache[p["id"]] = {
            "score": p["score"],
            "first_seen": now if "*[Novel]*" in p["first_seen"] else p["first_seen"]
        }
    save_cache(new_cache)
    logging.info("✅ Cache updated.")


# === Main Execution ===
if __name__ == "__main__":
    logging.info("🚀 Script started: Fetching Reddit trends...")
    raw_posts = fetch_trending_posts()
    if raw_posts:
        cache = load_cache()
        enhanced = enhance_posts(raw_posts, cache)
        save_to_file(enhanced)
        update_cache(enhanced)
    else:
        logging.warning("⚠️ No posts found.")
