import logging
from flask_restful import Resource, reqparse
from database.models.models import User, Item, Group, List
from database.models.base_model import DatabaseConnectionException

log = logging.getLogger(__name__)


class UserResource(Resource):

    @staticmethod
    def get(user_id: int):
        """
        gets User with user_id matching id
        params: id:int from url path
        returns
        - Success: 200 and serialized User
        - no such user exists: 404
        - Exception: 500
        """
        try:
            if not User.exists(user_id):
                return {'message': f'User with id {user_id} does not exist'}, 404

            user = User.get(user_id)

            return user.to_dict(), 200

        except DatabaseConnectionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500

    @staticmethod
    def put(user_id: int):
        """
        updates any number of field on user record with user_id of id
        params:
        - id:int from url path
        - first_name:str from request body
        - last_name:str from request body
        returns
        - Success: 200 and serialized updated User
        - Id doesn't exist in database: 404
        """
        try:
            if not User.exists(user_id):
                return {'message': f'User with id {user_id} does not exist'}, 404

            user_put_args = reqparse.RequestParser()
            user_put_args.add_argument('first_name', type=str, help='first name of the user is required', required=True)
            user_put_args.add_argument('last_name', type=str, help='last name of the user', required=True)

            args = user_put_args.parse_args()
            user = User.update(user_id, **args)

            return user.to_dict(), 200

        except DatabaseConnectionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500


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

        except DatabaseConnectionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500

    @staticmethod
    def post():
        """
        creates new record and return entire serialized User
        params:
        - first_name:str from request body
        - last_name:str from request body
        returns:
        - success: 201 and serialized User
        """

        try:
            user_post_args = reqparse.RequestParser()
            user_post_args.add_argument('first_name', type=str, help='first name of the user is required', required=True)
            user_post_args.add_argument('last_name', type=str, help='last name of the user is required', required=True)
            args = user_post_args.parse_args()

            id = User.create(first_name=args.first_name, last_name=args.last_name)
            user = User.get(id)
            return user.to_dict(), 201

        except DatabaseConnectionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500

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

        except DatabaseConnectionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500


class ListResource(Resource):
    @staticmethod
    def post(user_id: int):
        try:
            if not User.exists(user_id):
                return {'message': f'User with id {user_id} does not exist'}, 404

            user_post_args = reqparse.RequestParser()
            user_post_args.add_argument('name', type=str, help='name of the list is required', required=True)
            args = user_post_args.parse_args()

            id = List.create(name=args.name, owned_by_user=user_id)
            user = User.get(id)
            return user.to_dict(), 201

        except DatabaseConnectionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500


class ItemResource(Resource):
    @staticmethod
    def post(user_id: int):

        try:
            if not User.exists(user_id):
                return {'message': f'No user with id {user_id}'}, 400

            item_post_args = reqparse.RequestParser()
            item_post_args.add_argument('name', type=str, help='name of the item is required', required=True)
            args = item_post_args.parse_args()

            item_id = Item.create(name=args.name, owned_by_user=user_id)
            item = Item.get(item_id)
            return item.to_dict(), 201

        except DatabaseConnectionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500


class GroupResource(Resource):
    @staticmethod
    def post(user_id: int):
        try:
            if not User.exists(user_id):
                return {'message': f'No user with id {user_id}'}, 400

            group_post_args = reqparse.RequestParser()
            group_post_args.add_argument('name', type=str, help='name of the group is required', required=True)
            args = group_post_args.parse_args()

            group_id = Group.create(name=args.name, owned_by_user=user_id)

            owner = User.get(user_id)
            group = Group.get(group_id)
            owner.groups.append(group)
            owner.save()

            return group.to_dict(), 201

        except DatabaseConnectionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500








