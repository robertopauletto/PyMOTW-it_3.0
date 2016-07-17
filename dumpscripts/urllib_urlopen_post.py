#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import urllib

query_args = { 'q':'stringa di richiesta', 'foo':'bar' }
encoded_args = urllib.urlencode(query_args)
url = 'http://localhost:8080/'
print urllib.urlopen(url, encoded_args).read()