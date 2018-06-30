# sqlite3_create_aggregate.py

import sqlite3
import collections


db_filename = 'todo.db'

class Mode(object):
    def __init__(self):
        self.counter = collections.Counter()

    def step(self, value):
        print('step({!r})'.format(value))
        self.counter[value] += 1

    def finalize(self):
        result, count = self.counter.most_common(1)[0]
        print('finalize() -> {!r} ({} volte)'.format(result, count))
        return result


with sqlite3.connect(db_filename) as conn:
    conn.create_aggregate('mode', 1, Mode)

    cursor = conn.cursor()
    cursor.execute("""
       select mode(scadenza)
       from compito where progetto = 'pymotw-it 3'
    """)
    row = cursor.fetchone()
    print("La moda di scadenza è:", row[0])
