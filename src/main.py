import json
from dotenv import load_dotenv

from mail import send_mail
from news.elpais import fetch_elpais

load_dotenv()

news = fetch_elpais()

message = {
    "subject": "Daily News Recap",
    "message": json.dumps(news, indent=4, ensure_ascii=False)
}
send_mail(message=message)