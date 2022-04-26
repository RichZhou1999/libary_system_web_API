import sqlite3
class User():
    def __init__(self,uid, username, password):
        self.uid = uid
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users where username=?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
