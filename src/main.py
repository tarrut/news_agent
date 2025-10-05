from dotenv import load_dotenv
import datetime as dt

from mail import send_mail
from agent import get_mail_message
from news_fetcher import NewsFetcher

load_dotenv()

news_fetcher = NewsFetcher()
news = news_fetcher.get_news()

today = dt.datetime.now()

message = {
    "subject": f"News Recap - {today.strftime("%A %x")}",
    "message": get_mail_message(news)
}

send_mail(message=message)