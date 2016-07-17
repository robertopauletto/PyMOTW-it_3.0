#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import locale

sample_locales = [ ('USA',        'en_US'),
                   ('Francia',    'fr_FR'),
                   ('Spagna',     'es_ES'),
                   ('Portogallo', 'pt_PT'),
                   ('Polonia' ,   'pl_PL'),
                   ]

print '%20s %15s %20s' % ('Localizzazione', 'Interi', 'Virgola variabile')
for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)

    print '%20s' % name,
    print locale.format('%15d', 123456, grouping=True),
    print locale.format('%20.2f', 123456.78, grouping=True)