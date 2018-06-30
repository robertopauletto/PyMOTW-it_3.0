# shelve_writeback.py

import shelve
import pprint

with shelve.open('test_shelf.db', writeback=True) as s:
    print('Dati iniziali:')
    pprint.pprint(s['key1'])

    s['key1']['nuovo_valore'] = 'questo non esisteva prima'

    print('\nModificato:')
    pprint.pprint(s['key1'])

with shelve.open('test_shelf.db', writeback=True) as s:
    print('\nPreservato:')
    pprint.pprint(s['key1'])
