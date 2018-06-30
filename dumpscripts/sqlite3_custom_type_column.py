# sqlite3_custom_type_column.py

import pickle
import sqlite3

db_filename = 'todo.db'


def adapter_func(obj):
    """Converte da in-memoria alla rappresentazione del valore da conservare
    """
    print('adapter_func({})\n'.format(obj))
    return pickle.dumps(obj)


def converter_func(data):
    """Converte da valore conservato a rappresentazione in-memoria.
    """
    print('converter_func({!r})\n'.format(data))
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
# passare questa sequenza direttamente a executemany().
to_save = [
    (MyObj("questo e' il valore da salvare"),),
    (MyObj(42),),
]

with sqlite3.connect(db_filename,
                     detect_types=sqlite3.PARSE_COLNAMES) as conn:
    # Crea una tabella con una colonna di tipo "testo"
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
    # usando uno specificatore di tipo per convertire il testo in oggetti
    cursor.execute('select id, data as "pickle [MyObj]" from obj2')
    for obj_id, obj in cursor.fetchall():
        print('Recuperato', obj_id, obj)
        print('     con tipo', type(obj))
        print()
