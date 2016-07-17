#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print 'Creazione dello schema'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print 'Inserimento dei dati di partenza'
        
        conn.execute("""
        insert into progetto (nome, descrizione, scadenza)
        values ('pymotw-it', 'Il modulo Python della Settimana', '2010-11-01')
        """)
        
        conn.execute("""
        insert into compito (dettagli, stato, scadenza, progetto)
        values ('descrivere select', 'fatto', '2010-10-03', 'pymotw-it')
        """)
        
        conn.execute("""
        insert into compito (dettagli, stato, scadenza, progetto)
        values ('descrivere random', 'in attesa', '2010-10-10', 'pymotw-it')
        """)
        
        conn.execute("""
        insert into compito (dettagli, stato, scadenza, progetto)
        values ('descrivere sqlite3', 'attivo', '2010-10-17', 'pymotw-it')
        """)
    else:
        print 'Il database esiste, si suppone che esista anche lo schema.'
