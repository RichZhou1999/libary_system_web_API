from ma import ma
from db import db
from Models.book import Book


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        #load_only=("password")
        load_instance = True
        sqla_session = db.session
