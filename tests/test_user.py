import pytest
from faker import Faker
from database.models import User
from database.database import session

faker = Faker()


class TestUser:
    def test_create_user(self, test_db):
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
                                  password=password)
        new_user = session.query(User).filter_by(id=new_user_id).first()

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

    def test_user_exists(self, test_db):
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

        session.add(user)
        session.commit()

        assert User.exists(user.id)

    def test_user_not_exist(self, test_db):
        """
        check that user_id 5000 does not exist
        """
        id = 5000

        assert not User.exists(id)

    def test_get_user(self, test_db):
        """
        create user and test that it can be retrieved via get
        """
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password()

        user = User(email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password)

        session.add(user)
        session.commit()

        retrieved_user = User.get(id=user.id)
        assert retrieved_user.email == email
        assert retrieved_user.first_name == first_name
        assert retrieved_user.last_name == last_name
        assert retrieved_user.password == password

    def test_get_all_users(self, test_db):
        """
        delete all rows in User table
        create num_users and then get them all from db.
        passes if the correct number of users is returned
        """
        session.query(User).delete()
        session.commit()

        num_users = 10
        for i in range(num_users):
            first_name = faker.first_name()
            last_name = faker.last_name()
            email = faker.email()
            password = faker.password()

            user = User(email=email,
                        first_name=first_name,
                        last_name=last_name,
                        password=password)

            session.add(user)
            session.commit()

        users = User.get_all()

        assert len(users) == num_users


@pytest.mark.parametrize([(5,), (1,), (0,)])
def test_get_all_users_param(self, num_users, test_db):
    """
    delete all rows in User table
    create num_users and then get them all from db.
    passes if the correct number of users is returned
    """
    session.query(User).delete()
    session.commit()

    for i in range(num_users):
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password()

        user = User(email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password)

        session.add(user)
        session.commit()

    users = User.get_all()

    assert len(users) == num_users


# update

# get

# delete
