from database.models import User
from database.database import session, drop_db, init_db
from parameterized import parameterized

# @parameterized.expand([
#     ['Bob', 'Willis', 'bobw@test.com'],
#     ['Robert', 'Wilmur', 'rw@test.com'],
#     ['Ginna', 'Langford', 'gl@test.com']
#     ])
def test_create_user(self, first_name, last_name, email):
    """
    create user object
    get new object id from database
    check that user exists
    check that user exists
    """

    new_user_id = User.create(email=email, first_name=first_name, last_name=last_name,
                              password=1234, confirmed=True)

    new_user = session.query(User).filter_by(id=new_user_id).first()


if __name__ == '__main__':
    drop_db()
    init_db()
    test_create_users('Bob', 'Willis', 'bobw@test.com')
