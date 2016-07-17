#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import inspect
import example

arg_spec = inspect.getargspec(example.module_level_function)
print 'NOMEI   :', arg_spec[0]
print '*       :', arg_spec[1]
print '**      :', arg_spec[2]
print 'predef. :', arg_spec[3]

args_with_defaults = arg_spec[0][-len(arg_spec[3]):]
print 'parametri & predefiniti:', zip(args_with_defaults, arg_spec[3])