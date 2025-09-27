import smtplib
import os
import email.utils
from email.mime.text import MIMEText
import markdown


def send_mail(message: dict[str, str]):
    html_content = markdown.markdown(message["message"])

    sender = os.getenv("SENDER_MAIL")
    receiver = os.getenv("RECEIVER_MAIL")
    password = os.getenv("PASSWORD_MAIL")

    msg = MIMEText(html_content, "html")
    msg["To"] = email.utils.formataddr(("Recipient", receiver))
    msg["From"] = email.utils.formataddr(("Author", sender))
    msg["Subject"] = message["subject"]

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.set_debuglevel(True)
    try:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, [receiver], msg.as_string())
    finally:
        server.quit()