from dotenv import load_dotenv

from mail import send_mail
from news.elpais import fetch_elpais
from agent import get_mail_message

load_dotenv()

news = fetch_elpais()

message = {
    "subject": "Daily News Recap",
    "message": get_mail_message(news)
}
send_mail(message=message)