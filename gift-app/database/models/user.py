from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from database.database import Base
from database.models.base_model import BaseModel
import logging

log = logging.getLogger(__name__)


class User(Base, SerializerMixin, BaseModel):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    def __init__(self, name: str):
        self.name = name



