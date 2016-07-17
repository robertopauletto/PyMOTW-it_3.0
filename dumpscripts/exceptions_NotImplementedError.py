#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class BaseClass(object):
    """Definisce l'interfaccia"""
    def __init__(self):
        super(BaseClass, self).__init__()
    def do_something(self):
        """L'interfaccua, non implementata"""
        raise NotImplementedError(self.__class__.__name__ + '.fa_qualcosa')

class SubClass(BaseClass):
    """Implementa  interfaccia"""
    def do_something(self):
        """fa davvero qualcosa"""
        print self.__class__.__name__ + ' facendo qualcosa!'

SubClass().do_something()
BaseClass().do_something()
