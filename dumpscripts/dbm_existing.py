# dbm_existing.py

import dbm

with dbm.open('/tmp/example.db', 'r') as db:
    print('keys():', db.keys())
    for k in db.keys():
        print('iterando:', k, db[k])
    print('db["author"] =', db['author'])
