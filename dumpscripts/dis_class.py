#!/usr/bin/env python
# encoding: utf-8

import dis

class MyObject(object):
    """Esempio per dis."""
    
    CLASS_ATTRIBUTE = 'un qualche valore'
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'MyObject(%s)' % self.name

dis.dis(MyObject)