#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import locale

sample_locales = [ ('USA',        'en_US'),
                   ('Francia',    'fr_FR'),
                   ('Spagna',     'es_ES'),
                   ('Portogallo', 'pt_PT'),
                   ('Polonia' ,   'pl_PL'),
                   ]

for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)
    print '%20s: %10s  %10s' % (name, locale.currency(1234.56), locale.currency(-1234.56))