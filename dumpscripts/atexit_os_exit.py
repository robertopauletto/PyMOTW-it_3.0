#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import atexit
import os

def not_called():
    print 'Questa non dovrebbe essere chiamata'

print 'Sto registrando ...'
atexit.register(not_called)
print 'Registrata'

print 'Sto uscendo...'
os._exit(0)