import logging
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from database.database import Base
from database.models.base_model import BaseModel

log = logging.getLogger(__name__)


class User(Base, SerializerMixin, BaseModel):
    __tablename__ = 'user'

    serialize_only = ('id', 'name', 'last_name',
                      'groups.id', 'groups.name',
                      'lists.id', 'lists.name',
                      'items.id', 'items.name')

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    last_name = Column(String(80))
    lists = relationship('List')
    items = relationship('Item')
    groups = relationship('Group', secondary='user_group', back_populates="users")


class Group(Base, SerializerMixin, BaseModel):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    owned_by_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    users = relationship(User, secondary='user_group', back_populates="groups")


class UserGroup(Base, SerializerMixin, BaseModel):
   __tablename__ = 'user_group'
   user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
   group_id = Column(Integer, ForeignKey('group.id'), primary_key=True)


class List(Base, SerializerMixin, BaseModel):
    __tablename__ = 'list'
    id = Column(Integer, primary_key=True)
    owned_by_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String(254))


class Item(Base, SerializerMixin, BaseModel):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    owned_by_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String(254))

#
# class ListItem(Base, SerializerMixin, BaseModel):
#     __tablename__ = 'list_item'
#     id = Column(Integer, primary_key=True)
#     list_id = Column(Integer, ForeignKey('lsit.id'), primary_key=True)
#     item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)
#
#

