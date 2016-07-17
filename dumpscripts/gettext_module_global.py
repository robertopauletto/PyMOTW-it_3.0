#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gettext
t = gettext.translation('gettext_example', 'locale', fallback=True)
_ = t.ugettext
ngettext = t.ungettext

print _('Questo messaggio è nello script.')
