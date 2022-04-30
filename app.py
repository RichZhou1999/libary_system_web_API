from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from ma import ma
#from Resource.borrowed_books import Borrowed_books
# from Resource.manager_check_books import Manager_check_books
#from Resource.manager_register import Manager_register
from Resource.return_book import Return_book
from Resource.user_check_books import User_check_books
from Resource.user_register import User_register

from Resource.borrow_book import Borrow_book
import sqlite3


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite3:~/Desktop/data.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

api = Api(app)

@app.before_first_request
# def init_state ():
#     from db import db
#     db.init_app(app)
def create_tables():
    from db import db
    db.init_app(app)
    ma.init_app(app)
    db.create_all()

api.add_resource(User_register,"/user_register")
#api.add_resource(Manager_register,"/manager_register")
api.add_resource(Borrow_book,"/borrow_books/<string:username>")
api.add_resource(Return_book,"/return_books/<string:username>")
#api.add_resourcr(Borrowed_books,"/borrowed_books/<string:name>")
api.add_resource(User_check_books,"/user_check_books/<string:username>")
# api.add_resourcr(User_check_books,"/manager_check_books/<string:name>")


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True)
