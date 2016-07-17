#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import Cookie

HTTP_COOKIE = r'intero=5; stringa_con_apici="Disse, \"Salve, Mondo!\""'

print 'Dal costruttore:'
c = Cookie.SimpleCookie(HTTP_COOKIE)
print c

print
print 'Da load():'
c = Cookie.SimpleCookie()
c.load(HTTP_COOKIE)
print c