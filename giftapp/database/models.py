from sqlalchemy import Column, Integer, String
from database.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    def __init__(self, name: str):
        self.name = name
