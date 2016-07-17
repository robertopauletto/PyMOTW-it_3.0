#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import anydbm

db = anydbm.open('/tmp/esempio.db', 'n')
db['chiave'] = 'value'
db['oggi'] = 'Sunday'
db['autore'] = 'Doug'
db.close()
