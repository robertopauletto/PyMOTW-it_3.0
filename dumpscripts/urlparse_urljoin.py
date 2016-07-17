#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urlparse import urljoin
print urljoin('http://www.example.com/path/file.html', 'anotherfile.html')
print urljoin('http://www.example.com/path/file.html', '../anotherfile.html')