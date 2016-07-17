#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class MyClass(object):
    
    @property
    def attribute(self):
        return "Questo è il valore dell'attributo"

o = MyClass()
print o.attribute
o.attribute = 'Nuovo valore'
