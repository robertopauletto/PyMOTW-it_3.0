#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

try:
    import cPickle as pickle
except:
    import pickle
import sys

class SimpleObject(object):

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

if __name__ == '__main__':
    data = []
    data.append(SimpleObject('pickle'))
    data.append(SimpleObject('cPickle'))
    data.append(SimpleObject('ultimo'))

    try:
        filename = sys.argv[1]
    except IndexError:
        raise RuntimeError('Prego specificare un nome di file come parametro di %s' % sys.argv[0])

    out_s = open(filename, 'wb')
    try:
        # Scrive verso lo stream
        for o in data:
            print 'SCRITTURA: %s (%s)' % (o.name, o.name_backwards)
            pickle.dump(o, out_s)
    finally:
        out_s.close()
