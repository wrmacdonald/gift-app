from database.database import session
from database.models import User


class UserService:

    @staticmethod
    def get_user(id: int) -> User:
        """
        gets user that matches user_id
        id:int user_id of user to retrieve
        returns User
        """
        return session.query(User).filter_by(user_id=id).first()

    @staticmethod
    def get_users() -> list:
        """returns list of every user in database"""
        return User.query.all()

    @staticmethod
    def save_user(user: User) -> User:
        """
        saves new user to database
        user:User - user to save
        returns User that was saved
        """
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def update_user(id: int, args) -> User:
        """
        updates user.name in database
        params:
        - id:int user_id of user to update
        - args: dictionary of new values {fieldname: newValue} to update on record
        returns updated User
        """
        user = UserService.get_user(id)

        if args.name:
            user.name = args.name
            session.add(user)
            session.commit()

        return user

    @staticmethod
    def user_exists(id: int) -> bool:
        """
        returns True if user with id exists in database
            else False
        id:int - user_id of User to check
        """
        return bool(session.query(User).filter_by(user_id=id).first())

    @staticmethod
    def delete_user(id: int) -> None:
        """
        deletes user record from database
        id:int - user_id of User to delete
        """
        user = UserService.get_user(id)
        session.delete(user)
        session.commit()
        return




