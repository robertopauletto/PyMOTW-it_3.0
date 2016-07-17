#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urlparse import urlparse
parsed = urlparse('http://user:pass@NetLoc:80/path;parameters?query=argument#fragment')
print 'scheme  :', parsed.scheme
print 'netloc  :', parsed.netloc
print 'path    :', parsed.path
print 'params  :', parsed.params
print 'query   :', parsed.query
print 'fragment:', parsed.fragment
print 'username:', parsed.username
print 'password:', parsed.password
print 'hostname:', parsed.hostname, '(netloc in minuscolo)'
print 'port    :', parsed.port