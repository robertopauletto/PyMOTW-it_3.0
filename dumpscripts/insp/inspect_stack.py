#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect
"""Ispezione dello stack di chiamate"""
def recurse(limit):
    """Ispezione dello stack di chiamate"""
    local_variable = '.' * limit
    if limit <= 0:
        for frame, filename, line_num, func, source_code, source_index in inspect.stack():
            print '%s[%d]\n  -> %s' % (filename, line_num, source_code[source_index].strip())
            print inspect.getargvalues(frame)
            print
        return
    recurse(limit - 1)
    return

if __name__ == '__main__':
    """Ispezione dello stack di chiamate"""
    recurse(3)
