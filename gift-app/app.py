import logging
import os
from flask import Flask
from flask_restful import Api
from database.database import init_db, drop_db
from resources import UsersResource, UserResource, ItemResource, ListResource, GroupResource


app = Flask(__name__)
api = Api(app)

api.add_resource(UsersResource, '/api/users')
api.add_resource(UserResource, '/api/users/<user_id>')
api.add_resource(ListResource, '/api/users/<user_id>/lists')
api.add_resource(ItemResource, '/api/users/<user_id>/items')
api.add_resource(GroupResource, '/api/users/<user_id>/groups')


def main():
    drop_db()
    init_db()

    app.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"), format='%(asctime)s %(message)s')
    exit(main())







