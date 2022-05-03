import logging
import datetime
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from database.models import User
from confirmation_token import generate_confirmation_token
from mail.mail import send_email
from mail.messages import EmailConfirmationMessage

log = logging.getLogger(__name__)


class Signup(Resource):

    def post(self):
        """
        creates a User record
        success: returns 200
        """
        try:
            post_args = reqparse.RequestParser()
            post_args.add_argument('email', required=True)
            post_args.add_argument('password', required=True)
            post_args.add_argument('first_name')
            post_args.add_argument('last_name')
            args = post_args.parse_args()

            user_id = User.create(email=args.email,
                                  password=User.hash_password(args.password),
                                  first_name=args.first_name,
                                  last_name=args.last_name)

            user = User.get(email=args.email)

            token = generate_confirmation_token(user.email)
            msg = EmailConfirmationMessage(token, user.email)
            send_email(msg)

            return {'id': str(user_id)}, 200

        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}


class Login(Resource):

    def post(self):
        """
        authenticates user
        params:
        - email
        - password
        returns 200 and jwt if params matches a User record in the database
        returns 401 if it does not match or if user is not confirmed yet
        returns 404 if no user was found for the corresponding email
        """

        try:
            post_args = reqparse.RequestParser()
            post_args.add_argument('email', required=True)
            post_args.add_argument('password', required=True)
            args = post_args.parse_args()

            user = User.get(email=args.email)
            if not user:
                return {'error': 'email does not match any users'}, 404

            authorized = user.check_password(args.password)

            if not authorized:
                return {'error': 'Email or password invalid'}, 401

            if not user.confirmed:
                return {'error': 'Please activate account in order to log in'}, 401

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200

        except Exception as ex:
            return {'message': 'An internal service error occurred', 'error': str(ex)}, 500



