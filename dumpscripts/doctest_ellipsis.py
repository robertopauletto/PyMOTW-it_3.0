#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class MyClass(object):
    pass

def unpredictable(obj):
    """Ritorna una nuova lista che contiene obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_ellipsis.MyClass object at 0x...>]
    """
    return [obj]