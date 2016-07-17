#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [ 'ab*',     # a seguito da zero o più b
                'ab+',     # a seguito da uno o più b
                'ab?',     # a seguito da zero od una b
                'ab{3}',   # a seguito da tre b
                'ab{2,3}', # a seguito da due a tre b
                ])