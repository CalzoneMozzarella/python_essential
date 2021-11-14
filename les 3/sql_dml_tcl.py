import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS albums
                  (title text, artist text, release_date text,
                   publisher text, media_type text)
               """)

# Вставляем данные в таблицу
cursor.execute("""INSERT INTO albums
                  VALUES ('Medicine at midnight', 'Foo Fighters', '2020', 'VA', 'MP3')
                  """)

# Сохраняем изменения
conn.commit()

# Вставляем множество данных в таблицу используя безопасный метод "?"
albums = [('Show us your hits', 'Bloodhound Gang', '2010', 'VA', 'MP3'),
          ('Conspiracy Pt.2', 'Gessaffelstein', '2019', 'VA', 'Vinyl'),
          ('Power Up', 'AC/DC', '2020', 'VA', 'CD'),
          ('Emergency on planet Earth', 'Jamiroquai', '1993', 'VA', 'CD')]

cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)

conn.commit()
conn.close()