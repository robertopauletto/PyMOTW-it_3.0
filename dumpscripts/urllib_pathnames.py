#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

from urllib import pathname2url, url2pathname

print '== Predefinito =='
path = '/a/b/c'
print 'Originale:', path
print 'URL      :', pathname2url(path)
print 'Percorso :', url2pathname('/d/e/f')
print

from nturl2path import pathname2url, url2pathname

print '== Windows, senza lettere di drive =='
path = path.replace('/', '\\')
print 'Originale:', path
print 'URL      :', pathname2url(path)
print 'Percorso :', url2pathname('/d/e/f')
print

print '== Windows, con lettere di drive =='
path = 'C:\\' + path.replace('/', '\\')
print 'Originale:', path
print 'URL      :', pathname2url(path)
print 'Percorso :', url2pathname('/d/e/f')