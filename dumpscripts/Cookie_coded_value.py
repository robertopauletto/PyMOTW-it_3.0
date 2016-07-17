#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import Cookie

c = Cookie.SimpleCookie()
c['intero'] = 5
c['stringa_con_apici'] = 'Disse, "Salve, Mondo!"'

for name in ['intero', 'stringa_con_apici']:
    print c[name].key
    print '  %s' % c[name]
    print '  valore=%s' % c[name].value, type(c[name].value)
    print '  valore codificato=%s' % c[name].coded_value
    print