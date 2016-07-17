#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib

query_args = { 'q':'stringa di richiesta', 'foo':'bar' }
encoded_args = urllib.urlencode(query_args)
print 'Codificato:', encoded_args

url = 'http://localhost:8080/?' + encoded_args
print urllib.urlopen(url).read()