class manager():
    def __init__(mid, name, password, superword):
        self.mid = mid
        self.name = name
        self.password = password
        self.superpassword = superpassword

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
