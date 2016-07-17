#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3
import collections

db_filename = 'todo.db'

class Mode(object):
    def __init__(self):
        self.counter = collections.Counter()  # Counter è disponibile dalla versione 2.7 
    def step(self, value):
        print 'step(%r)' % value
        self.counter[value] += 1
    def finalize(self):
        result, count = self.counter.most_common(1)[0]
        print 'finalize() -> %r (%d volte)' % (result, count)
        return result

with sqlite3.connect(db_filename) as conn:

    conn.create_aggregate('mode', 1, Mode)
    
    cursor = conn.cursor()
    cursor.execute("select mode(scadenza) from compito where progetto = 'pymotw-it'")
    row = cursor.fetchone()
    print "Il mode(scadenza) è:", row[0]