from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

config = ConfigParser()
config.read('config/configuration.conf')

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
engine = create_engine(DB_HOST)

session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
