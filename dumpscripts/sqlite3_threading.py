# sqlite3_threading.py

import sqlite3
import sys
import threading
import time

db_filename = 'todo.db'
isolation_level = None  # modalità autocommit


def reader(conn):
    print('Partenza del thread')
    try:
        cursor = conn.cursor()
        cursor.execute('select * from compiti')
        cursor.fetchall()
        print('risultati recuperati')
    except Exception as err:
        print('ERRORE:', err)


if __name__ == '__main__':
    with sqlite3.connect(db_filename,
                         isolation_level=isolation_level) as conn:
        t = threading.Thread(name='Reader 1', target=reader, args=(conn,))
        t.start()
        t.join()
