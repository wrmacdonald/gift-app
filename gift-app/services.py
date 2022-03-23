from database.database import session
from database.models import User
import logging

log = logging.getLogger(__name__)


class UserService:

    @staticmethod
    def get_user(id: int) -> User:
        """
        gets user that matches user_id
        id:int user_id of user to retrieve
        returns User
        """
        log.debug(f'fetching user with id {id} users from database')
        return session.query(User).filter_by(user_id=id).first()

    @staticmethod
    def get_users() -> list:
        """returns list of every user in database"""
        log.debug(f'fetching all users from the database')
        return User.query.all()

    @staticmethod
    def save_user(user: User) -> User:
        """
        saves new user to database
        user:User - user to save
        returns User that was saved
        """
        log.debug(f'saving new user with id {user.user_id} to the database')
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

        log.debug(f'updating user {id}')
        if args.name:
            user.name = args.name
            session.add(user)
            session.commit()
        else:
            log.info(f'user {id} does not have a name, updated anyway')

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
        log.info(f'deleting user {id}')
        user = UserService.get_user(id)
        session.delete(user)
        session.commit()
        return




