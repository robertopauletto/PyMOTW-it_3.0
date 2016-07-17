#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import shelve

s = shelve.open('test_shelf.db', writeback=True)
try:
    print s['chiave1']
    s['chiave1']['altro_valore'] = 'questo prima non era qui'
    print s['chiave1']
finally:
    s.close()

s = shelve.open('test_shelf.db', writeback=True)
try:
    print s['chiave1']
finally:
    s.close()
