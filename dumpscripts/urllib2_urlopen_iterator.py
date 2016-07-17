#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import urllib2

response = urllib2.urlopen('http://localhost:8080/')
for line in response:
    print line.rstrip()