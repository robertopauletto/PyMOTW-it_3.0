#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urlparse import urlparse
original = 'http://netloc/path;parameters?query=argument#fragment'
print 'ORIGINALE:', original
parsed = urlparse(original)
print 'ELABORATO:', parsed.geturl()