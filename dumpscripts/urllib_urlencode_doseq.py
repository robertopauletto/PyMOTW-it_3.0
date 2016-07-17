#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib

query_args = { 'foo':['foo1', 'foo2'] }
print 'Singola :', urllib.urlencode(query_args)
print 'Sequenza:', urllib.urlencode(query_args, doseq=True  )