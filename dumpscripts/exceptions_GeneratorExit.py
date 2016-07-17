#!/usr/bin/env python
# -*- coding: UTF-8 -*-


def my_generator():
    try:
        for i in range(5):
            print 'Trattengo', i
            yield i
    except GeneratorExit:
        print 'Uscita prematura'

g = my_generator()
print g.next()
g.close()
