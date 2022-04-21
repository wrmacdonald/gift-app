import logging
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_bcrypt import generate_password_hash, check_password_hash
from database.database import Base
from database.models.base_model import BaseModel

log = logging.getLogger(__name__)


class User(Base, SerializerMixin, BaseModel):
    __tablename__ = 'user'

    serialize_only = ('id', 'first_name', 'last_name', 'email',
                      'created_on', 'is_activated',
                      'groups.id', 'groups.name',
                      'lists.id', 'lists.name',
                      'items.id', 'items.idea')

    id = Column(Integer, primary_key=True)
    first_name = Column(String(254))
    last_name = Column(String(254))
    email = Column('email', String(254), nullable=False, unique=True)
    password = Column('password', String(254), nullable=False)
    created_on = Column(DateTime(timezone=True), server_default=func.now())
    is_activated = Column(Boolean, default=False)
    lists = relationship('List')
    items = relationship('Item', foreign_keys='Item.owned_by_user_id', back_populates='owned_by_user')
    groups = relationship('Group', secondary='user_group', back_populates='users')
#
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Group(BaseModel, Base, SerializerMixin):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(254))
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    owned_by_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    users = relationship(User, secondary='user_group', back_populates='groups')


class UserGroup(Base):
    __tablename__ = 'user_group'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'), primary_key=True)


class List(Base, SerializerMixin, BaseModel):
    __tablename__ = 'list'
    id = Column(Integer, primary_key=True)
    owned_by_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    # TODO: Add group fk
    name = Column(String(254))
    items = relationship('Item', secondary='list_item', back_populates="lists")


class Item(Base, SerializerMixin, BaseModel):
    __tablename__ = 'item'

    serialize_only = ('id', 'owned_by_user_id', 'idea', 'link',
                      'exact', 'similar', 'size', 'color',
                      'desire_level', 'time_added',
                      'is_purchased', 'time_purchased')

    id = Column(Integer, primary_key=True)
    owned_by_user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    purchased_by_user_id = Column(Integer, ForeignKey('user.id'))
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
    lists = relationship(List, secondary='list_item', back_populates="items")
    owned_by_user = relationship('User', foreign_keys='Item.owned_by_user_id', back_populates='items')
    purchased_by_user = relationship('User', foreign_keys='Item.purchased_by_user_id')


class ListItem(Base, SerializerMixin, BaseModel):
    __tablename__ = 'list_item'
    list_id = Column(Integer, ForeignKey('list.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)


#
