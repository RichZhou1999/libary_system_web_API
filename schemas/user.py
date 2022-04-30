from ma import ma
from Models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_only=("password")
        dump_only=("uid")
        load_instance = True
