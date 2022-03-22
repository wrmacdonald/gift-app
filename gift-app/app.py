from flask import Flask
from flask_restful import Api
from database.database import init_db
from resources import Home, UsersResource, UserResource
import logging
import os

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<id>')


def main():
    init_db()
    app.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"), format='%(asctime)s %(message)s')
    exit(main())






