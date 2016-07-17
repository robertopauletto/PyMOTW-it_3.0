#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import shlex

text = """Questo testo ha "parti virgolettate" al suo interno."""
print 'ORIGINALE:', repr(text)
print

print 'TOKEN:'
print shlex.split(text)