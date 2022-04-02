from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from database.database import Base
from database.models.base_model import BaseModel
from database.database import session
import logging

log = logging.getLogger(__name__)


class User(Base, SerializerMixin, BaseModel):
    __tablename__ = 'user'

    serialize_only = ('id', 'name', 'last_name',
                      'groups.id', 'groups.name',
                      'lists.id', 'lists.name',
                      'items.id', 'items.name')

    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    last_name = Column(String(254))
    lists = relationship('List')
    items = relationship('Item')
    groups = relationship('Group', secondary='user_group')


class Group(Base, SerializerMixin, BaseModel):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    owned_by_user = Column(Integer, ForeignKey('user.id'), nullable=False)
    users = relationship(User, secondary='user_group')

    # @classmethod
    # def create(cls, **kwargs):
    #     # group_id = Group.create(name=kwargs.name, owned_by_user=kwargs.user_id)
    #     group = Group(name=kwargs.name, owned_by_user=kwargs.owned_by_user)
    #     log.debug(f'saving new group with id {group.id} to the database')
    #     group.save()
    #
    #     owner = User.get(kwargs.owned_by_user)
    #     group = Group.get(group.id)
    #     owner.groups.append(group)
    #     session.add(owner)
    #     session.commit()
    #     return group.id
    # #     id = super().create(kwargs)
    # #     # group = Group.get(id=id)
    # #     # owner = User.get(group.owned_by_user)
    # #     # owner.groups.append(group)
    # #     # session.add(owner)
    # #     # session.commit()
    # #     return id


class UserGroup(Base, SerializerMixin, BaseModel):
   __tablename__ = 'user_group'
   user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
   group_id = Column(Integer, ForeignKey('group.id'), primary_key=True)


class List(Base, SerializerMixin, BaseModel):
    __tablename__ = 'list'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String(254))


class Item(Base, SerializerMixin, BaseModel):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    name = Column(String(254))



