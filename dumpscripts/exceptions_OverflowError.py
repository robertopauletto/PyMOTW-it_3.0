#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys

print 'Intero normale: (maxint=%s)' % sys.maxint
try:
    i = sys.maxint * 3
    print 'Nessun overflow per ', type(i), 'i =', i
except OverflowError, err:
    print 'Overflow a ', i, err

print
print 'Intero lungo:'
for i in range(0, 100, 10):
    print '%2d' % i, 2L ** i

print
print 'Valori a virgola mobile:'
try:
    f = 2.0**i
    for i in range(100):
        print i, f
        f = f ** 2
except OverflowError, err:
    print 'Overflow dopo ', f, err
