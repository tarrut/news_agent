import requests
from xml.etree import ElementTree

from news.utils import etree_to_dict
from config import load_config

class NewsFetcher:
    """Class for retreiving rss feeds of different newspapers
    """

    def __init__(self):
        self.selected_news = []


    def fetch(self):
        """Main method of the class that retrieves the feeds
        """
        config = load_config()
        newspapers_config = config["newspapers"]

        for newspaper_id, config in newspapers_config.items():
            news = self.read_newspaper(newspaper_id, config)
            self.selected_news.extend(news)


    def get_news(self) -> list[dict]:
        """Getter of the news parameter
        
        Returns:
            The list of news as dictionaries.
        """
        if self.news:
            return self.selected_news
            
        print("The news have not been fetched yet. Use \"NewsFetcher.fetch()\" first!")
        return

    def read_newspaper(self, newspaper_id: str, config: dict[dict]) -> list[dict]:
        """Reads a single RSS feed and extracts the news

        Args:
            newspaper_id: Id of the newspaper
            config: Configuration for fetching the newspaper

        Returns:
            list of dicts with the news of the newspaper RSS feed
        """
        response = requests.get(config["url"])
        if response.status_code != 200:
            return

        feed_processed = ElementTree.fromstring(response.content)
        feed_dict = etree_to_dict(feed_processed)
        news = feed_dict["rss"]["channel"]["item"]

        for new in news:
            new["newspaper"] = newspaper_id

        return news
    
