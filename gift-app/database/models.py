from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from database.database import Base
import logging

log = logging.getLogger(__name__)


class User(Base, SerializerMixin):
    __tablename__ = 'user'
    user_id = Column('user_id', Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)

    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name






