#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import weakref

class ExpensiveObject(object):
    def __del__(self):
        print '(In eliminazione %s)' % self

obj = ExpensiveObject()
r = weakref.ref(obj)

print 'obj:', obj
print 'ref:', r
print 'r():', r()

print 'eliminazione di obj'
del obj
print 'r():', r()
