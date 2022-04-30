from flask import jsonify, request
from flask_restful import Resource, reqparse
from Models.user import User
#from Models.book import Book
import sqlite3
from db import db

class History(db.Model):
    __tablename__ = "history"

    # bid = db.Column(db.Integer, db.ForeignKey("books.bid"),primary_key=True)
    # uid = db.Column(db.Integer, db.ForeignKey("users.uid"),primary_key=True)
    bid = db.Column(db.Integer,db.ForeignKey("books.bid"),primary_key=True)
    uid = db.Column(db.Integer,primary_key=True)
    borrow_time = db.Column(db.String,primary_key=True)
    return_time = db.Column(db.String)
    book_history = db.relationship("Book", foreign_keys=[bid])
    # bid = db.Column(db.Integer,primary_key=True)
    # uid = db.Column(db.Integer,primary_key=True)
    # def __init__(self,bid, uid, borrow_time, return_time):
    #     self.bid = bid
    #     self.uid = uid
    #     self.borrow_time = borrow_time
    #     self.return_time = return_time

    @classmethod
    def check_state_by_bid(cls,bid):
        return cls.query.filter_by(bid=bid).filter_by(return_time=None).first()


    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
