class Message:
    def __init__(self, body, subject):
        self.body = body
        self.subject = subject


class ActivateAccountMessage(Message):
    def __init__(self, token):
        url = 'http://localhost:5000/api/activate/' + token
        body = f'Welcome! Thanks for signing up. Please follow this link to activate your account:{url}\n\nThanks!'
        subject = "Please confirm your email"
        super().__init__(body, subject)
