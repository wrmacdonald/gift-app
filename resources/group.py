import logging
from flask_restful import Resource, reqparse
from database.models.models import User, Item, Group, List
from database.models.base_model import DatabaseActionException

log = logging.getLogger(__name__)


class GroupResource(Resource):

    # Create Group
        # Create group
        # Add users to group
        # Create users
        # Create empty list for each group member
    @staticmethod
    def post():
        pass

    # Update Group Members
        # Add or remove group member
        # Create empty list for each new group member
    @staticmethod
    def put():
        pass
