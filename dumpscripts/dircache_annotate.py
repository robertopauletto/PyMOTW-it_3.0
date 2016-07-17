#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import dircache
from pprint import pprint
import os

path = '../..'

contents = dircache.listdir(path)

annotated = contents[:]
dircache.annotate(path, annotated)

fmt = '%20s\t%20s'

print fmt % ('ORIGINALI', 'ANNOTATI')
print fmt % (('-' * 20,)*2)

for o, a in zip(contents, annotated):
    print fmt % (o, a)
