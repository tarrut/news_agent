from dotenv import load_dotenv
import datetime as dt

from mail import send_mail
from agent import get_mail_message
from news.news_fetcher import NewsFetcher
from news.news_filter import NewsFilter
from agents.selector_agent import SelectorAgent

load_dotenv()

# Extract news from RSS feeds
news_fetcher = NewsFetcher()
news_fetcher.fetch()
raw_news = news_fetcher.get_news()

# Filter the raw news
news_filter = NewsFilter(raw_news)
news_filter.filter_news()
news = news_filter.get_news()

# Select the most relevant news
selector_agent = SelectorAgent(news)

# today = dt.datetime.now()

# message = {
#     "subject": f"News Recap - {today.strftime("%A %x")}",
#     "message": get_mail_message(news)
# }

# send_mail(message=message)