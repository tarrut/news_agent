from datetime import datetime, timezone, timedelta
from dateutil import parser

def is_interesting(entry, interesting_categories):
    categories = [t['term'] for t in entry.get('tags', [])]
    return any(cat in interesting_categories for cat in categories) and is_today


def is_today(entry):
    entry_time = parser.parse(entry["published"])

    if entry_time.tzinfo is None:
        entry_time = entry_time.replace(tzinfo=timezone.utc)
    else:
        entry_time = entry_time.astimezone(timezone.utc)
    
    now = datetime.now(timezone.utc)
    return (now - entry_time) <= timedelta(hours=24)


def filter_entry(entry, id_):
    new = {"id": id_}
    for key in ("link", "title", "summary"):
        value = entry.get(key)
        if value:
            new[key] = value
    return new
