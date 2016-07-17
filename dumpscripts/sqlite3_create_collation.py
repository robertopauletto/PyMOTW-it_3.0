#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3
try:
    import cPickle as pickle
except:
    import pickle

db_filename = 'todo.db'

def adapter_func(obj):
    return pickle.dumps(obj)

def converter_func(data):
    return pickle.loads(data)

class MyObj(object):
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return 'MyObj(%r)' % self.arg
    def __cmp__(self, other):
        return cmp(self.arg, other.arg)

# Registra le funzioni per manipoloare il tipo
sqlite3.register_adapter(MyObj, adapter_func)
sqlite3.register_converter("MyObj", converter_func)

def collation_func(a, b):
    a_obj = converter_func(a)
    b_obj = converter_func(b)
    print 'collation_func(%s, %s)' % (a_obj, b_obj)
    return cmp(a_obj, b_obj)

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    # Definisce la collation
    conn.create_collation('unpickle', collation_func)

    # Pulisce la tabella ed inserisce i nuovi valori
    conn.execute('delete from obj')
    conn.executemany('insert into obj (data) values (?)',
                     [(MyObj(x),) for x in xrange(5, 0, -1)],
                     )

    # Interroga il database per ottenere gli oggetti appena salvati
    print '\nInterrogazione in corso:'
    cursor = conn.cursor()
    cursor.execute("select id, data from obj order by data collate unpickle")
    for obj_id, obj in cursor.fetchall():
        print obj_id, obj
        print