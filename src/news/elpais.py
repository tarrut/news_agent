import feedparser
from datetime import datetime, timezone, timedelta

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
    entry_time = datetime.strptime(entry["published"], "%a, %d %b %Y %H:%M:%S %Z")
    entry_time = entry_time.replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    return (now - entry_time) <= timedelta(hours=24)


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
    
    return interesting_entries
