import sqlite3

db_filename = 'todo.db'


def authorizer_func(action, table, column, sql_location, ignore):
    print('\nauthorizer_func({}, {}, {}, {}, {})'.format(
        action, table, column, sql_location, ignore))

    response = sqlite3.SQLITE_OK  # be permissive by default

    if action == sqlite3.SQLITE_SELECT:
        print('requesting permission to run a select statement')
        response = sqlite3.SQLITE_OK

    elif action == sqlite3.SQLITE_READ:
        print('requesting access to column {}.{} from {}'.format(
            table, column, sql_location))
        if column == 'dettagli':
            print('  ignoring details column')
            response = sqlite3.SQLITE_IGNORE
        elif column == 'priorita':
            print('  preventing access to priority column')
            response = sqlite3.SQLITE_DENY

    return response


with sqlite3.connect(db_filename) as conn:
    conn.row_factory = sqlite3.Row
    conn.set_authorizer(authorizer_func)

    print('Using SQLITE_IGNORE to mask a column value:')
    cursor = conn.cursor()
    cursor.execute("""
    select id, dettagli from compito where progetto = 'pymotw-it 3'
    """)
    for row in cursor.fetchall():
        print(row['id'], row['dettagli'])

    print('\nUsing SQLITE_DENY to deny access to a column:')
    cursor.execute("""
    select id, priorita from compito where progetto = 'pymotw-it 3'
    """)
    for row in cursor.fetchall():
        print(row['id'], row['dettagli'])
