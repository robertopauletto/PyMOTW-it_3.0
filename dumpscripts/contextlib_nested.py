#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import contextlib

@contextlib.contextmanager
def make_context(name):
    print 'in entrata:', name
    yield name
    print 'in uscita :', name

with contextlib.nested(make_context('A'), make_context('B'), make_context('C')) as (A, B, C):
    print 'all\'interno dell\'istruzione with:', A, B, C