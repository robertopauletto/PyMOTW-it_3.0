#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import dircache

path = '/tmp'
first = dircache.listdir(path)
dircache.reset()
second = dircache.listdir(path)

print 'Identica  :', first is second
print 'Uguale    :', first == second
print 'Differenza:', list(set(second) - set(first))
