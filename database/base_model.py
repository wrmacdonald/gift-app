import logging

from typing import List

from database.database import session

log = logging.getLogger(__name__)


class DatabaseActionException(Exception):
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
        except Exception as ex:
            log.error(str(ex))
            raise DatabaseActionException(ex)

    @classmethod
    def create(cls, **kwargs) -> int:
        """
        params: kwargs - dictionary of any number of variables
        creates new instance of object and saves it to the database
        returns id of new object
        """
        obj = cls(**kwargs)
        log.debug(f'saving new {cls} with id {obj.id} to the database')
        obj.save()
        return obj.id

    @classmethod
    def get_all(cls, **kwargs) -> List[object]:
        """
        returns list of all rows in the database that match kwargs
        if no arguments are given, returns all instances
        """
        try:
            log.debug(f'fetching all {cls} from the database')

            if len(kwargs) == 0:
                return cls.query.all()

            return session.query(cls).filter_by(**kwargs).all()
        except Exception as ex:
            log.error(str(ex))
            raise DatabaseActionException(ex)

    @classmethod
    def get(cls, **kwargs) -> object:
        """
        get all instances of cls filtered by kwargs
        """
        try:
            return session.query(cls).filter_by(**kwargs).first()
        except Exception as ex:
            log.error(str(ex))
            raise DatabaseActionException(ex)

    @classmethod
    def update(cls, id: int, **kwargs) -> object:
        """
        params: id - id of row
        kwargs: dictionary of any number of variables
        gets instance of object with id
        assigns all variables in kwargs to it that match attributes of the object
        ignores anything with a value of None
        and save updated object to database
        return User that was saved
        """
        try:
            user = cls.get(id=id)
            log.debug(f'updating user {id}')
            for arg in kwargs:
                if hasattr(user, arg) and kwargs[arg]:
                    setattr(user, arg, kwargs[arg])
                else:
                    log.info(f'{cls} does not have an attribute {arg}')
            user.save()
            return user
        except Exception as ex:
            log.error(str(ex))
            raise DatabaseActionException(ex)

    def save(self):
        """save to database"""
        try:
            session.add(self)
            session.commit()
        except Exception as ex:
            log.error(str(ex))
            raise DatabaseActionException(ex)

    def delete(self) -> None:
        """
        deletes row from table
        id:int - id of row to delete
        """
        try:
            log.info(f'deleting {type(self)} with id {id}')
            session.delete(self)
            session.commit()
        except Exception as ex:
            log.error(str(ex))
            raise DatabaseActionException(ex)
