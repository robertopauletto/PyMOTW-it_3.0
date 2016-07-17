#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select * from compito where progetto = 'pymotw-it'
    """)

    print 'La tabella Compito ha queste colonne:'
    for colinfo in cursor.description:
        print colinfo
