from dotenv import load_dotenv
import datetime as dt

from mail import send_mail
from agent import get_mail_message
from news.elpais import fetch_elpais
from news.diarisabadell import fetch_diari_sabadell
from news.ara import fetch_ara

load_dotenv()

news = []
news.append(fetch_elpais())
news.append(fetch_diari_sabadell())
news.append(fetch_ara())

today = dt.datetime.now()

message = {
    "subject": f"News Recap - {today.strftime("%A %x")}",
    "message": get_mail_message(news)
}

send_mail(message=message)