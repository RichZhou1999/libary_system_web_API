from flask import jsonify,request
from flask_restful import Resource,Api,reqparse
from Models.user import User
from Models.book import Book
from Models.history import History
from marshmallow import ValidationError


from schemas.history import HistorySchema



history_schema = HistorySchema()

import time
class Return_book(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument("bid",type = str,
    # required=True)

    @classmethod
    def post(cls,username):
        # data = cls.parser.parse_args()
        user = User.find_by_username(username)
        if not user:
            return jsonify({
                "message":" User not exist",
                "state": "404"
            })
        json_data = request.get_json()
        history = History.check_state_by_bid(json_data['bid'])
        if not history:
            return jsonify({
                "message":" Book not available",
                "state": "404"
            })
        history.return_time = str(time.time())
        history.add_to_db()
        return jsonify({
            "message":"successfully"
        })
