#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3
import sys

db_filename = 'todo.db'
project_name = sys.argv[1]

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    query = """select id, priorita, dettagli, stato, scadenza from compito
            where progetto = :nome_progetto
            order by scadenza, priorita
            """

    cursor.execute(query, {'nome_progetto':project_name})

    for row in cursor.fetchall():
        task_id, priority, details, status, deadline = row
        print '%2d {%d} %-25s [%-8s] (%s)' % (task_id, priority, details, status, deadline)