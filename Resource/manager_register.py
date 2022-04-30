from flask_restful import Resource,Api
from flask import jsonify, request
from flask_restful import Resource, reqparse
from Models.manager import Manager
import sqlite3

superpassword = 'super_key'
class Manager_register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name",type = str,
    required=True)

    parser.add_argument("password",type = str,
    required=True)

    parser.add_argument("superpassword",type = str,
    required=True)

    def post(self):
        data = User_register.parser.parse_args()
        data["superpassword"] != superpassword:
        return jsonify({
                        "message":"wrong superpassword"
        })
        manager = Manager.find_by_username(data['username'])
        if manager:
            return {"message":"same name exist","state":400}
        manager = manager(name = data["name"],password = data["password"],
        superpassword = superpassword)
        manager.add_to_db()
