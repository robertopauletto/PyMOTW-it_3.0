#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from re_test_patterns import test_patterns

test_patterns('Questa è una porzione di testo -- con punteggiatura.',
              [ '[^-. ]+',  # sequenze senza -, ., o spazi
                ])
