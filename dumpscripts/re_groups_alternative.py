#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re_test_patterns_groups import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [r'a((a+)|(b+))', # 'a' seguito da una sequanza di 'a' o da una sequenza di 'b'
               r'a((a|b)+)',    # 'a' seguito da una sequenza di 'a' o 'b'
               ])