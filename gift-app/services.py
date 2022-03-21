from database.database import session
from database.models import User


class UserService:

    @staticmethod
    def get_user(id):
        return session.query(User).filter_by(user_id=id).first()

    @staticmethod
    def get_users():
        return User.query.all()

    @staticmethod
    def save_user(user):
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def delete_user(id):
        user = UserService.get_user(id)
        session.delete(user)
        session.commit()




