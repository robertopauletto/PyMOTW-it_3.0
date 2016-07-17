#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3

db_filename = 'todo.db'

def authorizer_func(action_code, table, column, sql_location, ignore):
    print '\nauthorizer_func(%s, %s, %s, %s, %s)' % \
        (action_code, table, column, sql_location, ignore)

    response = sqlite3.SQLITE_OK # permissiva per default

    if action_code == sqlite3.SQLITE_SELECT:
        print 'richiesta permessi per eseguire una istruzione select'
        response = sqlite3.SQLITE_OK
    
    elif action_code == sqlite3.SQLITE_READ:
        print 'richiesta permessi per alla colonna %s.%s da %s' % \
            (table, column, sql_location)
        if column == 'dettagli':
            print '  si ignorano la colonna dettagli'
            response = sqlite3.SQLITE_IGNORE
        elif column == 'priorita':
            print "  si nega l'accesso alla colonna priorita"
            response = sqlite3.SQLITE_DENY

    return response

with sqlite3.connect(db_filename) as conn:
    conn.row_factory = sqlite3.Row
    conn.set_authorizer(authorizer_func)

    print 'Si usa SQLITE_IGNORE per nascondere un valore di colonna:'
    cursor = conn.cursor()
    cursor.execute("select id, dettagli from compito where progetto = 'pymotw-it'")
    for row in cursor.fetchall():
        print row['id'], row['dettagli']

    print "\nSi usa SQLITE_DENY per negare l'accesso alla colonna:"
    cursor.execute("select id, priorita from compito where progetto = 'pymotw-it'")
    for row in cursor.fetchall():
        print row['id'], row['dettagli']
        