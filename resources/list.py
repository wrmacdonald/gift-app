import logging
from flask_restful import Resource, reqparse
from database.models.models import User, Item, Group, List, ListItem
from database.models.base_model import DatabaseActionException

log = logging.getLogger(__name__)


class ListItemResource(Resource):

    # Delete List Item (DELETE api/users/<user_id>/lists/<list_id>/items/<item_id>)
    @staticmethod
    def delete():
        pass

    # Get ListItems (GET api/users/<user_id>/lists/<list_id>/items)
        # Get all items & details for user & list
    # Get ListItem by item_Id and list_id (GET api/users/<user_id>/lists/<list_id>/items?=item_id=)
    @staticmethod
    def get():
        pass

    # Add Item to List
        # Create a ListItem
    @staticmethod
    def post():
        pass
