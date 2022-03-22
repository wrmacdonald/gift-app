from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

log = logging.getLogger(__name__)

config = ConfigParser()
config.read('config/configuration.conf')
db_options = dict(config['DATABASE'])
engine = create_engine(db_options['sqlite_connection_string'])
session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
