from flask import request
from flask_restful import Resource, reqparse
from services import UserService
from database.models import User


class Home(Resource):
    def get(self):
        return 'Home'


class UsersResource(Resource):
    @staticmethod
    def get():
        """gets all users"""

        users = UserService.get_users()
        return [{user.id: user.name} for user in users], 200

    def post(self):
        """creates new record with name and return entire user in json"""

        user_post_args = reqparse.RequestParser()
        user_post_args.add_argument('name', type=str, help='name of the user', required=True)
        args = user_post_args.parse_args()

        user = User(args.name)
        UserService.save_user(user)

        return {user.id: user.name}, 201



