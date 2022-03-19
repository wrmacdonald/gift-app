from database.database import db_session
from database.models import User


class UserService:
    @staticmethod
    def get_users():
        return User.query.all()

    @staticmethod
    def save_user(user):
        db_session.add(user)
        db_session.commit()
        return user
