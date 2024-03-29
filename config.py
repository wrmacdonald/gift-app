import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config:
    """Base configuration."""

    # # database configs
    DB_HOST = os.getenv('DB_HOST')
    TEST_DB_HOST = 'sqlite:///' + os.path.join(basedir, 'tests/test.db')

    MODE = 'DEV'

    # # main config
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')

    # mail settings
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')

    # gmail authentication
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    # mail accounts
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')

    # testing
    NUM_TEST_EXECUTIONS = 3


if __name__ == '__main__':
    Config()