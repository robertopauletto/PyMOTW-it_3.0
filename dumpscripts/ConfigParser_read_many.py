#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from ConfigParser import SafeConfigParser
import glob

parser = SafeConfigParser()

candidates = ['non_esiste.ini', 'anche-questo-non-esiste.ini',
              'simple.ini', 'multisezione.ini',
              ]

found = parser.read(candidates)

missing = set(candidates) - set(found)

print 'File di configurazione trovati :', sorted(found)
print 'File di configurazione mancanti:', sorted(missing)