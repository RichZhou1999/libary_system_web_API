from flask_restful import Resource,Api
from flask import jsonify, request
from flask_restful import Resource, reqparse
from Models.book import Book
import sqlite3

class Manager_add(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name",type = str,
    required=True)

    parser.add_argument("author",type = str,
    required=True)

    parser.add_argument("edition",type = str,
    required=True)

    parser.add_argument("publisher",type = str,
    required=True)

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        book = Book(**data)
        book.add_to_db()
