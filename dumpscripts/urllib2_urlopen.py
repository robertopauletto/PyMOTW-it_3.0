#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import urllib2

response = urllib2.urlopen('http://localhost:8080/')
print 'RISPOSTA:', response
print 'URL     :', response.geturl()

headers = response.info()
print 'DATA    :', headers['date']
print 'HEADER  :'
print '---------'
print headers

data = response.read()
print 'LUNGH.  :', len(data)
print 'DATI    :'
print '---------'
print data