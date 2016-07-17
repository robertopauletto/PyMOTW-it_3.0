#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import sqlite3
import sys
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-10s) %(message)s',
                    )

db_filename = 'todo.db'
isolation_level = sys.argv[1]

def writer():
    my_name = threading.currentThread().name
    logging.debug('in connessione')
    with sqlite3.connect(db_filename, isolation_level=isolation_level) as conn:
        cursor = conn.cursor()
        logging.debug('connesso')
        cursor.execute('update compito set priorita = priorita + 1')
        logging.debug('modifiche effettuate')
        logging.debug('in attesa di sincronizzare')
        ready.wait() # sincronizza
        logging.debug('IN PAUSA')
        time.sleep(1)
        conn.commit()
        logging.debug('MODIFICHE EFFETTUATE')
    return

def reader():
    my_name = threading.currentThread().name
    with sqlite3.connect(db_filename, isolation_level=isolation_level) as conn:
        cursor = conn.cursor()
        logging.debug('in attesa di sincronizzare')
        ready.wait() # sincronizza
        logging.debug('attendo oltre')
        cursor.execute('select * from compito')
        logging.debug('SELECT ESEGUITO')
        results = cursor.fetchall()
        logging.debug('risultati recuperati')
    return

if __name__ == '__main__':
    ready = threading.Event()

    threads = [
        threading.Thread(name='Lettore 1', target=reader),
        threading.Thread(name='Lettore 2', target=reader),
        threading.Thread(name='Scrittore 1', target=writer),
        threading.Thread(name='Scrittore 2', target=writer),
        ]
    
    [ t.start() for t in threads ]
    
    time.sleep(1)
    logging.debug('impostazioni pronte')
    ready.set()

    [ t.join() for t in threads ]