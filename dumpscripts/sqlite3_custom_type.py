# sqlite3_custom_type.py

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


class MyObj:

    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return 'MyObj({!r})'.format(self.arg)


# Registra le funzioni per la manipolazione del tipo.
sqlite3.register_adapter(MyObj, adapter_func)
sqlite3.register_converter("MyObj", converter_func)

# Crea alcuni oggetti da salvare. Usa una lista di tuple in modo da poter
# passare questa sequanza direttamente a executemany().
to_save = [
    (MyObj('questo il valore da salvare'),),
    (MyObj(42),),
]

with sqlite3.connect(db_filename,
                     detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    # Crea una tabella con una colonna di tipo "MyObj"
    conn.execute("""
    create table if not exists obj (
        id    integer primary key autoincrement not null,
        data  MyObj
    )
    """)
    cursor = conn.cursor()

    # Inserisce gli oggetti nel database
    cursor.executemany("insert into obj (data) values (?)", to_save)

    # Interroga il database richiedendo gli oggetti appena salvati
    cursor.execute("select id, data from obj")
    for obj_id, obj in cursor.fetchall():
        print('Recuperato', obj_id, obj)
        print('    con tipo', type(obj))
        print()
