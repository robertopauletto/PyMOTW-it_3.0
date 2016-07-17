#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import shelve

s = shelve.open('test_shelf.db', flag='r')
try:
    existing = s['chiave1']
finally:
    s.close()

print existing
