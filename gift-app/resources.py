from flask_restful import Resource, reqparse, abort
from services import UserService
from database.models import User
import utils


class Home(Resource):
    def get(self):
        return 'Home'


class UserResource(Resource):

    @staticmethod
    def get(id):
        """gets user with id"""

        user = UserService.get_user(id)

        if not user:
            abort(404, message=f'User with id {id} does not exist')

        return user.serialize(), 200


class UsersResource(Resource):
    @staticmethod
    def get():
        """gets all users"""

        users = UserService.get_users()
        if len(users) == 0:
            return 'no users found', 204

        return utils.serialize_list(users), 200

    @staticmethod
    def post():
        """creates new record with name and return entire user in json"""

        user_post_args = reqparse.RequestParser()
        user_post_args.add_argument('name', type=str, help='name of the user', required=True)
        args = user_post_args.parse_args()

        user = User(name=args.name)
        UserService.save_user(user)

        return user.serialize(), 201

    @staticmethod
    def delete():
        """deletes user record with id"""

        user_delete_args = reqparse.RequestParser()
        user_delete_args.add_argument('id', type=int, help='id of the user', required=True)
        args = user_delete_args.parse_args()

        UserService.delete_user(args.id)

        return 'Success', 204



