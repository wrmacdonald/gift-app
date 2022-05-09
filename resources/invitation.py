import logging
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from mail.mail import send_email
from mail.messages import EmailInviteMessage
from database.models import Group

log = logging.getLogger(__name__)


class InviteMemberResource(Resource):

    @jwt_required()
    def post(self, group_id: int):
        """
        send a group invite email to a given email address
        params:
        - group id from url
        - email from body
        returns:
        - group does not exist: 404
        - email not given: 404
        - 200
        """
        try:
            post_args = reqparse.RequestParser()
            post_args.add_argument('email', required=True)
            args = post_args.parse_args()

            if not Group.exists(group_id):
                return {'message': f'Group with id {group_id} does not exist'}, 404

            if not args.email:
                return {'message': f'Must provide an email'}, 404

            group = Group.get(id=group_id)

            # TODO: handle link to signup/login resource passing group_id, & adding user to group once signed in

            msg = EmailInviteMessage(group_id, args.email, group.name)
            send_email(msg)

            return {'Sent invite email to: ': str(args.email)}, 200

        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}, 500

    def get(self):
        # create a link to share the group_id & let any user join
        # group id
        pass
