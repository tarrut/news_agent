from dotenv import load_dotenv
from mail import send_mail
from news.elpais import fetch_elpais

load_dotenv()

message = {
    "subject": "Daily News Recap",
    "message": fetch_elpais()
}
send_mail(message=message)