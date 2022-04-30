from flask import jsonify
from flask_restful import Resource,Api
from Models.book import Book
from schemas.book import BookSchema
import sqlite3
from marshmallow import ValidationError


book_schema = BookSchema()


class User_check_books(Resource):
    def get(self,username):
        books = Book.find_available_books()
        for book in books:
            print(book)
        print(len(books),"++++")
        book_list = book_schema.dump(books)
        return book_list
        # book_list = []
        # for book in books:
        #     names = ["uid","name","author","edition"]
        #     nums = [i for i in range(4)]
        #     temp ={}
        #     for name,num in zip(names,nums):
        #         temp[name] = book[num]
        #
        #     book_list.append(temp)
        # return jsonify({"books":book_list})
