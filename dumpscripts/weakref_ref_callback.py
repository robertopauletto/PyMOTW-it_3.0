#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import weakref

class ExpensiveObject(object):
    def __del__(self):
        print '(Eliminazione di %s)' % self

def callback(reference):
    """Chiamato quando l'oggetto referenziato viene eliminato"""
    print 'callback(', reference, ')'

obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print 'obj:', obj
print 'ref:', r
print 'r():', r()

print 'Eliminazione di obj'
del obj
print 'r():', r()