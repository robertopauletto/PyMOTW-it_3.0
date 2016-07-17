#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def recurse(level):
    print 'ricorsione(%s)' % level
    if level:
        recurse(level-1)
    return

def not_called():
    print 'Questa funzione non è mai chiamata.'