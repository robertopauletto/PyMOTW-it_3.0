#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urlparse import urlparse
parsed = urlparse('http://netloc/path;parameters?query=argument#fragment')
print parsed
