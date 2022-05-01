import logging
from itsdangerous import URLSafeTimedSerializer
from config import Config

log = logging.getLogger(__name__)


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    return serializer.dumps(email, salt=Config.SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(Config.SECRET_KEY)
    try:
        return serializer.loads(
            token,
            salt=Config.SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
    except:
        log.error('Token confirmation failed')
        return False