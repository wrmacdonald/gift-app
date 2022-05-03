import logging
from sqlalchemy.sql import func
from flask_restful import Resource
from confirmation_token import confirm_token
from database.models import User

log = logging.getLogger(__name__)


class EmailConfirmation(Resource):
    def post(self, token: str):
        """confirm user's email from token"""

        try:
            email = confirm_token(token)
        except:
            return 'The confirmation link is invalid or has expired.', 400

        try:
            user = User.get(email=email)
            if user.confirmed:
                return 'Account already confirmed. Please login.', 200

            user.confirmed = True
            user.confirmed_on = func.now()
            user.save()
            return 'Success', 200

        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}, 500

