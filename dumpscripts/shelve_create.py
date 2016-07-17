#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import shelve

s = shelve.open('test_shelf.db')
try:
    s['chiave1'] = { 'int': 10, 'float':9.5, 'string':'Dati di esempio' }
finally:
    s.close()
