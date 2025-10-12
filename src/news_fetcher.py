from news.elpais import fetch_elpais
from news.diarisabadell import fetch_diari_sabadell
from news.ara import fetch_ara

URLS = {
    "el_pais": fetch_elpais,
    "ara": fetch_ara,
    "diari_sabadell": fetch_diari_sabadell
}

class NewsFetcher():

    def __init__(self):
        self.news = {}
        self.fetch_news()
        self.titulars = {}

    def fetch_news(self):
        for newspaper, fetch_function in URLS.items():
            self.news[newspaper] = fetch_function()

    def get_news(self):
        if not self.news:
            self.fetch_news()
        return self.news
    
    def get_titulars(self):
        if not self.news:
            self.fetch_news()

        if not self.titulars:
            for newspaper, news in self.news.items():
                self.titulars[newspaper] = {}
                for id, new in news.items():
                    self.titulars[newspaper][id] = new["title"]
        
        return self.titulars
            
