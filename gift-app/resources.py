from flask import render_template
from flask_restful import Resource, reqparse, abort
from services import UserService
from database.models import User
import utils


class Home(Resource):
    @staticmethod
    def get():
        try:
            return render_template('home.html.jinja')

        except:
            abort(500, message='Internal Server Error')


class UserResource(Resource):

    @staticmethod
    def get(id):
        """gets user with id"""

        try:
            user = UserService.get_user(id)

            if not user:
                abort(404, message=f'User with id {id} does not exist')
            return user.serialize(), 200

        except:
            abort(500, message='Internal Server Error')

class UsersResource(Resource):
    @staticmethod
    def get():
        """gets all users"""

        try:
            users = UserService.get_users()
            if len(users) == 0:
                return 'no users found', 204
            return utils.serialize_list(users), 200

        except:
            abort(500, message='Internal Server Error')

    @staticmethod
    def post():
        """creates new record with name and return entire user in json"""

        try:
            user_post_args = reqparse.RequestParser()
            user_post_args.add_argument('name', type=str, help='name of the user', required=True)
            args = user_post_args.parse_args()

            user = User(name=args.name)
            UserService.save_user(user)
            return user.serialize(), 201

        except:
            abort(500, message='Internal Server Error')

    @staticmethod
    def delete():
        """deletes user record with id"""

        try:
            user_delete_args = reqparse.RequestParser()
            user_delete_args.add_argument('id', type=int, help='id of the user', required=True)
            args = user_delete_args.parse_args()

            UserService.delete_user(args.id)
            return 'Success', 204

        except:
            abort(500, message='Internal Server Error')


