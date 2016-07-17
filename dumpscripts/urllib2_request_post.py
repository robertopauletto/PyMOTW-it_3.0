#!/usr/binf/env python
# -*- coding: UTF-8 -*-


import urllib
import urllib2

query_args = { 'q':'query string', 'foo':'bar' }

request = urllib2.Request('http://localhost:8080/')
print 'Metodo Request prima dei dati:', request.get_method()

request.add_data(urllib.urlencode(query_args))
print 'Metodo Request dopo i dati :', request.get_method()
request.add_header('User-agent', 'PyMOTW (http://www.doughellmann.com/PyMOTW/)')

print
print 'DATI IN USCITA     :'
print request.get_data()

print
print 'RISPOSTA DEL SERVER:'
print urllib2.urlopen(request).read()