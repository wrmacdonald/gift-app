import logging
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from database.models.models import User, Group
from database.models.base_model import DatabaseActionException
from serialize import serialize

log = logging.getLogger(__name__)


class GroupResource(Resource):

    @jwt_required()
    def post(self):
        """
        Create Group
        Create new Group associated to user who owns it
        returns
        - user does not exist: 400
        - success: 200 and serialized Group
        """
        try:
            post_args = reqparse.RequestParser()
            post_args.add_argument('owned_by_user', type=int, required=True)
            post_args.add_argument('name')
            args = post_args.parse_args()

            if not User.exists(args.owned_by_user):
                return {'message': f'User with id {args.owned_by_user} does not exist'}, 400

            group_id = Group.create(owned_by_user=args.owned_by_user,
                                    name=args.name)

            group = Group.get(id=group_id)

            return serialize(group), 201

        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}

    @jwt_required()
    def put(self):
        """
        Update Group information
        returns
        - user does not exist: 400
        - success: 200 and serialized Group
        """
        try:
            put_args = reqparse.RequestParser()
            put_args.add_argument('id', type=int, required=True)
            put_args.add_argument('owned_by_user', type=int)
            put_args.add_argument('name')
            args = put_args.parse_args()

            if not Group.exists(args.id):
                return {'message': f'Group with id {args.id} does not exist'}, 400

            if args.owned_by_user is not None and not User.exists(args.owned_by_user):
                return {'message': f'User with id {args.owned_by_user} does not exist'}, 400

            group = Group.update(**args)

            return serialize(group), 200

        except DatabaseActionException as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}

    @jwt_required()
    def get(self):
        """
        get list of all Groups a User is in
        returns
        - user does not exist: 400
        - success: 200 and list of Groups
        """
        try:
            user_id = int(request.args.get('user_id'))

            if not user_id:
                return {'message': 'user_id must be specific'}, 400

            if not User.exists(user_id):
                return {'message': f'User with id {user_id} does not exist'}, 400

            groups = Group.get_all(owned_by_user=user_id)

            return serialize(groups), 200

        except DatabaseActionException as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}


# /api/group/<group_id:int>/members
class GroupMembersResource(Resource):
    # add user to group
    @staticmethod
    def post():
        # group id
        # user id
        pass

    # remove user from group
    @ staticmethod
    def delete():
        # group id
        # user id
        pass


class InviteMemberResource(Resource):
    @staticmethod
    def post():
        # send invite email to email address
        # group id
        pass
