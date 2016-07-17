#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from ConfigParser import SafeConfigParser
import codecs

parser = SafeConfigParser()

# Apre il file con la codifica corretta
with codecs.open('unicode.ini', 'r', encoding='utf-8') as f:
    parser.readfp(f)

password = parser.get('bug_tracker', 'password')

print 'Password:', password.encode('utf-8')
print 'Type    :', type(password)
print 'repr()  :', repr(password)