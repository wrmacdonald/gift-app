from flask import Flask
from flask_restful import Api
from database.database import init_db
from resources import Home, UsersResource, UserResource

app = Flask(__name__)
api = Api(app)

api.add_resource(Home, '/')
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<id>')


if __name__ == '__main__':

    init_db()
    app.run(debug=True)


