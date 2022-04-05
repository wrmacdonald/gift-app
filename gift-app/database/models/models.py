import logging
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base
from database.models.base_model import BaseModel

log = logging.getLogger(__name__)


class User(Base, SerializerMixin, BaseModel):
    __tablename__ = 'user'

    serialize_only = ('id', 'first_name', 'last_name', 'email_address',
                      'time_created', 'is_activated', 'is_deleted',
                      'groups.id', 'groups.name',
                      'lists.id', 'lists.name',
                      'items.id', 'items.idea')

    id = Column(Integer, primary_key=True)
    first_name = Column(String(254))
    last_name = Column(String(254))
    email_address = Column(String(254))
    hashed_password = Column(String(254))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    is_activated = Column(Boolean)
    time_deleted = Column(DateTime(timezone=True))
    is_deleted = Column(Boolean, nullable=False, default=False)
    lists = relationship('List')
    items = relationship('Item')
    groups = relationship('Group', secondary='user_group', back_populates="users")


class Group(Base, SerializerMixin, BaseModel):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(254))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_deleted = Column(DateTime(timezone=True))
    is_deleted = Column(Boolean, nullable=False, default=False)
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
    items = relationship('Item', secondary='list_item', back_populates="lists")


class Item(Base, SerializerMixin, BaseModel):
    __tablename__ = 'item'

    serialize_only = ('id', 'owned_by_user', 'idea', 'link',
                      'exact', 'similar', 'size', 'color',
                      'desire_level', 'time_added',
                      'is_purchased', 'time_purchased',
                      'is_deleted', 'time_deleted')

    id = Column(Integer, primary_key=True)
    owned_by_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    # purchased_by_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    idea = Column(String(254))
    link = Column(String(254))
    exact = Column(Boolean, nullable=False, default=False)
    similar = Column(Boolean, nullable=False, default=False)
    size = Column(String(254))
    color = Column(String(254))
    desire_level = Column(Integer)
    time_added = Column(DateTime(timezone=True), server_default=func.now())
    is_purchased = Column(Boolean, nullable=False, default=False)
    time_purchased = Column(DateTime(timezone=True))
    is_deleted = Column(Boolean, nullable=False, default=False)
    time_deleted = Column(DateTime(timezone=True))
    lists = relationship(List, secondary='list_item', back_populates="items")


class ListItem(Base, SerializerMixin, BaseModel):
    __tablename__ = 'list_item'
    list_id = Column(Integer, ForeignKey('list.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)



