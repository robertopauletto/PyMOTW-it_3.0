#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns('This is a prime #1 example!',
              [ r'\d+', # sequenza di cifre
                r'\D+', # sequenza di non-cifre
                r'\s+', # sequenza di whitespace
                r'\S+', # sequenza di non-whitespace
                r'\w+', # caratteri alfanumerici
                r'\W+', # non-alfanumerici
                ])