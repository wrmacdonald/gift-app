from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
import logging

log = logging.getLogger(__name__)

load_dotenv()
# DB_HOST = os.getenv("DB_HOST")
# engine = create_engine(DB_HOST)

# connect to mySQL server
DB_HOST2 = os.getenv("DB_HOST2")
engine = create_engine(DB_HOST2)

session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
