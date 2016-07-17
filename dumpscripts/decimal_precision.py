#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import decimal

d = decimal.Decimal('0.123456')

for i in range(4):
    decimal.getcontext().prec = i
    print i, ':', d, d * 1
    