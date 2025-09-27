import feedparser
from datetime import datetime, timezone
import json

INTERESTING_CATEGORIES = [
    "Política",
    "Europa",
    "Unión Europea",
    "España",
    "Estados Unidos",
    "Historia",
    "Tecnología",
    "Inteligencia artificial",
    "Economía",
    "Cataluña"
]

URL = "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada"


def is_interesting(entry):
    categories = [t['term'] for t in entry.get('tags', [])]
    return any(cat in INTERESTING_CATEGORIES for cat in categories) and is_today


def is_today(entry):
    dt = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %Z")
    dt = dt.replace(tzinfo=timezone.utc)
    today = datetime.now(timezone.utc).date()
    return dt.date() == today


def filter_entry(entry, id):
    return {
        "id": id,
        "link": entry["link"],
        "title": entry["title"],
        "summary": entry["summary"],
    }


def fetch_elpais():
    feed = feedparser.parse(URL)
    interesting_entries = []

    id = 1
    for e in feed.entries:
        if is_interesting(e) and is_today(e):
            interesting_entries.append(filter_entry(e, id))
            id += 1
    
    return json.dumps(interesting_entries, indent=4, ensure_ascii=False)
