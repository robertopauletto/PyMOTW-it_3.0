#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sqlite3
import sys
import threading
import time

db_filename = 'todo.db'
isolation_level = None # modalità autocommit 

def reader(conn):
    my_name = threading.currentThread().name
    print 'Partenza del thread'
    try:
        cursor = conn.cursor()
        cursor.execute('select * from compiti')
        results = cursor.fetchall()
        print 'risultati recuperati'
    except Exception, err:
        print 'ERRORE:', err
    return

if __name__ == '__main__':

    with sqlite3.connect(db_filename, isolation_level=isolation_level) as conn:
        t = threading.Thread(name='Reader 1', target=reader, args=(conn,))
        t.start()
        t.join()