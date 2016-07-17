#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3

db_filename = 'todo.db'

def encrypt(s):
    print 'Codifica %r' % s
    return s.encode('rot-13')

def decrypt(s):
    print 'Decodifica %r' % s
    return s.encode('rot-13')


with sqlite3.connect(db_filename) as conn:

    conn.create_function('encrypt', 1, encrypt)
    conn.create_function('decrypt', 1, decrypt)
    cursor = conn.cursor()

    # Raw values
    print 'Valori originali:'
    query = "select id, dettagli from compito"
    cursor.execute(query)
    for row in cursor.fetchall():
        print row

    print '\nCodifica...'
    query = "update compito set dettagli = encrypt(dettagli)"
    cursor.execute(query)
    
    print '\nValori codificati grezzi:'
    query = "select id, dettagli from compito"
    cursor.execute(query)
    for row in cursor.fetchall():
        print row
    
    print "\nDecodifica nell'interrogazione ..."
    query = "select id, decrypt(dettagli) from compito"
    cursor.execute(query)
    for row in cursor.fetchall():
        print row