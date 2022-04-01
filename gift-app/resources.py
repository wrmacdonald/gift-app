from flask import render_template
from flask_restful import Resource, reqparse, abort
from database.models.user import User
from database.models.base_model import DatabaseConnectionException
import logging

log = logging.getLogger(__name__)


class Home(Resource):
    @staticmethod
    def get():
        return render_template('home.html.jinja')


class UserResource(Resource):

    @staticmethod
    def get(id: int):
        """
        gets User with user_id matching id
        params: id:int from url path
        returns
        - Success: 200 and serialized User
        - no such user exists: 404
        - Exception: 500
        """
        try:
            if not User.exists(id):
                return {'message': f'User with id {id} does not exist'}, 404

            user = User.get(id)

            if not user:
                abort(404, message=f'User with id {id} does not exist')

            return user.to_dict(), 200

        except DatabaseConnectionException:
            abort(500, message='Internal Service Error')

    @staticmethod
    def put(id: int):
        """
        updates any number of field on user record with user_id of id
        params:
        - id:int from url path
        - name:str from request body
        - last_name:str from request body
        returns
        - Success: 200 and serialized updated User
        - Id doesn't exist in database: 404
        """
        try:
            if not User.exists(id):
                return {'message': f'User with id {id} does not exist'}, 404

            user_put_args = reqparse.RequestParser()
            user_put_args.add_argument('name', type=str, help='name of the user is required', required=True)
            user_put_args.add_argument('last_name', type=str, help='last name of the user', required=True)

            args = user_put_args.parse_args()
            user = User.update(id, **args)

            return user.to_dict(), 200

        except DatabaseConnectionException:
            abort(500, message='Internal Service Error')


class UsersResource(Resource):
    @staticmethod
    def get():
        """
        gets all Users from database
        returns
        - success: 200 and list of all serialized Users
        - no users in database: 204
        """

        try:
            users = User.get_all()
            if len(users) == 0:
                return 'no users found', 204

            return [user.to_dict() for user in users], 200

        except DatabaseConnectionException:
            abort(500, message='Internal Service Error')

    @staticmethod
    def post():
        """
        creates new record with name and return entire serialized User
        params:
        - name:str from request body
        - last_name:str from request body
        returns:
        - success: 201 and serialized User
        """

        try:
            user_post_args = reqparse.RequestParser()
            user_post_args.add_argument('name', type=str, help='name of the user is required', required=True)
            user_post_args.add_argument('last_name', type=str, help='last name of the user', required=True)
            args = user_post_args.parse_args()

            id = User.create(name=args.name, last_name=args.last_name)
            user = User.get(id)
            return user.to_dict(), 201

        except DatabaseConnectionException:
            abort(500, message='Internal Service Error')

    @staticmethod
    def delete():
        """
        deletes User with id
        params: id:int from request body
        returns:
        - user does not exist: 404
        - success: 204
        """

        try:
            user_delete_args = reqparse.RequestParser()
            user_delete_args.add_argument('id', type=int, help='id of the user is required', required=True)
            args = user_delete_args.parse_args()

            if not User.exists(args.id):
                return {'message': f'User with id {args.id} does not exist'}, 404

            user = User.get(args.id)
            user.delete()

            return 'Success', 204

        except DatabaseConnectionException:
            abort(500, message='Internal Service Error')




