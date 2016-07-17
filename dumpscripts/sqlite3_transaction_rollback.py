#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3

db_filenome = 'todo.db'

def show_projects(conn):
    cursor = conn.cursor()
    cursor.execute('select nome, descrizione from progetto')
    for nome, desc in cursor.fetchall():
        print '  ', nome
    return

with sqlite3.connect(db_filenome) as conn:

    print 'Prima delle modifiche:'
    show_projects(conn)

    try:

        # Istruzione di cancellazione
        cursor = conn.cursor()
        cursor.execute("delete from progetto where nome = 'virtualenvwrapper'")

        # Mostra i risultati
        print '\Dopo la cancellazione:'
        show_projects(conn)

        # Finge che l'esecuzione abbia causato un errore
        raise RuntimeError('errore simulato')

    except Exception, err:
        # Scarta le  modifiche
        print 'ERRORE:', err
        conn.rollback()
        
    else:
        # Salva le modifiche
        conn.commit()

    # Mostra i risultati
    print '\nDopo la chiamata di rollback:'
    show_progettos(conn)