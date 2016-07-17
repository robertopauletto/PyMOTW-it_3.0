#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

try:
    import cPickle as pickle
except:
    import pickle
import pprint

data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'PRIMA:',
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print 'DOPO:',
pprint.pprint(data2)

print 'STESSI?:', (data1 is data2)
print 'UGUALI?:', (data1 == data2)
