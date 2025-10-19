from dotenv import load_dotenv
import datetime as dt

from mail import send_mail
from agent import get_mail_message
from news.news_fetcher import NewsFetcher
from news.news_filter import NewsFilter

load_dotenv()

news_fetcher = NewsFetcher()
news_fetcher.fetch()
raw_news = news_fetcher.get_news()

news_filter = NewsFilter(raw_news)
news_filter.filter_news()
news = news_filter.get_news()

today = dt.datetime.now()

message = {
    "subject": f"News Recap - {today.strftime("%A %x")}",
    "message": get_mail_message(news)
}

send_mail(message=message)