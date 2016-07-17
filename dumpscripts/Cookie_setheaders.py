#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import Cookie

c = Cookie.SimpleCookie()
c['ilmiocookie'] = 'valore_del_cookie'
print c
