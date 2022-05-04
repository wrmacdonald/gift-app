import unittest
from database.models import User
from database.database import session, drop_db, init_db
from parameterized import parameterized
from tests.testing import setup_db


class UserTest(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, True)

    @parameterized.expand([
        ['Bob', 'Willis', 'bobs@test.com', 'password'],
        ['Robert', 'Wilmur', 'rw@test.com', 'p@ssw0rD']
    ])
    def test_create_user(self, first_name, last_name, email, password):
        """
        create user object
        get new object id from database
        check that user exists
        """

        setup_db

        new_user_id = User.create(email=email, first_name=first_name, last_name=last_name, password=password)
        new_user = session.query(User).filter_by(id=new_user_id).first()

        self.assertIsNot(new_user, None)
        self.assertEqual(new_user.email, email)
        self.assertEqual(new_user.first_name, first_name)
        self.assertEqual(new_user.last_name, last_name)
        self.assertEqual(new_user.password, password)
        self.assertFalse(new_user.confirmed)
        self.assertEqual(new_user.lists, [])
        self.assertEqual(new_user.groups, [])
        self.assertEqual(new_user.items, [])
        self.assertFalse(new_user.confirmed_on)






# update

# get

# delete


if __name__ == '__main__':
    unittest.main()
