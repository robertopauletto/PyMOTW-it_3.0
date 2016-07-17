#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns('Questa porzione di testo -- con punteggiatura.',
              [ '[a-z]+',      # sequenza di lettere minuscole
                '[A-Z]+',      # sequenza di lettere maiuscole
                '[a-zA-Z]+',   # sequenza di lettere maiuscole o minuscole
                '[A-Z][a-z]+', # una lettera maiuscola seguita da lettere  minuscole
                ])
