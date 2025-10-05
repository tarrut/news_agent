import feedparser

from news.utils import is_today, filter_entry

URL =  "https://www.diaridesabadell.com/feed"

def fetch_diari_sabadell():
    feed = feedparser.parse(URL)
    interesting_entries = []

    id = 1
    for e in feed.entries:
        if is_today(e):
            interesting_entries.append(filter_entry(e, id))
            id += 1
    
    return interesting_entries