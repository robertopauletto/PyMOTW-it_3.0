#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select nome, descrizione, scadenza from progetto where nome = 'pymotw-it'
    """)
    name, description, deadline = cursor.fetchone()

    print 'Dettagli del progetto per %s (%s) scadenza %s' % (description, name, deadline)

    cursor.execute("""
    select id, priorita, dettagli, stato, scadenza from compito
    where progetto = 'pymotw-it' order by scadenza
    """)

    print '\nProssimi 5 compiti:'

    for row in cursor.fetchmany(5):
        task_id, priority, details, status, deadline = row
        print '%2d {%d} %-25s [%-8s] (%s)' % (task_id, priority, details, status, deadline)