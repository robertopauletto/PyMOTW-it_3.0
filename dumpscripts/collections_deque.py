#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# collections_deque.py

import collections

d = collections.deque('abcdefg')
print ('Deque:', d)
print ('Lunghezza:', len(d))
print ('Estremo sx:', d[0])
print ('Estremo dx:', d[-1])

d.remove('c')
print ('rimuovo(c):', d)
