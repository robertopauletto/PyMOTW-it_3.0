#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3
import sys

db_filename = 'todo.db'

sql = "select id, dettagli, scadenza from compito"

def show_deadline(conn):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    for col in ['id', 'dettagli', 'scadenza']:
        print '  colunna:', col
        print '    valore :', row[col]
        print '    tipo   :', type(row[col])
    return

print 'Senza identificazione del tipo:'

with sqlite3.connect(db_filename) as conn:
    show_deadline(conn)

print '\nCon identificazione del tipo:'

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    show_deadline(conn)