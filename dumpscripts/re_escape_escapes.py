#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns(r'\d+ \D+ \s+ \S+ \w+ \W+',
              [ r'\\d\+',
                r'\\D\+',
                r'\\s\+',
                r'\\S\+',
                r'\\w\+',
                r'\\W\+',
                ])