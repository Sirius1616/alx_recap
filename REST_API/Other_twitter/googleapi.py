import os
import logging
from datetime import datetime
from pytrends.request import TrendReq

# === Set up logging ===
logging.basicConfig(
    filename="trend_fetcher.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# === Keywords to track ===
KEYWORDS = [
    "small cap", "gainers", "breakouts", "pre-market",
    "momentum", "surge", "bullish", "rally"
]

# === Initialize pytrends ===
pytrends = TrendReq(hl='en-US', tz=360)

def fetch_trends(keywords, geo='ES'):
    logging.info("Fetching Google Trends data...")
    pytrends.build_payload(keywords, cat=0, timeframe='now 1-H', geo=geo, gprop='')
    return pytrends.interest_over_time()

def display_trends(trend_data):
    if trend_data.empty:
        print("⚠️ No trend data available.")
        logging.warning("No data returned from Google Trends.")
        return

    print("=== 📊 Real-time Stock Interest Trends (Spain) ===\n")
    for kw in KEYWORDS:
        if kw in trend_data.columns:
            interest = trend_data[kw].iloc[-1]
            print(f"🔹 {kw.title()} — Interest Level: {interest}")
    print("\n✅ Done.")

# === Main execution ===
if __name__ == "__main__":
    print("🔍 Starting trend fetcher...")
    logging.info("Started Google Trends stock topic fetcher.")
    
    try:
        data = fetch_trends(KEYWORDS)
        display_trends(data)
    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"❌ Error occurred: {e}")
