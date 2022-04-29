import logging
# import datetime
from flask_restful import Resource
from user_token import confirm_token
from database.models import User

log = logging.getLogger(__name__)


class UserActivationResource(Resource):
    @staticmethod
    def post(token):

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
