import requests
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

if not SERPAPI_KEY:
    raise ValueError("SERPAPI Key is missing! Check your .env file.")


def get_trending_keywords(topic="artificial intelligence"):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_trends",   # search engine
        "q": topic,   # search query
        "hl": "en",   # language
        "date": "today 12-m",  # last 12 months
        "tz": "420",       #time zone
        "data_type": "RELATED_QUERIES",   #data type
        "api_key": SERPAPI_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Debug: Print raw response
    print("\n RAW RESPONSE:\n", data)

    if "related_queries" in data:
        #Filter only AI-related keywords
        keywords = [
            item["query"] for item in data["related_queries"]["top"][:10]
            if "ai" in item["query"].lower() or "artificial intelligence" in item["query"].lower()
        ]
        return keywords

    return []


