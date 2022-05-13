import pytest
import random
from faker import Faker
from database.models import User
from database.database import session
from config import Config
from tests.fake_data import FakeUserInfo

faker = Faker()


class TestUser:

    @pytest.mark.parametrize('exec_number', range(Config.NUM_TEST_EXECUTIONS))
    def test_create_user(self, test_db, exec_number):
        """
        create user object
        get new object id from database
        check that user exists
        """
        user_data = FakeUserInfo()
        new_user_id = User.create(**user_data.to_dict())
        new_user = session.query(User).filter_by(id=new_user_id).first()

        assert new_user
        assert new_user.email == user_data.email
        assert new_user.first_name == user_data.first_name
        assert new_user.last_name == user_data.last_name
        assert new_user.password == user_data.password
        assert not new_user.confirmed
        assert not new_user.lists
        assert not new_user.groups
        assert not new_user.items
        assert not new_user.confirmed_on

    @pytest.mark.parametrize('exec_number', range(Config.NUM_TEST_EXECUTIONS))
    def test_user_exists(self, test_db, exec_number):
        """
        create user object
        check that user exists
        """

        user_data = FakeUserInfo()
        user = User(**user_data.to_dict())

        session.add(user)
        session.commit()

        assert User.exists(user.id)

    @pytest.mark.parametrize('exec_number', range(Config.NUM_TEST_EXECUTIONS))
    def test_user_not_exist(self, test_db, exec_number):
        """
        check that user_id 5000 does not exist
        """
        session.query(User).delete()
        session.commit()

        id = random.randint(1, 100000)

        assert not User.exists(id)

    @pytest.mark.parametrize('exec_number', range(Config.NUM_TEST_EXECUTIONS))
    def test_get_user(self, test_db, exec_number):
        """
        create user and test that it can be retrieved via get
        """

        user_data = FakeUserInfo()
        user = User(**user_data.to_dict())

        session.add(user)
        session.commit()

        retrieved_user = User.get(id=user.id)
        assert retrieved_user.email == user_data.email
        assert retrieved_user.first_name == user_data.first_name
        assert retrieved_user.last_name == user_data.last_name
        assert retrieved_user.password == user_data.password

    @pytest.mark.parametrize('exec_number', range(Config.NUM_TEST_EXECUTIONS))
    def test_get_all_users(self, test_db, exec_number):
        """
        delete all rows in User table
        create num_users and then get them all from db.
        passes if the correct number of users is returned
        """
        session.query(User).delete()
        session.commit()

        num_users = random.randint(0, 10)
        for i in range(num_users):

            user_data = FakeUserInfo()
            user = User(**user_data.to_dict())

            session.add(user)
            session.commit()

        users = User.get_all()

        assert len(users) == num_users

    @pytest.mark.parametrize('update_info', [{'email': faker.email()},
                                             {'first_name': faker.first_name()},
                                             {'last_name': faker.last_name()},
                                             {'password': faker.password()},
                                             {'first_name': faker.first_name(),
                                              'last_name': faker.last_name()},
                                             {'email': faker.email(),
                                              'first_name': faker.first_name(),
                                              'last_name': faker.last_name(),
                                              'password': faker.password()}
                                             ])
    def test_update_user(self, test_db, update_info):
        """
        create user, update the user to new val, and then retrieve it from the db.
        """

        user_data = FakeUserInfo()
        user = User(**user_data.to_dict())

        session.add(user)
        session.commit()

        updated_user = User.update(id=user.id,
                                   email=update_info.get('email'),
                                   first_name=update_info.get('last_name'),
                                   last_name=update_info.get('last_name'),
                                   password=update_info.get('password'))

        if update_info.get('email'):
            assert updated_user.email == update_info['email']
        else:
            assert updated_user.email == user.email

        if update_info.get('fist_name'):
            assert updated_user.first_name == update_info['fist_name']
        else:
            assert updated_user.first_name == user.first_name

        if update_info.get('last_name'):
            assert updated_user.last_name == update_info['last_name']
        else:
            assert updated_user.last_name == user.last_name

        if update_info.get('password'):
            assert updated_user.password == update_info['password']
        else:
            assert updated_user.password == user.password

    @pytest.mark.parametrize('exec_number', range(Config.NUM_TEST_EXECUTIONS))
    def test_delete_user(self, test_db, exec_number):
        """
        create user, delete it, & test that it does not exist
        """

        user_data = FakeUserInfo()
        user = User(**user_data.to_dict())

        session.add(user)
        session.commit()

        User.delete(user)

        assert not bool(session.query(User).filter_by(id=user.id).first())
