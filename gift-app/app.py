from flask import Flask
from flask_restful import Api
from database.database import init_db, drop_db
from resources import Home, UsersResource, UserResource, ItemResource, ListResource, GroupResource
import logging
import os

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<id>')
api.add_resource(ListResource, '/users/<id>/lists')
api.add_resource(ItemResource, '/users/<user_id>/items')
api.add_resource(GroupResource, '/users/<user_id>/groups')


def main():
    drop_db()
    init_db()

    app.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"), format='%(asctime)s %(message)s')
    exit(main())







