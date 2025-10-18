
from news.utils import is_today

class NewsFilter:
    """Class that filters the today news and improves their format
    """

    def __init__(self, raw_news: list[dict]):
        """
        Args:
            raw_news: list of unprocessed raw news
        """
        self._raw_news = raw_news
        self.news = {}

    
    def filter_news(self):
        self.filter_news_by_date()
        self.fix_news_format()


    def filter_news_by_date(self):
        self._raw_news = [new for new in self._raw_news if is_today(new)]

    
    def fix_news_format(self):
        id = 0
        for new in self._raw_news:

            if not all(k in new for k in ("title", "link", "pubDate", "description")):
                continue

            self.news[id] = {
                "title": new.get("title"),
                "link": new.get("link"),
                "publicated": new.get("pubDate"),
                "description": new.get("description"),
                "newspaper": new.get("newspaper")
            }
            id += 1