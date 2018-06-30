# sqlite3_regex.py

import re
import sqlite3

db_filename = 'todo.db'


def regexp(pattern, input):
    return bool(re.match(pattern, input))


with sqlite3.connect(db_filename) as conn:
    conn.row_factory = sqlite3.Row
    conn.create_function('regexp', 2, regexp)
    cursor = conn.cursor()

    pattern = '.*[tT]radurre .*'

    cursor.execute(
        """
        select id, priorita, dettagli, stato, scadenza from compito
        where dettagli regexp :pattern
        order by scadenza, priorita
        """,
        {'pattern': pattern},
    )

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print('{:2d} [{:d}] {:<25} [{:<10}] ({})'.format(
              task_id, priority, details, status, deadline))
