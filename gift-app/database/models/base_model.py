import logging
from database.database import session

log = logging.getLogger(__name__)


class DatabaseConnectionException(BaseException):
    pass


class BaseModel:
    @classmethod
    def exists(cls, id: int) -> bool:
        """
        params: id - id of row
        returns true if row exists in database and false if it doesn't exist
        """
        try:
            return bool(session.query(cls).filter_by(id=id).first())
        except:
            raise DatabaseConnectionException

    @classmethod
    def create(cls, **kwargs) -> int:
        """
        params: kwargs - dictionary of any number of variables
        creates new instance of object and saves it to the database
        returns id of new object
        """
        obj = cls(**kwargs)
        log.debug(f'saving new {cls} with id {id} to the database')
        obj.save()
        return obj.id

    @classmethod
    def get_all(cls) -> list:
        """
        returns list of all rows in the database
        """
        try:
            log.debug(f'fetching all {cls} from the database')
            return cls.query.all()
        except:
            raise DatabaseConnectionException

    @classmethod
    def get(cls, id):
        """
        params: id - id of row
        returns object with id
        """
        try:
            log.debug(f'fetching {cls} with id {id} users from database')
            return session.query(cls).filter_by(id=id).first()
        except:
            raise DatabaseConnectionException

    @classmethod
    def update(cls, id: int, **kwargs):
        """
        params: id - id of row
        kwargs: dictionary of any number of variables
        gets instance of object with id
        assigns all variables in kwargs to it that match attributes of the object
        and save updated object to database
        """
        try:

            user = cls.get(id)
            log.debug(f'updating user {id}')
            for arg in kwargs:
                if hasattr(user, arg):
                    setattr(user, arg, kwargs[arg])
                else:
                    log.info(f'{cls} does not have an attribute {arg}')
            user.save()
            return user
        except:
            raise DatabaseConnectionException

    def save(self):
        """save to database"""
        try:
            session.add(self)
            session.commit()
        except:
            raise DatabaseConnectionException

    def delete(self):
        """
        deletes row from table
        id:int - id of row to delete
        """
        try:
            log.info(f'deleting {type(self)} with id {id}')
            session.delete(self)
            session.commit()
        except:
            raise DatabaseConnectionException
