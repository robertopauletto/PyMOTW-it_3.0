#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import anydbm

db = anydbm.open('/tmp/esempio.db', 'r')
try:
    print 'chiavi():', db.keys()
    for k, v in db.iteritems():
        print 'iterazione:', k, v
    print 'db["autore"] =', db['autore']
finally:
    db.close()
