from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from database.database import Base
from database.models.base_model import BaseModel
import logging

log = logging.getLogger(__name__)


# class List(Base, SerializerMixin, BaseModel):
#     __tablename__ = 'list'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
#     name = Column(String(254))
#
#     def __init__(self, name: str):
#         self.name = name