#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gettext

# Set up message catalog access
# Imposta l'accesso al catalogo di messaggi
t = gettext.translation('gettext_example', 'locale', fallback=True)
_ = t.ugettext

print _("Questo messaggio si trova nello script.")
