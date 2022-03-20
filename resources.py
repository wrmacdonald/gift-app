from flask import jsonify
from flask_restful import Resource
from services import UserService


class HelloWorld(Resource):
    @staticmethod
    def get():
        return {'hello': 'world'}


class UserResource(Resource):
    @staticmethod
    def get():
        users = UserService.get_users()
        data = jsonify([{user.id: user.name} for user in users])
        return data
