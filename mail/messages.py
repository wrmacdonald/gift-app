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


class EmailInviteMessage(EmailMessage):

    def __init__(self, group_id: int, recipient: str, group_name: str):
        super().__init__()

        login_url = f'http://127.0.0.1:5000/api/auth/login?group_id={group_id}'
        signup_url = f'http://127.0.0.1:5000/api/auth/signup?group_id={group_id}'
        self['Subject'] = Subjects.INVITE
        self['To'] = recipient
        self['From'] = Config.MAIL_DEFAULT_SENDER
        self.set_content(BodyTemplates.INVITATION_BODY.substitute(login_url=login_url,
                                                                  signup_url=signup_url,
                                                                  group_name=group_name))


class Subjects:
    CONFIRMATION = "Confirm your email"
    INVITE = "You're invited a Gift group"


class BodyTemplates:
    CONFIRMATION_BODY = Template(
        'Welcome to the GIFT APP, thanks for signing up!\n\n'
        + 'Please follow this link to confirm your email:$url\n\n'
        + 'Thanks,\n-The gift app team')

    INVITATION_BODY = Template(
        'You\'ve been invited to join the group "$group_name" on the GIFT APP!\n\n'
        + 'If you already have an account, please follow this link to join the group: $login_url\n\n'
        + 'If you do not already have an account, please follow this link to create an account '
          '& join the group: $signup_url\n\n'
        + 'Thanks,\n-The gift app team')
