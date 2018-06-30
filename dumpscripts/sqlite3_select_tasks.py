# sqlite3_select_tasks.py

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select id, priorita, dettagli, stato, scadenza
    from compito
    where progetto = 'pymotw-it 3'
    """)

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<10}] ({})'.format(
            task_id, priority, details, status, deadline))
