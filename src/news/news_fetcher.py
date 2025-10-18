import requests
from xml.etree import ElementTree

from utils import etree_to_dict
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
            self.selected_news.append(news)

    def read_newspaper(self, newspaper_id, config):
        """Reads a single RSS feed and extracts the news

        Args:
            newspaper_id (str): Id of the newspaper
            config (dict): Configuration for fetching the newspaper

        Returns:
            (list[dict]) list of dicts with the news of the newspaper RSS feed
        """
        response = requests.get(config["url"])
        feed_processed = ElementTree.fromstring(response.content)
        feed_dict = etree_to_dict(feed_processed)
        news = feed_dict["rss"]["channel"]["item"]
        for new in news:
            new["newspaper"] = newspaper_id
        return news
    
