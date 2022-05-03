from string import Template
from config import Config
from email.message import EmailMessage


class EmailConfirmationMessage(EmailMessage):

    def __init__(self, token: str, recipient: str):
        super().__init__()

        url = 'http://localhost:5000/api/confirm-email/' + token
        self['Subject'] = Subjects.CONFIRMATION
        self['To'] = recipient
        self['From'] = Config.MAIL_DEFAULT_SENDER
        self.set_content(BodyTemplates.CONFIRMATION_BODY.substitute(url=url))


class Subjects:
    CONFIRMATION = "Confirm your email"


class BodyTemplates:
    CONFIRMATION_BODY = Template(
        'Welcome to the GIFT APP, thanks for signing up!\n\n'
        + 'Please follow this link to confirm your email:$url\n\n'
        + 'Thanks,\n-The gift app team')
