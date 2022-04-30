from flask import jsonify, request
from flask_restful import Resource, reqparse
from Models.user import User
from schemas.user import UserSchema
import sqlite3
from marshmallow import ValidationError


user_schema = UserSchema()

class User_register(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument("username",type = str,
    # required=True)
    #
    # parser.add_argument("password",type = str,
    # required=True)

    def post(self):
        try:
            user = user_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages,400
        # data = User_register.parser.parse_args()
        if User.find_by_username(user.username):
            return {"message":"same name exist","state":400}
        user.add_to_db()

        return {"message":"succeed"}, 201
