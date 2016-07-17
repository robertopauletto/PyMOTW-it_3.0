#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def my_function(a, b):
    """
    >>> my_function(2, 3) #doctest: +REPORT_NDIFF
    6 
    >>> my_function('a', 3)
    'aaa'
    """
    return a * b