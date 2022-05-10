from faker import Faker
from database.models import User
from database.database import session
from parameterized import parameterized
from pytest import fixture
from tests.conftest import db_session

faker = Faker()


class Test_User:
    def test_create_user(self, db_session):
        """
        create user object
        get new object id from database
        check that user exists
        """
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password()

        new_user_id = User.create(email=email,
                                  first_name=first_name,
                                  last_name=last_name,
                                  password=password,
                                  session=db_session)
        new_user = db_session.query(User).filter_by(id=new_user_id).first()

        assert new_user
        assert new_user.email == email
        assert new_user.first_name == first_name
        assert new_user.last_name == last_name
        assert new_user.password == password
        assert not new_user.confirmed
        assert not new_user.lists
        assert not new_user.groups
        assert not new_user.items
        assert not new_user.confirmed_on

    def test_user_exists(self, db_session):
        """
        create user object
        check that user exists
        """

        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password()

        user = User(email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password)

        db_session.add(user)
        db_session.commit()

        assert User.exists(user.id, db_session)


# update

# get

# delete



