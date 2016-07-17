#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import imp
from imp_get_suffixes import module_types

print 'Pacchetto:'
f, filename, description = imp.find_module('example')
print module_types[description[2]], filename
print

print 'Sub-modulo:'
f, filename, description = imp.find_module('submodule', [filename])
print module_types[description[2]], filename
if f: f.close()
