import unittest
from database.models.models import User
from database.database import session, drop_db, init_db
from parameterized import parameterized


class UserTest(unittest.TestCase):
    """integration tests of the user model database interactions"""

    @parameterized.expand([
        ['Bob', 'Willis'],
        ['Robert', 'Wilmur']
    ])
    def test_create_user(self, name, last_name):
        """
        create user object
        get new object id from database
        check that user exists
        check that user exists
        """

        new_user_id = User.create(name=name, last_name=last_name)

        new_user = session.query(User).filter_by(id=new_user_id).first()

        self.assertIsNot(new_user, None)
        self.assertEqual(new_user.name, name)
        self.assertEqual(new_user.last_name, last_name)

    @parameterized.expand([
        ['Helma', 'Tail'],
        ['Robert', 'Wilmur']
    ])
    def test_user_exists(self, name, last_name):
        """
        create user object
        check that user exists
        """

        user = User(name=name, last_name=last_name)

        session.add(user)
        session.commit()

        exists = User.exists(user.id)

        self.assertTrue(exists)

    @parameterized.expand([[5000], [4999]])
    def test_user_not_exist(self, id):
        """make sure exists is false if user does not have a record"""

        session.query(User).delete()
        session.commit()

        self.assertFalse(User.exists(id))

    @parameterized.expand([
        ['Bob', 'Willis'],
        ['Velvet', 'Smithy']
    ])
    def test_get_user(self, name, last_name):
        """create user and test that it can be retrieved"""

        user = User(name=name, last_name=last_name)

        session.add(user)
        session.commit()

        db_user = User.get(user.id)

        self.assertEqual(db_user.id, user.id)
        self.assertEqual(db_user.name, user.name)
        self.assertEqual(db_user.last_name, user.last_name)

    @parameterized.expand([[5], [1], [0]])
    def test_get_user(self, num_users):
        """
        delete all rows in User table
        create num_users and then get them all from db.
        Passes if the correct number of users is returned
        """

        session.query(User).delete()
        session.commit()

        for i in range(num_users):
            user = User(name='test', last_name='test_last')
            session.add(user)
            session.commit()

        users = User.get_all()

        self.assertEqual(len(users), num_users)


    @parameterized.expand([
        ['Bob', 'Willis', {}],
        ['Velvet', 'Smithy', {'last_name': 'sMiThY'}],
        ['Velvet', 'Smithy', {'name': 'Velv'}],
        ['Velvet', 'Smithy', {'name': 'Velv', 'last_name': 'sMiThY'}]
    ])
    def test_update_user(self, name, last_name, new_values):
        """create user and test that it can be retrieved"""

        user = User(name=name, last_name=last_name)

        session.add(user)
        session.commit()

        updated_user = user.update(user.id, **new_values)

        self.assertEqual(updated_user.id, user.id)

        if name in new_values:
            self.assertEqual(updated_user.name, new_values.name)

        if last_name in new_values:
            self.assertEqual(updated_user.last_name, new_values.last_name)

    @parameterized.expand([
        ['Bob', 'Willis'],
        ['Velvet', 'Smithy']
    ])
    def test_delete_user(self, name, last_name):
        """create user, then delete it and make sure it does not exist anymore"""

        # create user
        user = User(name=name, last_name=last_name)

        session.add(user)
        session.commit()

        # delete user
        user.delete()

        # check it doesn't exist
        self.assertFalse(bool(session.query(User).filter_by(id=user.id).first()))


if __name__ == '__main__':
    drop_db()
    init_db()
    unittest.main()
    drop_db()

