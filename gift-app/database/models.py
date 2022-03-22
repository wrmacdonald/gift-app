from sqlalchemy import Column, Integer, String
from database.database import Base
import logging

log = logging.getLogger(__name__)


class User(Base):
    __tablename__ = 'user'
    user_id = Column('user_id', Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    def serialize(self) -> dict:
        return {self.user_id: self.name}




