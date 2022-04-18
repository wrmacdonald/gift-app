import logging
import os
from flask import Flask
from flask_restful import Api
from database.database import init_db, drop_db
from resources.user import UserResource
from resources.item import ItemResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/api/users')
api.add_resource(ItemResource, '/api/items')


def main():
    drop_db()
    init_db()

    app.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"), format='%(asctime)s %(message)s')
    exit(main())







