# shelve_readonly.py

import dbm
import shelve

with shelve.open('test_shelf.db', flag='r') as s:
    print('Esistente:', s['key1'])
    try:
        s['key1'] = 'nuovo valore'
    except dbm.error as err:
        print('ERRORE: {}'.format(err))
