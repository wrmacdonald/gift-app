from flask import Flask
from flask_restful import Api
from database.database import init_db
from database.models import User
from services import UserService
from resources import HelloWorld, UserResource

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(UserResource, '/user')

if __name__ == '__main__':

    init_db()

    matt = User('Matt')
    wes = User('Wes')
    UserService.save_user(matt)
    UserService.save_user(wes)

    app.run(debug=True)


