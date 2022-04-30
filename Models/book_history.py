import sqlite3

class Book_history():
    def __init__(self,uid, username, password):
        self.uid = uid
        self.username = username
        self.password = password

    @classmethod
    def find_by_bid(cls,bid):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM book_history where bid=? and backtime!=NULL"
        result = cursor.execute(query,(bid,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
