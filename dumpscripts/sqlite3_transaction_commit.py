#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3

db_filename = 'todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select nome, descrizione from progetto')
    for name, desc in cursor.fetchall():
        print '  ', name
    return

with sqlite3.connect(db_filename) as conn1:

    print 'Prima delle modifiche:'
    show_projects(conn1)

    # Istruzione Insert in un cursore
    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into progetto (nome, descrizione, scadenza)
    values ('virtualenvwrapper', 'Estensioni Virtualenv', '2011-01-01')
    """)

    print '\nDopo le modifiche in conn1:'
    show_projects(conn1)

    # Istruzione Select da un'altra connessione, senza prima chiamare commit
    print '\nPrima di commit:'
    with sqlite3.connect(db_filename) as conn2:
        show_projects(conn2)

    # Chiamata di Commit quindi select da un'altra connessione
    conn1.commit()
    print '\nDopo commit:'
    with sqlite3.connect(db_filename) as conn3:
        show_projects(conn3)
    