from ma import ma
from db import db
from Models.history import History


class HistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = History
        #load_only=("password")
        load_instance = True
        sqla_session = db.session
