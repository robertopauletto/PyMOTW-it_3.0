#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib

response = urllib.urlopen('http://localhost:8080/')
print 'RISPOSTA :', response
print 'URL      :', response.geturl()

headers = response.info()
print 'DATA     :', headers['date']
print 'HEADERS  :'
print '---------'
print headers

data = response.read()
print 'LUNGHEZZA:', len(data)
print 'DATI     :'
print '---------'
print data