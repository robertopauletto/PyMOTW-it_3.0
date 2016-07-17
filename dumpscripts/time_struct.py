#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time

print 'gmtime   :', time.gmtime()
print 'localtime:', time.localtime()
print 'mktime   :', time.mktime(time.localtime())

print
t = time.localtime()
print 'Giorno del mese:', t.tm_mday
print 'Giorno della settimana:', t.tm_wday
print "Giorno dell'anno:", t.tm_yday
