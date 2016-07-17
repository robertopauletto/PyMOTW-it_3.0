#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3
try:
    import cPickle as pickle
except:
    import pickle

db_filename = 'todo.db'

def adapter_func(obj):
    """Converte da in-memoria alla rappresentazione del valore da conservare
    """
    print 'adapter_func(%s)\n' % obj
    return pickle.dumps(obj)

def converter_func(data):
    """Converte da valore conservato a rappresentazione in-memoria.
    """
    print 'converter_func(%r)\n' % data
    return pickle.loads(data)


class MyObj(object):
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return 'MyObj(%r)' % self.arg

# Registra le funczioni per la manipolazione del tipo.
sqlite3.register_adapter(MyObj, adapter_func)
sqlite3.register_converter("MyObj", converter_func)

# Crea alcuni oggetti da salvare.  Usa una lista di tuple in modo da poter
# passare questa sequanza direttamente a executemany().
to_save = [ (MyObj("questo e' il valore da salvare"),),
            (MyObj(42),),
            ]

with sqlite3.connect(db_filename, detect_types=sqlite3.PARSE_COLNAMES) as conn:
    # Crea una tabella con una colonna di tipo MyObj"
    conn.execute("""
    create table if not exists obj2 (
        id    integer primary key autoincrement not null,
        data  text
    )
    """)
    cursor = conn.cursor()

    # Inserisce gli oggetti nel  database
    cursor.executemany("insert into obj2 (data) values (?)", to_save)

    # Interroga il database richiedendo gli oggetti appena salvati
    cursor.execute('select id, data as "pickle [MyObj]" from obj2')
    for obj_id, obj in cursor.fetchall():
        print 'Recuperato', obj_id, obj, type(obj)
        print