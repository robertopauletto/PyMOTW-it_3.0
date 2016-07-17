#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re_test_patterns_groups import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [r'a((a+)|(b+))',     # forma capturing 
               r'a((?:a+)|(?:b+))', # forma non-capturing
               ])