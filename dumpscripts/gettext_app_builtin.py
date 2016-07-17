#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gettext
gettext.install('gettext_example', 'locale', unicode=True, names=['ngettext'])

print _('Questo messaggio è nello script.')
