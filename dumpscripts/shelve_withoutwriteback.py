# shelve_withoutwriteback.py

import shelve

with shelve.open('test_shelf.db') as s:
    print(s['key1'])
    s['key1']['nuovo_valore'] = 'questo non esisteva prima'

with shelve.open('test_shelf.db', writeback=True) as s:
    print(s['key1'])
