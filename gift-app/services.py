from database.database import session
from database.models import User


class UserService:

    @staticmethod
    def get_user(id: int) -> User:
        return session.query(User).filter_by(user_id=id).first()

    @staticmethod
    def get_users() -> list:
        return User.query.all()

    @staticmethod
    def save_user(user: User) -> User:
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def update_user(id: int, args) -> User:
        user = UserService.get_user(id)

        if args.name:
            user.name = args.name
            session.add(user)
            session.commit()

        return user

    @staticmethod
    def user_exists(id: int) -> bool:
        return bool(session.query(User).filter_by(user_id=id).first())

    @staticmethod
    def delete_user(id: int) -> None:
        user = UserService.get_user(id)
        session.delete(user)
        session.commit()
        return




