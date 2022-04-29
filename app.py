import logging
import os
from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.database import init_db, drop_db
from routes import initialize_routes
from config import Config


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
app.config['SECRET_KEY'] = Config.SECRET_KEY

bcrypt = Bcrypt(app)
jwt = JWTManager(app)
api = Api(app)
initialize_routes(api)


def main():
    drop_db()
    init_db()

    app.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"), format='%(asctime)s %(message)s')
    exit(main())
