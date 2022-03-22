from flask import render_template
from flask_restful import Resource, reqparse, abort
from services import UserService
from database.models import User
import logging

log = logging.getLogger(__name__)


class Home(Resource):
    @staticmethod
    def get():
        try:
            return render_template('home.html.jinja')

        except:
            abort(500, message='Internal Server Error')


class UserResource(Resource):

    @staticmethod
    def get(id: int):
        """
        gets User with user_id matching id
        params: id:int from url path
        returns
        - Success: 200 and serialized User
        - Exception: 500
        """

        try:
            user = UserService.get_user(id)

            if not user:
                abort(404, message=f'User with id {id} does not exist')
            return user.to_dict(), 200

        except:
            abort(500, message='Internal Server Error')

    @staticmethod
    def put(id: int):
        """
        updates any number of field on user record with user_id of id
        params:
        - id:int from url path
        - name:str from request body
        returns
        - Success: 200 and serialized updated User
        - Id doesn't exist in database: 404
        - Exception: 500
        """

        try:
            if UserService.user_exists(id):
                user_put_args = reqparse.RequestParser()
                user_put_args.add_argument('name', type=str, help='name of the user', required=True)
                args = user_put_args.parse_args()

                user = UserService.update_user(id, args)
                return user.to_dict(), 200
        except:
            abort(500, message='Internal Server Error')

        abort(404, message=f'User with id {id} does not exist')


class UsersResource(Resource):
    @staticmethod
    def get():
        """
        gets all Users from database
        returns
        - success: 200 and list of all serialized Users
        - no users in database: 204
        - Exception: 500
        """

        try:
            users = UserService.get_users()
            if len(users) == 0:
                return 'no users found', 204
            return [user.to_dict() for user in users], 200

        except:
            abort(500, message='Internal Server Error')

    @staticmethod
    def post():
        """
        creates new record with name and return entire serialized User
        params:
        - name:str from request body
        returns:
        - success: 201 and serialized User
        - failure: 500
        """

        try:
            user_post_args = reqparse.RequestParser()
            user_post_args.add_argument('name', type=str, help='name of the user', required=True)
            args = user_post_args.parse_args()

            user = User(name=args.name)
            UserService.save_user(user)
            return user.to_dict(), 201

        except:
            abort(500, message='Internal Server Error')

    @staticmethod
    def delete():
        """
        deletes User with id
        params: id:int from request body
        returns:
        - success: 204
        - failure: 500
        """

        try:
            user_delete_args = reqparse.RequestParser()
            user_delete_args.add_argument('id', type=int, help='id of the user', required=True)
            args = user_delete_args.parse_args()

            UserService.delete_user(args.id)
            return 'Success', 204

        except:
            abort(500, message='Internal Server Error')


