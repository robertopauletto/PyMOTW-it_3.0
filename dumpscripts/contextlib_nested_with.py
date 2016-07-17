#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import contextlib

@contextlib.contextmanager
def make_context(name):
    print 'in entrata:', name
    yield name
    print 'in uscita :', name

with make_context('A') as A, make_context('B') as B, make_context('C') as C:
    print 'all\'interno dell\'istruzione with:', A, B, C