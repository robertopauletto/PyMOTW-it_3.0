#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib

response = urllib.urlopen('http://localhost:8080/')
for line in response:
    print line.rstrip()