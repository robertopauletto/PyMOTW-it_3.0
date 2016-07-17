#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urlparse import urlparse, urlunparse
original = 'http://netloc/path;?#'
print 'ORIGINALE:', original
parsed = urlparse(original)
print 'ELABORATO:', type(parsed), parsed
t = parsed[:]
print 'TUPLA    :', type(t), t
print 'NUOVO    :', urlunparse(t)