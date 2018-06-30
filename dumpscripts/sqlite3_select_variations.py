# sqlite3_select_variations.py

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select nome, descrizione, scadenza from progetto where nome = 'pymotw-it 3'
    """)
    name, description, deadline = cursor.fetchone()

    print('Dettagli del progetto per {} ({})\n scadenza {}'.format(
        description, name, deadline))

    cursor.execute("""
    select id, priorita, dettagli, stato, scadenza from compito
    where progetto = 'pymotw-it 3' order by scadenza
    """)

    print('\nProssimi 5 compiti:')

    for row in cursor.fetchmany(5):
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<10}] ({})'.format(
            task_id, priority, details, status, deadline))
