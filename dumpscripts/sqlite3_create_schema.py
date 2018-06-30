# sqlite3_create_schema.py

import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creazione dello schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserimento dei dati di partenza')

        conn.execute("""
        insert into progetto (nome, descrizione, scadenza)
        values ('pymotw-it 3', 'Il modulo Python della Settimana', '2018-08-16')
        """)

        conn.execute("""
        insert into compito (dettagli, stato, scadenza, progetto)
        values ('tradurre select', 'fatto', '2018-05-21', 'pymotw-it 3')
        """)

        conn.execute("""
        insert into compito (dettagli, stato, scadenza, progetto)
        values ('tradurre random', 'in attesa', '2018-06-02', 'pymotw-it 3')
        """)

        conn.execute("""
        insert into compito (dettagli, stato, scadenza, progetto)
        values ('tradurre sqlite3', 'attivo', '2018-10-31', 'pymotw-it 3')
        """)
    else:
        print('Il database esiste, si suppone che esista anche lo schema.')
