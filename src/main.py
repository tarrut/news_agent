from dotenv import load_dotenv
import datetime as dt

from mail import send_mail
from news.elpais import fetch_elpais
from agent import get_mail_message

load_dotenv()

news = fetch_elpais()
today = dt.datetime.now()

message = {
    "subject": f"News Recap - {today.strftime("%A %x")}",
    "message": get_mail_message(news)
}

send_mail(message=message)