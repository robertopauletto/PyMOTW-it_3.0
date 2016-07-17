#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import locale
import time

sample_locales = [ ('USA',      'en_US'),
                   ('Francia',   'fr_FR'),
                   ('Spagna',    'es_ES'),
                   ('Portogallo', 'pt_PT'),
                   ('Polonia',   'pl_PL'),
                   ]

for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)
    print '%20s: %s' % (name, time.strftime(locale.nl_langinfo(locale.D_T_FMT)))    