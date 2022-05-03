import logging
from flask_restful import Resource

log = logging.getLogger(__name__)


class InviteMemberResource(Resource):
    @staticmethod
    def post():
        # send invite email to email address
        # group id
        pass
