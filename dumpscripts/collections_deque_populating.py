#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# collections_deque_populating.py

import collections

# Si aggiunge da destra
d1 = collections.deque()
d1.extend('abcdefg')
print('extend    :', d1)
d1.append('h')
print('append    :', d1)

# Si aggiunge da sinistra
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)
