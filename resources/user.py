import logging
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from database.models.models import User, Group
from database.models.base_model import DatabaseActionException
from serialize import serialize


log = logging.getLogger(__name__)


class UserResource(Resource):

    @jwt_required()
    def put(self):
        """
        Update user information
        params:
        - id: int id of user to update - required
        - email
        - first_name
        - last_name
        - password
        returns
        - user does not exist: 404
        - success: 200 and serialized User
        """
        try:
            user_put_args = reqparse.RequestParser()
            user_put_args.add_argument('id', type=int, required=True)
            user_put_args.add_argument('email')
            user_put_args.add_argument('first_name')
            user_put_args.add_argument('last_name')
            user_put_args.add_argument('password')
            args = user_put_args.parse_args()

            if not User.exists(args.id):
                return {'message': f'User with id {args.id} does not exist'}, 404

            args = user_put_args.parse_args()
            user = User.update(**args)

            return serialize(user), 200

        except DatabaseActionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500

    @jwt_required()
    def get(self):
        """
        gets all Users from database for group_id
        returns
        - success: 200 and list of all serialized Users
        - no users in database: 204
        - group doesn't exist: 400
        """
        try:
            group_id = int(request.args.get('group_id'))
            if not Group.exists(group_id):
                return {'message': f'Group with id {group_id} does not exist'}, 400

            users = User.get_all(group_id=group_id)
            if len(users) == 0:
                return 'no users found', 204

            return serialize(users), 200

        except DatabaseActionException as ex:
            return {'message': 'Internal Service Error', 'error': str(ex)}, 500

    @jwt_required()
    def delete(self):
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

            user = User.get(id=args.id)
            user.delete()

            return 'Success', 204

        except DatabaseActionException as ex:
            return {'message': 'Internal Service Error', 'error': ex}, 500

