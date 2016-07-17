#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import locale

sample_data = [ ('USA',        'en_US', '1,234.56'),
                ('Francia',    'fr_FR', '1234,56'),
                ('Spagna',     'es_ES', '1234,56'),
                ('Portogallo', 'pt_PT', '1234.56'),
                ('Polonia',    'pl_PL', '1 234,56'),
                ]

for name, loc, a in sample_data:
    locale.setlocale(locale.LC_ALL, loc)
    f = locale.atof(a)
    print '%20s: %9s => %f' % (name, a, f)
    