#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sqlite3


schema_filename = 'todo_schema.sql'

with sqlite3.connect(':memory:') as conn:
    conn.row_factory = sqlite3.Row

    print 'Creazione dello schema'
    with open(schema_filename, 'rt') as f:
        schema = f.read()
    conn.executescript(schema)

    print 'Inserimento dei dati di partenza'
        
    conn.execute("""
    insert into progetto (nome, descrizione, scadenza)
    values ('pymotw-it', 'Il modulo Python della Settimana', '2010-11-01')
    """)
        
    data = [
        ('descrivere select', 'fatto', '2010-10-03', 'pymotw-it'),
        ('descrivere random', 'in attesa', '2010-10-10', 'pymotw-it'),
        ('descrivere sqlite3', 'attivo', '2010-10-17', 'pymotw-it'),
        ]
    
    conn.executemany("""
            insert into compito (dettagli, stato, scadenza, progetto)
            values (?, ?, ?, ?)
            """, data)

    print 'Scaricamento:'
    for text in conn.iterdump():
        print text