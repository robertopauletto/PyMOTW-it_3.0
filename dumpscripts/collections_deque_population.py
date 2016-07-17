#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections

# Aggiungo da destra
d = collections.deque()
d.extend('abcdefg')
print 'extend    :', d
d.append('h')
print 'append    :', d

# Aggiungo da sinistra
d = collections.deque()
d.extendleft('abcdefg')
print 'extendleft:', d
d.appendleft('h')
print 'appendleft:', d
