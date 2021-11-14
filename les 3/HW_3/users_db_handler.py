import sqlite3


class Users_DB:
    def __init__(self):
        self.conn = sqlite3.connect("users.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (login, password,PRIMARY KEY (login))""")

    def check_user_exists(self, login):
        self.cursor.execute("""SELECT * FROM users where login=?""", (login,))
        data_from_db = self.cursor.fetchall()
        if data_from_db:
            return True
        else:
            return False

    def add_user(self, login, password):
        if self.check_user_exists(login):
            return False
        else:
            self.cursor.execute("""INSERT INTO users VALUES (?,?)""", (login, password))
            self.conn.commit()
            return True

    def check_user_password(self, login, password):
        if self.check_user_exists(login):
            return False
        else:
            self.cursor.execute("""SELECT * FROM users where login=?""", (login,))
            data_from_db = self.cursor.fetchall()
            if data_from_db[0][1] == password:
                return True
            else:
                return False
