import logging
from flask_restful import Resource, reqparse
from user_token import confirm_token, generate_confirmation_token
from database.models import User

log = logging.getLogger(__name__)


class Activate(Resource):
    @staticmethod
    def post(token: str):
        """activate user from token"""

        try:
            email = confirm_token(token)
        except:
            return 'The confirmation link is invalid or has expired.', 400

        user = User.get(email=email)
        if user.activated:
            return 'Account already confirmed. Please login.', 204
        else:
            user.activated = True
            user.save()
            return 'You have confirmed your account. Thanks!', 200


class SendActivation(Resource):
    def post(self):
        # get email from query params
        # generate token and send activation email

        post_args = reqparse.RequestParser()
        post_args.add_argument('email', required=True)
        args = post_args.parse_args()

        user = User.get(email=args.email)

        token = generate_confirmation_token(user.email)  # this will be in the invite resource

        # send email
        return {"token": token}, 200


