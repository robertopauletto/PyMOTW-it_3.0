#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import atexit

def my_cleanup(name):
    print 'my_cleanup(%s)' % name

atexit.register(my_cleanup, 'prima')
atexit.register(my_cleanup, 'seconda')
atexit.register(my_cleanup, 'terza')