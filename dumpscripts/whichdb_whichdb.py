#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import anydbm
import whichdb

db = anydbm.open('/tmp/esempio.db', 'n')
db['chiave'] = 'valore'
db.close()

print whichdb.whichdb('/tmp/esempio.db')
