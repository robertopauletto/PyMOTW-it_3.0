#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

try:
    import cPickle as pickle
except:
    import pickle
import pprint
from StringIO import StringIO
import sys


try:
    filename = sys.argv[1]
except IndexError:
    raise RuntimeError('Prego specificare un nome di file come parametro di %s' % sys.argv[0])

in_s = open(filename, 'rb')
try:
    # Legge i dati
    while True:
        try:
            o = pickle.load(in_s)
        except EOFError:
            break
        else:
            print 'LETTURA: %s (%s)' % (o.name, o.name_backwards)
finally:
    in_s.close()
