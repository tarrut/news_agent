from dotenv import load_dotenv
from mail import send_mail

load_dotenv()

message = {
    "subject": "Daily News Recap",
    "message": """
# Hello

This is a **Markdown** email.

- Item 1
- Item 2
"""
}
send_mail(message=message)