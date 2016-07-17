#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import imp

try:
    imp.find_module('modulo_che_non_esiste')
except ImportError, err:
    print 'ImportError:', err