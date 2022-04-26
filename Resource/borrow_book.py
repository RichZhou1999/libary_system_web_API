from flask import jsonify
from flask_restful import Resource,request,reqparse
from Models.book import Book
from Models.user import User
import time
import sqlite3

class Borrow_book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("bid",type = str,
    required=True)

    def post(self,username):

        user = User.find_by_username(username)
        if not user:
            return jsonify({
                "message":" User not exist",
                "state": "404"
            })

        data = Borrow_book.parser.parse_args()
        book = Book.find_by_bid(data["bid"])
        if not book:
            return jsonify({
                "message":" This book has been borrowed",
                "state":400
            })
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        sql_q = "PRAGMA foreign_keys = ON"
        cursor.execute(sql_q)
        user = User.find_by_username(username)
        insert_query = "INSERT INTO history Values(?,?,?,NULL)"
        #data = ("3",'Harryp', 'JK', '10', '1')
        cursor.execute(insert_query,(data["bid"],1,str(time.time())))
        update_query = "Update books Set state = 1 Where bid = %s"%(data["bid"])
        cursor.execute(update_query)
        connection.commit()
        connection.close()
        return {"message":"succeed "},201
