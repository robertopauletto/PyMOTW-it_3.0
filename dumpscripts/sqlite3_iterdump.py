# sqlite3_iterdump.py

import sqlite3

schema_filename = 'todo_schema.sql'

with sqlite3.connect(':memory:') as conn:
    conn.row_factory = sqlite3.Row

    print('Creazione dello schema')
    with open(schema_filename, 'rt') as f:
        schema = f.read()
    conn.executescript(schema)

    print('Inserimento dei dati di partenza')

    conn.execute("""
    insert into progetto (nome, descrizione, scadenza)
    values ('pymotw-it 3', 'Il modulo Python della Settimana', '2018-10-31')
    """)

    data = [
        ('descrivere select', 'fatto', '2018-05-13', 'pymotw-it 3'),
        ('descrivere random', 'in attesa', '2018-06-01', 'pymotw-it 3'),
        ('descrivere sqlite3', 'attivo', '2017-10-17', 'pymotw-it 3'),
        ]

    conn.executemany("""
            insert into compito (dettagli, stato, scadenza, progetto)
            values (?, ?, ?, ?)
            """, data)

    print('Scaricamento:')
    for text in conn.iterdump():
        print(text)
