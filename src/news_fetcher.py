from news.elpais import fetch_elpais
from news.diarisabadell import fetch_diari_sabadell
from news.ara import fetch_ara

URLS = {
    "el_pais": fetch_elpais,
    "ara": fetch_diari_sabadell,
    "diari_sabadell": fetch_ara
}

class NewsFetcher():

    def __init__(self):
        self.news = {}
        self.fetch_news()

    def fetch_news(self):
        for newspaper, fetch_function in URLS.items():
            self.news[newspaper] = fetch_function()

    def get_news(self):
        return self.news
