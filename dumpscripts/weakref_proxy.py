#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import weakref

class ExpensiveObject(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print '(Eliminazione di %s)' % self

obj = ExpensiveObject('Il mio oggetto')
r = weakref.ref(obj)
p = weakref.proxy(obj)

print 'via obj:', obj.name
print 'via ref:', r().name
print 'via proxy:', p.name
del obj
print 'via proxy:', p.name