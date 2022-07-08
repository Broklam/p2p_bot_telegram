import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        conn.execute('''
          CREATE TABLE IF NOT EXISTS ORDERS
          ([order_id] INTEGER PRIMARY KEY, [seller] TEXT, [quantity] FLOAT, [price] FLOAT)
          ''')
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':\
    create_connection(r"Propositions.db")

