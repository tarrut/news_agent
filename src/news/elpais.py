import feedparser

from news.utils import is_today, filter_entry, is_interesting

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

def fetch_elpais():
    feed = feedparser.parse(URL)
    interesting_entries = []

    id = 1
    for e in feed.entries:
        if is_interesting(e, INTERESTING_CATEGORIES) and is_today(e):
            interesting_entries.append(filter_entry(e, id))
            id += 1
    
    return interesting_entries
