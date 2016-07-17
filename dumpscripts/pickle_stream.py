#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

try:
    import cPickle as pickle
except:
    import pickle
import pprint
from StringIO import StringIO

class SimpleObject(object):

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('ultimo'))

# Simula un file con StringIO
out_s = StringIO()

# Scrive allo stream
for o in data:
    print 'SCRITTURA: %s (%s)' % (o.name, o.name_backwards)
    pickle.dump(o, out_s)
    out_s.flush()

# Imposta uno stream leggibile
in_s = StringIO(out_s.getvalue())

# Legge i dati
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print 'LETTURA: %s (%s)' % (o.name, o.name_backwards)
