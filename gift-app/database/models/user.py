from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from database.database import Base
from database.models.base_model import BaseModel
import logging

log = logging.getLogger(__name__)


class User(Base, SerializerMixin, BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    last_name = Column(String(254))
    lists = relationship('List')
    items = relationship('Item')

    def __init__(self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name


class List(Base, SerializerMixin, BaseModel):
    __tablename__ = 'list'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String(254))

    def __init__(self, name: str):
        self.name = name


class Item(Base, SerializerMixin, BaseModel):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String(254))

    def __init__(self, name: str, user_id: int):
        self.name = name
        self.user_id = user_id

