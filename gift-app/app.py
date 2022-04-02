from flask import Flask
from flask_restful import Api
from database.database import init_db, drop_db, session
from database.models.models import User, Group
from resources import Home, UsersResource, UserResource, ItemResource, GroupResource
import logging
import os

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<id>')
# api.add_resource(ListResource, 'users/<id>/lists')
api.add_resource(ItemResource, '/users/<user_id>/items')
api.add_resource(GroupResource, '/users/<user_id>/groups')


def main():
    drop_db()
    init_db()
    # d1 = User(name="Accounts")
    # d2 = User(name="Sales")
    # d3 = User(name="Marketing")
    #
    # e1 = Group(name="John")
    # e2 = Group(name="Tony")
    # e3 = Group(name="Graham")
    #
    # e1.users.append(d1)
    # e2.users.append(d3)
    # d1.groups.append(e3)
    # d2.groups.append(e2)
    # d3.groups.append(e1)
    # e3.users.append(d2)
    #
    # session.add(e1)
    # session.add(e2)
    # session.add(d1)
    # session.add(d2)
    # session.add(d3)
    # session.add(e3)
    # session.commit()
    app.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"), format='%(asctime)s %(message)s')
    exit(main())







