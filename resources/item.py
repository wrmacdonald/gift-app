import logging
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from database.models import User, Item
from database.base_model import DatabaseActionException
from serialize import serialize

log = logging.getLogger(__name__)


class ItemResource(Resource):

    @jwt_required()
    def post(self):
        """
        Add Item
        Create new ListItem associated to user & group and Item with details sent in body
        """
        try:
            post_args = reqparse.RequestParser()
            post_args.add_argument('owned_by_user_id', type=int, required=True)
            post_args.add_argument('group_id')
            post_args.add_argument('idea')
            post_args.add_argument('link')
            post_args.add_argument('exact', type=bool)
            post_args.add_argument('similar', type=bool)
            post_args.add_argument('size')
            post_args.add_argument('color')
            post_args.add_argument('desire_level', type=int)
            args = post_args.parse_args()

            if not User.exists(args.owned_by_user_id):
                return {'message': f'User with id {args.owned_by_user_id} does not exist'}, 404

            item_id = Item.create(owned_by_user_id=args.owned_by_user_id,
                                  idea=args.idea,
                                  link=args.link,
                                  exact=args.exact,
                                  similar=args.similar,
                                  size=args.size,
                                  color=args.color,
                                  desire_level=args.desire_level)

            item = Item.get(id=item_id)

            return serialize(item), 201

        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}, 500

    @jwt_required()
    def put(self):
        """
        Update item information
        returns
        - user does not exist or item doesn't exist: 404
        - success: 200 and serialized User
        """
        try:
            put_args = reqparse.RequestParser()
            put_args.add_argument('id', type=int, required=True)
            put_args.add_argument('owned_by_user_id', type=int)
            put_args.add_argument('group_id', type=int)
            put_args.add_argument('idea')
            put_args.add_argument('link', type=str)
            put_args.add_argument('exact', type=bool)
            put_args.add_argument('similar', type=bool)
            put_args.add_argument('size', type=str)
            put_args.add_argument('color', type=str)
            put_args.add_argument('desire_level', type=int)
            args = put_args.parse_args()

            if not Item.exists(args.id):
                return {'message': f'Item with id {args.id} does not exist'}, 404

            if args.owned_by_user_id is not None and not User.exists(args.owned_by_user_id):
                return {'message': f'User with id {args.owned_by_user_id} does not exist'}, 404

            item = Item.update(**args)
            return serialize(item), 200

        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}, 500

    @jwt_required()
    def delete(self):
        """
        deletes Item with id
        params: id:int from request body
        returns:
        - item does not exist: 404
        - success: 204
        """
        try:
            delete_args = reqparse.RequestParser()
            delete_args.add_argument('id', type=int, required=True)
            args = delete_args.parse_args()

            if not Item.exists(args.id):
                return {'message': f'Item with id {args.id} does not exist'}, 404

            item = Item.get(id=args.id)

            item.delete()

            return 'Success', 204

        except Exception as ex:
            return {'message': 'Internal Service Error', 'error': str(ex)}, 500

    @jwt_required()
    def get(self):
        """
        gets all Item by user_id
        returns
        - success: 200 and list of all Items that belong to the User
        - no users in database: 204
        - group doesn't exist: 400
        """
        try:
            user_id = int(request.args.get('user_id'))

            if not user_id:
                return {'message': 'user_id must be specified'}, 400

            if not User.exists(user_id):
                return {'message': f'User with id {user_id} does not exist'}, 404

            items = Item.get_all(owned_by_user_id=user_id)

            return serialize(items), 200

        except Exception as ex:
            return {'message': 'Internal Service Error', 'error': str(ex)}, 500
