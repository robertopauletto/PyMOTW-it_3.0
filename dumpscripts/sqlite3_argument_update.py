# sqlite3_argument_update.py

import sqlite3
import sys

db_filename = 'todo.db'
id = int(sys.argv[1])
status = sys.argv[2]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "update compito set stato = :stato where id = :id"
    cursor.execute(query, {'stato':status, 'id':id})
