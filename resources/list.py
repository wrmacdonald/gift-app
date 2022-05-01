import logging
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from database.models.models import List, ListItem, User, Item, Group
from database.models.base_model import DatabaseActionException
from serialize import serialize

log = logging.getLogger(__name__)


class ListResource(Resource):

    # Create a List - linked to user who owns it and a group they're in
    @jwt_required()
    def post(self):
        """
        Create a new List associated to user who owns it & a group
        params:
        - owned_by_user: int id of user - required
        - group_id: int id of a group
        - name:
        returns:
        - user does not exist: 400
        - user not a member of the group: 400
        - success: 200 and serialized List
        """
        try:
            post_args = reqparse.RequestParser()
            post_args.add_argument('owned_by_user', type=int, required=True)
            post_args.add_argument('group_id', type=int)
            post_args.add_argument('name')
            args = post_args.parse_args()

            if not User.exists(args.owned_by_user):
                return {'message': f'User with id {args.owned_by_user} does not exist'}, 400

            if not Group.exists(args.group_id):
                return {'message': f'Group with id {args.group_id} does not exist'}, 400

            user = User.get(id=args.owned_by_user)
            group = Group.get(id=args.group_id)

            if user not in group.users:
                return {'message': f'User with id {args.user_id} is not in group'}, 400

            list_id = List.create(owned_by_user=args.owned_by_user,
                                  group_id=args.group_id,
                                  name=args.name)

            list = List.get(id=list_id)

            return serialize(list), 200

        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}

    @jwt_required()
    def put(self):
        """
        Update List information
        returns:
        - list does not exist: 400
        - success: 200 and serialized List
        """
        try:
            put_args = reqparse.RequestParser()
            put_args.add_argument('id', type=int, required=True)
            put_args.add_argument('owned_by_user', type=int)
            put_args.add_argument('name')
            args = put_args.parse_args()

            if not List.exists(args.id):
                return {'message': f'List with id {args.id} does not exist'}, 400

            if args.owned_by_user is not None and not User.exists(args.owned_by_user):
                return {'message': f'User with id {args.owned_by_user} does not exist'}, 400

            list = List.update(**args)

            return serialize(list), 200

        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}

    # Get all lists for a user
    @jwt_required()
    def get(self):
        """
        Get all Lists owned by a user
        params:
        - user_id from url path
        returns:
        - user does not exist: 400
        - success: 200 and serialized List(s)
        """
        try:
            user_id = int(request.args.get('user_id'))

            if not user_id:
                return {'message': 'user_id must be specific'}, 400

            if not User.exists(user_id):
                return {'message': f'User with id {user_id} does not exist'}, 400

            lists = List.get_all(owned_by_user=user_id)

            return serialize(lists), 200

        except DatabaseActionException as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}


class ListItemResource(Resource):

    @jwt_required()
    def post(self, list_id: int):
        """
        Add an Item to a List
        params:
        - list_id from url path
        - item_id from body
        returns:
        - item does not exist: 400
        - list does not exist: 400
        - success: 200 and serialized List
        """
        try:
            if not List.exists(list_id):
                return {'message': f'List with id {list_id} does not exist'}, 400

            post_args = reqparse.RequestParser()
            post_args.add_argument('item_id', type=int, required=True)
            args = post_args.parse_args()

            if not Item.exists(args.item_id):
                return {'message': f'Item with id {args.item_id} does not exist'}, 400

            item = Item.get(id=args.item_id)
            list = List.get(id=list_id)

            list.items.append(item)
            list.save()

            return serialize(list), 200

        except DatabaseActionException as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}

    @jwt_required()
    def delete(self, list_id: int):
        """
        Remove an Item from a List
        params:
        - list_id from url path
        - item_id from body
        returns:
        - item does not exist: 400
        - list does not exist: 400
        - success: 200 and serialized List
        """
        try:
            if not List.exists(list_id):
                return {'message': f'List with id {list_id} does not exist'}, 400

            post_args = reqparse.RequestParser()
            post_args.add_argument('item_id', type=int, required=True)
            args = post_args.parse_args()

            if not Item.exists(args.item_id):
                return {'message': f'Item with id {args.item_id} does not exist'}, 400

            item = Item.get(id=args.item_id)
            list = List.get(id=list_id)

            if item not in list.items:
                return {'message': f'Item with id {args.item_id} is not in list'}, 400

            list.items.remove(item)
            list.save()

            return serialize(list), 200

        except DatabaseActionException as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}

    # Get all or a single item from a list
    @jwt_required()
    def get(self, list_id: int):
        """
        Get all or a single item from a list depending on what you pass it
        get a single ListItem by item_id and list_id
        or get all ListItems in a List by just list_id
        params:
        - list_id from url path
        - item_id from body (optional)
        returns:
        - item does not exist: 400
        - list does not exist: 400
        - success: 200 and serialized List
        """
        try:
            if not List.exists(list_id):
                return {'message': f'List with id {list_id} does not exist'}, 400

            post_args = reqparse.RequestParser()
            post_args.add_argument('item_id', type=int)
            args = post_args.parse_args()

            if not args.item_id:
                # if item was not specified, get all items:
                list = List.get(id=list_id)
                return serialize(list.items), 200

            # otherwise, get specified item:
            if not Item.exists(args.item_id):
                return {'message': f'Item with id {args.item_id} does not exist'}, 400

            item = Item.get(id=args.item_id)

            return serialize(item), 200

        except DatabaseActionException as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}
