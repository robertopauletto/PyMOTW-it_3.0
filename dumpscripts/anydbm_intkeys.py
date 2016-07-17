#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import anydbm

db = anydbm.open('/tmp/esempio.db', 'w')
try:
    db[1] = 'uno'
finally:
    db.close()
