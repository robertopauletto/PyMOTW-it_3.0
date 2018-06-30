# sqlite3_cursor_description.py

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select * from compito where progetto = 'pymotw-it 3'
    """)

    print('La tabella Compito ha queste colonne:')
    for colinfo in cursor.description:
        print(colinfo)
