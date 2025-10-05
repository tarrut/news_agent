from dotenv import load_dotenv
import datetime as dt

from mail import send_mail
from news.elpais import fetch_elpais
from news.diarisabadell import fetch_diari_sabadell
from agent import get_mail_message

load_dotenv()

news = []
news.append(fetch_elpais())
news.append(fetch_diari_sabadell())

today = dt.datetime.now()

message = {
    "subject": f"News Recap - {today.strftime("%A %x")}",
    "message": get_mail_message(news)
}

send_mail(message=message)