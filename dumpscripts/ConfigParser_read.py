#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('simple.ini')

print parser.get('bug_tracker', 'url')