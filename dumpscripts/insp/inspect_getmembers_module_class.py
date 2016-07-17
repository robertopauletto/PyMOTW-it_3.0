#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect

import example


for name, data in inspect.getmembers(example, inspect.isclass):
    print '%s :' % name, repr(data)