from flask import jsonify
from flask_restful import Resource,request,reqparse
from Models.book import Book
from Models.user import User
from Models.history import History
import time
import sqlite3
from schemas.history import HistorySchema
from marshmallow import ValidationError
from db import db


history_schema = HistorySchema()

class Borrow_book(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument("bid",type = str,
    # required=True)

    def post(self,username):
        user = User.find_by_username(username)
        if not user:
            return jsonify({
                "message":" User not exist",
                "state": "404"
            })
        json_data = request.get_json()
        if History.check_state_by_bid(json_data['bid']):
            return jsonify({
                "message":" Book not available",
                "state": "404"
            })
        json_data['borrow_time'] = str(time.time())
        json_data['uid'] = user.uid
        json_data['return_time'] = None
        if History.check_state_by_bid(json_data['bid']):
            return jsonify({
                "message":" Book not available",
                "state": "404"
            })
        try:
            # history = history_schema.load(json_data,session=db.session)
            history = history_schema.load(json_data)
        except ValidationError as err:
                return err.messages,400
        # data = Borrow_book.parser.parse_args()
        if History.check_state_by_bid(json_data['bid']):
            return jsonify({
                "message":" Book not available",
                "state": "404"
            })
        history.add_to_db()
        return jsonify({
            "message":"successfully"
        })
