import sqlite3
from db import db
import os

class User(db.Model):
    __tablename__ = "users"

    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)

    # def __init__(self, username, password,uid=None):
    #     self.uid = uid
    #     self.username = username
    #     self.password = password


    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
