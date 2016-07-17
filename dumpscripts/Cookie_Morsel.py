#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import Cookie
import datetime

def show_cookie(c):
    print c
    for key, morsel in c.iteritems():
        print
        print 'key =', morsel.key
        print '  value =', morsel.value
        print '  coded_value =', morsel.coded_value
        for name in morsel.keys():
            if morsel[name]:
                print '  %s = %s' % (name, morsel[name])

c = Cookie.SimpleCookie()

# Un cookie con un valore che deve essere codificato per potere entrare nell'intestazione
c['encoded_value_cookie'] = '"cookie_value"'
c['encoded_value_cookie']['comment'] = 'Si noti che il valore di questo cookie ha degli apici racchiusi in una sequenza di escape'

# Un cookie che si applica solo a parti del sito
c['restricted_cookie'] = 'cookie_value'
c['restricted_cookie']['path'] = '/sub/path'
c['restricted_cookie']['domain'] = 'PyMOTW'
c['restricted_cookie']['secure'] = True

# Un cookie che scade in 5 minuti
c['with_max_age'] = 'scade in 5 minutei'
c['with_max_age']['max-age'] = 300 # secondi

# A cookie that expires at a specific time
# Un cookie che scade ad un tempo specifico
c['expires_at_time'] = 'cookie_value'
expires = datetime.datetime(2009, 2, 14, 18, 30, 14) + datetime.timedelta(hours=1)
c['expires_at_time']['expires'] = expires.strftime('%a, %d %b %Y %H:%M:%S') # Wdy, DD-Mon-YY HH:MM:SS GMT

show_cookie(c)