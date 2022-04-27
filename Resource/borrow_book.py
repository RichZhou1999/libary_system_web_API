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
        book = Book.find_by_bid_state(data["bid"],0)
        if not book:
            return jsonify({
                "message":" This book is not available",
                "state":400
            })
        result = Book.borrow_book_logic(username,data["bid"])
        return jsonify(result)
