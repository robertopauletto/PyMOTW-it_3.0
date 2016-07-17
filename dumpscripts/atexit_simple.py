#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import atexit

def all_done():
    print 'all_done()'

print 'In registrazione'
atexit.register(all_done)
print 'Registrato'