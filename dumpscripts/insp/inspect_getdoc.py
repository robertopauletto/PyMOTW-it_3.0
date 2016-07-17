#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect
import example

print 'B.__doc__:'
print example.B.__doc__
print
print 'getdoc(B):'
print inspect.getdoc(example.B)