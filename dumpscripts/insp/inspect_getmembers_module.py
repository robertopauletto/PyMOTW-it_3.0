#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect

import example



for name, data in inspect.getmembers(example):
    if name == '__builtins__':
        continue
    print '%s :' % name, repr(data)