#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import decimal

for value in [ 'Infinity', 'NaN', '0' ]:
    print decimal.Decimal(value), decimal.Decimal('-' + value)
print

# Matematica con infinity
print 'Infinito + 1:', (decimal.Decimal('Infinity') + 1)
print '-Infinito + 1:', (decimal.Decimal('-Infinity') + 1)

# Stampa le comparazioni di NaN
print decimal.Decimal('NaN') == decimal.Decimal('Infinity')
print decimal.Decimal('NaN') != decimal.Decimal(1)