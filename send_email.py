import smtplib, ssl
from dotenv import load_dotenv
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "pgbimpro@gmail.com"
    load_dotenv()
    password = os.getenv("EMAIL_PASSWORD")

    receiver = "pgbimpro@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
