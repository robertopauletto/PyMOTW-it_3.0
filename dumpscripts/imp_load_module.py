#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import imp

f, filename, description = imp.find_module('example')
example_package = imp.load_module('example', f, filename, description)
print 'Pacchetto:', example_package

f, filename, description = imp.find_module('submodule', 
                                           example_package.__path__)
try:
    submodule = imp.load_module('example.module', f, filename, description)
    print 'Sub-modulo:', submodule
finally:
    f.close()