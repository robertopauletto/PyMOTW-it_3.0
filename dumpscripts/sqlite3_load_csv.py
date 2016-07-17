#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
import sqlite3
import sys

db_filename = 'todo.db'
data_filename = sys.argv[1]

SQL = """insert into compito (dettagli, priorita, stato, scadenza, progetto)
         values (:dettagli, :priorita, 'attivo', :scadenza, :progetto)
      """

with open(data_filename, 'rt') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with sqlite3.connect(db_filename) as conn:
        cursor = conn.cursor()
        cursor.executemany(SQL, csv_reader)