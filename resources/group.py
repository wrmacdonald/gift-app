import logging
from flask_restful import Resource, reqparse
from database.models.models import User, Item, Group, List
from database.models.base_model import DatabaseActionException

log = logging.getLogger(__name__)


class GroupResource(Resource):

    # Create Group
    @staticmethod
    def post():
        pass

    # Update Group Details
    @staticmethod
    def put():
        pass

    @staticmethod
    def get():
        # get list of groups that user is in
        # user_id
        pass


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
