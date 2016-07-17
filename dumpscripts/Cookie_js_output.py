#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import Cookie

c = Cookie.SimpleCookie()
c['integer'] = 5
c['string_with_quotes'] = 'He said, "Hello, World!"'

for name in ['integer', 'string_with_quotes']:
    print c[name].key
    print '  %s' % c[name]
    print '  value=%s' % c[name].value, type(c[name].value)
    print '  coded_value=%s' % c[name].coded_value
    print