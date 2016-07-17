#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urlparse import urldefrag
original = 'http://netloc/path;parameters?query=argument#fragment'
print original
url, fragment = urldefrag(original)
print url
print fragment