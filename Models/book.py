from flask_restful import Resource,request
import sqlite3

class Book(Resource):
    def __init__(self,bid,name,author,edition,publisher,state):
        self.bid = bid
        self.name = name
        self.author = author
        self.edition = edition
        self.publisher = publisher
        self.state = state

    @classmethod
    def find_by_bid(cls,bid):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM books where bid = ? and state = 0"
        result = cursor.execute(query,(bid,))
        row = result.fetchone()
        if row:
            book = cls(*row)
        else:
            book = None

        connection.close()
        return book
