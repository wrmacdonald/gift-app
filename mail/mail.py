import smtplib
from config import Config
from mail.messages import Message


def send_email(recipient: str, msg: Message):

    with smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT) as smpt:
        smpt.ehlo()
        smpt.starttls()
        smpt.ehlo()

        smpt.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)

        msg = f'{msg.subject}\n\n{msg.body}'
        smpt.sendmail(Config.MAIL_DEFAULT_SENDER, recipient, msg)

