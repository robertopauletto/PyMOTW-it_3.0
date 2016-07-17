#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    # Modifica row factory per usare Row
    conn.row_factory = sqlite3.Row
    
    cursor = conn.cursor()

    cursor.execute("""
    select nome, descrizione, scadenza from progetto where nome = 'pymotw-it'
    """)
    name, description, deadline = cursor.fetchone()

    print 'Dettagli del progetto %s (%s) scadenza %s' % (description, name, deadline)

    cursor.execute("""
    select id, priorita, stato, scadenza, dettagli from compito
    where progetto = 'pymotw-it' order by scadenza
    """)

    print '\nProssimi 5 compiti:'

    for row in cursor.fetchmany(5):
        print '%2d {%d} %-25s [%-8s] (%s)' % (
            row['id'], row['priorita'], row['dettagli'], row['stato'], row['scadenza'],
            )