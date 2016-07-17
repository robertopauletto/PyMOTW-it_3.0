#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [ 'a(ab)',    # 'a' seguito da 'ab' letterale
                'a(a*b*)',  # 'a' seguito da 0-n 'a' e 0-n 'b'
                'a(ab)*',   # 'a' seguito da 0-n 'ab'
                'a(ab)+',   # 'a' seguito da 1-n 'ab'
                ])