#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc
import weakref

class ExpensiveObject(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print '(Elimino %s)' % self

obj = ExpensiveObject('obj')
p = weakref.proxy(obj)

print 'PRIMA:', p.name
obj = None
print 'DOPO :', p.name
