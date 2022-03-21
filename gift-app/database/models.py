from sqlalchemy import Column, Integer, String
from database.database import Base


class User(Base):
    __tablename__ = 'user'
    user_id = Column('user_id', Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    def serialize(self):
        return {self.user_id: self.name}

    @staticmethod
    def serialize_list(users):
        return [user.serialize() for user in users]



