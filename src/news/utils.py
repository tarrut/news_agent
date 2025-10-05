from datetime import datetime, timezone, timedelta

def is_interesting(entry, interesting_categories):
    categories = [t['term'] for t in entry.get('tags', [])]
    return any(cat in interesting_categories for cat in categories) and is_today


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