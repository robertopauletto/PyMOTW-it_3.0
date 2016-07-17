#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gettext

catalogs = gettext.find('gettext_example', 'locale', all=True)
print 'Cataloghi:', catalogs
