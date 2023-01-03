import sqlite3

sqlite_connection = sqlite3.connect('blog_1.db')
cursor = sqlite_connection.cursor()
print("Подключен к SQLite")

sqlite_insert_query = """INSERT INTO blog_posts
                          (id, title, subtitle, date, body, img_url, author)
                          VALUES
                          (1, 'The Life of Cactus', 'Who', 'October 20 2020', 'qew', 'fdsf', 'gfds' );"""
count = cursor.execute(sqlite_insert_query)
sqlite_connection.commit()
print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
cursor.close()


# sqlite_connection = sqlite3.connect('blog_1.db')
# cursor = sqlite_connection.cursor()
# print("База данных создана и успешно подключена к SQLite")
#
# sqlite_select_query = "select blog_posts();"
# cursor.execute(sqlite_select_query)
# record = cursor.fetchall()
# print("Версия базы данных SQLite: ", record)
# cursor.close()

# sqlite_connection = sqlite3.connect('blog_1.db')
# sqlite_create_table_query = '''CREATE TABLE blog_posts (
#                                 id INTEGER PRIMARY KEY,
#                                 title TEXT NOT NULL,
#                                 subtitle text NOT NULL UNIQUE,
#                                 date datetime,
#                                 body REAL NOT NULL,
#                                 img_url TEXT NOT NULL,
#                                 author TEXT NOT NULL);'''
#
# cursor = sqlite_connection.cursor()
# print("База данных подключена к SQLite")
# cursor.execute(sqlite_create_table_query)
# sqlite_connection.commit()
# print("Таблица SQLite создана")