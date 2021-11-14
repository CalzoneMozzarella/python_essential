import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()


def add_user(login, password):
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (login, password)""")
    cursor.execute("""INSERT INTO users VALUES (?,?)""", (login, password))
    conn.commit()


def get_user(login):
    cursor.execute("""SELECT * FROM users WHERE login=?""", (login,))
    return cursor.fetchall()


add_user('admin', 'admin')
