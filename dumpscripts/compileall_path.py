#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import compileall
import sys

sys.path[:] = ['examples', 'nientequi']
print 'sys.path =', sys.path
compileall.compile_path()