import smtplib
from config import Config


def send_email(msg):
    """log into ssl connection to google smpt server amd snd message"""

    with smtplib.SMTP_SSL(Config.MAIL_SERVER, Config.MAIL_PORT) as smpt:
        smpt.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
        smpt.send_message(msg)
