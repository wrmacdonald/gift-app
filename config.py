import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration."""

    # database configs
    DB_HOST = os.getenv('DB_HOST')

    # # main config
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    # DEBUG = os.getenv('DEBUG')
    # BCRYPT_LOG_ROUNDS = os.getenv('BCRYPT_LOG_ROUNDS')
    # WTF_CSRF_ENABLED = os.getenv('WTF_CSRF_ENABLED')
    # DEBUG_TB_ENABLED = os.getenv('DEBUG_TB_ENABLED')
    # DEBUG_TB_INTERCEPT_REDIRECTS = os.getenv('DEBUG_TB_INTERCEPT_REDIRECTS')
    #
    # # mail settings
    # MAIL_SERVER = os.getenv('MAIL_SERVER')
    # MAIL_PORT = os.getenv('MAIL_PORT')
    # MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    # MAIL_USE_SSL = os.getenv('MAIL_USE_SSL')
    #
    # # gmail authentication
    # MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    # MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    #
    # # mail accounts
    # v = os.getenv('MAIL_DEFAULT_SENDER')
