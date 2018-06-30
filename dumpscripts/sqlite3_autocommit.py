# sqlite3_autocommit.py

import logging
import sqlite3
import sys
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-10s) %(message)s',
)

db_filename = 'todo.db'
isolation_level = None  # modalità autocommit

def writer():
    with sqlite3.connect(
            db_filename, isolation_level=isolation_level) as conn:
        cursor = conn.cursor()
        cursor.execute('update compito set priorita = priorita + 1')
        logging.debug('in attesa per sincronizzare')
        ready.wait()  # sincronizza i thread
        logging.debug('IN PAUSA')
        time.sleep(1)
    return


def reader():
    with sqlite3.connect(
            db_filename, isolation_level=isolation_level) as conn:
        cursor = conn.cursor()
        logging.debug('in attesa per sincronizzare')
        ready.wait() # sincronizza
        logging.debug('in attesa')
        cursor.execute('select * from compito')
        logging.debug('SELECT ESEGUITO')
        results = cursor.fetchall()
        logging.debug('risultati recuperati')


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
