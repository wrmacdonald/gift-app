import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration."""

    # app configs
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')

    # database configs
    DB_HOST = os.getenv('DB_HOST')

    # # main config
    # SECRET_KEY = 'my_precious'
    # SECURITY_PASSWORD_SALT = 'my_precious_two'
    # DEBUG = False
    # BCRYPT_LOG_ROUNDS = 13
    # WTF_CSRF_ENABLED = True
    # DEBUG_TB_ENABLED = False
    # DEBUG_TB_INTERCEPT_REDIRECTS = False
    #
    # # mail settings
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 465
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True
    #
    # # gmail authentication
    # MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    # MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']
    #
    # # mail accounts
    # MAIL_DEFAULT_SENDER = 'from@example.com'