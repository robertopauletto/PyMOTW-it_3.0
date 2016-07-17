#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gettext import translation
import sys

t = translation('gettext_plural', 'locale', fallback=True)
num = int(sys.argv[1])
msg = t.ungettext('%(num)d significa singolare.', '%(num)d significa plurale.', num)

# Ci si deve comunque occupare di aggiungere i  valori  al messaggio
print msg % {'num':num}
