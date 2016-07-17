#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import atexit
import sys

def all_done():
    print 'all_done()'

print 'Sto registrando ...'
atexit.register(all_done)
print 'Registrata'

print 'Sto uscendo...'
sys.exit()