from flask import jsonify
from flask_restful import Resource,Api,reqparse
from Models.user import User
from Models.book import Book

import time
class Return_book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("bid",type = str,
    required=True)
    def post(self,username):
        data = Return_book.parser.parse_args()
        user = User.find_by_username(username)
        if not user:
            return jsonify({
                "message":" User not exist",
                "state": "404"
            })
        book = Book.find_by_bid_state(data["bid"],1)
        if not book:
            return jsonify({
                "message":" book not exist",
                "state": "404"
            })
        result = Book.return_book_logic(username,data["bid"])

        return jsonify(result)
