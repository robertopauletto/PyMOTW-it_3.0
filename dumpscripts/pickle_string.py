#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

try:
    import cPickle as pickle
except:
    import pickle
import pprint

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'DATI:',
pprint.pprint(data)

data_string = pickle.dumps(data)
print 'PICKLE:', data_string
