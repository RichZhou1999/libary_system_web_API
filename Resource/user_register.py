from flask import jsonify, request
from flask_restful import Resource, reqparse
from Models.user import User
import sqlite3

class User_register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",type = str,
    required=True)

    parser.add_argument("password",type = str,
    required=True)

    def post(self):
        data = User_register.parser.parse_args()
        user = User.find_by_username(data['username'])
        if user:
            return {"message":"same name exist","state":400}
        #postdata = request.get_json()
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        insert_query = "INSERT INTO users Values(NULL ,?,?)"
        cursor.execute(insert_query,(data["username"],data["password"]))
        connection.commit()
        connection.close()
        return {"message":"succeed"}, 201
