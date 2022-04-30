import logging
from flask_restful import Resource
from user_token import confirm_token
from database.models import User

log = logging.getLogger(__name__)


class Activate(Resource):
    def post(self, token: str):
        """activate user from token"""

        try:
            email = confirm_token(token)
        except:
            return 'The confirmation link is invalid or has expired.', 400

        try:
            user = User.get(email=email)
            if user.activated:
                return 'Account already confirmed. Please login.', 204
            else:
                user.activated = True
                user.save()
                return 'You have confirmed your account. Thanks!', 200
        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}

