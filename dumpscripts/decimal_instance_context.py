#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import decimal

# Imposta un contesto con precisione limitata
c = decimal.getcontext().copy()
c.prec = 3

# Crea la costante
pi = c.create_decimal('3.1415')

# Il valore costante viene arrotondato
print 'PI:', pi

print 'RESULT:', decimal.Decimal('2.01') * pi