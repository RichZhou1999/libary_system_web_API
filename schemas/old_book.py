from flask_restful import Resource,request
import sqlite3
import time
class Book(Resource):
        __tablename__ = "books"
        bid = db.Column(db.Interger, primary_key=True)
        name = db.Column(db.String)
        author = db.Column(db.String)
        edition = db.Column(db.String)
        publisher = db.Column(db.String)
        state = db.Column(db.Interger)

        def __init__(self,bid,name,author,edition,publisher,state):
            self.bid = bid
            self.name = name
            self.author = author
            self.edition = edition
            self.publisher = publisher
            self.state = state

        @classmethod
        def basic_find(cls,query,num):
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()
            result = cursor.execute(query)
            if num == "one":
                row = result.fetchone()
                if row:
                    book = cls(*row)
                else:
                    book = None
            else:
                books = result.fetchall()
                return books
            connection.close()
            return book

        @classmethod
        def basic_update(cls,query):
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()
            sql_q = "PRAGMA foreign_keys = ON"
            cursor.execute(sql_q)
            cursor.execute(query)
            connection.commit()
            connection.close()

        @classmethod
        def find_available_books(cls,num="all"):
            query = "SELECT * FROM books where state =0 "
            book = cls.basic_find(query, num="all")
            return book

        @classmethod
        def find_by_bid_state(cls,bid,state):
            query = "SELECT * FROM books where bid =%s and state = %s"%(bid,state)
            book = cls.basic_find(query, num="one")
            return book

        @classmethod
        def return_book_logic(cls,username,bid):
            update_query = "Update books Set state = 0 Where bid = %s"%(bid)
            cls.basic_update(update_query)
            update_query = "Update history Set backtime = %s Where bid = %s"%(time.time(),bid)
            cls.basic_update(update_query)
            return {"message":"Return books successfully"}

        @classmethod
        def borrow_book_logic(cls,username,bid):
            insert_query = "INSERT INTO history Values(%s,%s,%s,NULL)"%(bid,1,str(time.time()))
            cls.basic_update(update_query)
            update_query = "Update books Set state = 1 Where bid = %s"%(bid)
            cls.basic_update(update_query)
            return {"message":"Borrow books successfully"}

class Bookhistory(Resource):
    pass


    #db.session.add(self)
    #db.session.commit(  )
