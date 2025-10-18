from collections import defaultdict
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


def filter_entry(entry):
    new = {}
    for key in ("link", "title", "summary"):
        value = entry.get(key)
        if value:
            new[key] = value
    return new


def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v
                     for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v)
                        for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d