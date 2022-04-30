from flask_restful import Resource,request
from Models.history import History
import sqlite3
import time
from db import db

class Book(db.Model):
    __tablename__ = "books"

    bid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    author = db.Column(db.String)
    edition = db.Column(db.String)
    publisher = db.Column(db.String)

    def __init__(self,name,author,edition,publisher,state,bid=None):
        self.bid = bid
        self.name = name
        self.author = author
        self.edition = edition
        self.publisher = publisher


    @classmethod
    def find_available_books(cls):
        from Models.history import History
        #books = cls.query.join(History).filter_by(History.bid==cls.bid).filter_by(History.backtime!=None).all()
        temp = History.query.filter_by(return_time!=None).all()
        books = db.session.query(Book.bid ==temp.bid).all()
        return books

    @classmethod
    def find_by_bid(cls,bid):
        book = cls.query.filter_by(bid=bid).first()
        return book

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()








    #db.session.add(self)
    #db.session.commit(  )
