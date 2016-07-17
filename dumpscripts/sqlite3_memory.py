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

    print 'Cerco i compiti ...'
    cursor = conn.cursor()
    cursor.execute("""
    select id, priorita, stato, scadenza, dettagli from compito
    where progetto = 'pymotw-it' order by scadenza
    """)
    for row in cursor.fetchall():
        print '%2d {%d} %-25s [%-8s] (%s)' % (
            row['id'], row['priorita'], row['dettagli'], row['stato'], row['scadenza'],
            )

with sqlite3.connect(':memory:') as conn2:
    print '\nCerco compiti nella seconda connessione...'
    cursor = conn2.cursor()
    cursor.execute("""
    select id, priorita, stato, scadenza, dettagli from compito
    where progetto = 'pymotw-it' order by scadenza
    """)
    for row in cursor.fetchall():
        print '%2d {%d} %-25s [%-8s] (%s)' % (
            row['id'], row['priorita'], row['dettagli'], row['stato'], row['scadenza'],
            )