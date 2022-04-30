import smtplib
from config import Config


def send_email(recipient: str, subject: str, body: str):

    with smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT) as smpt:
        smpt.ehlo()
        smpt.starttls()
        smpt.ehlo()

        smpt.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)

        msg = f'{subject}\n\n{body}'
        smpt.sendmail(Config.MAIL_DEFAULT_SENDER, recipient, msg)

