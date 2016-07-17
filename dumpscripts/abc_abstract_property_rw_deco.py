#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import abc

class Base(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractproperty
    def value(self):
        return 'Questo non si dovrebbe mai vedere'
    
    @value.setter
    def value(self, newvalue):
        return


class Implementation(Base):
    
    _value = 'Valore predefinito'
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, newvalue):
        self._value = newvalue


i = Implementation()
print 'Implementation.value:', i.value

i.value = 'Nuovo valore'
print 'Valore modificato:', i.value    
    
    
    #print 'Sottoclasse:', issubclass(IncompleteImplementation, PluginBase)
    #print 'Istanza    :', isinstance(IncompleteImplementation(), PluginBase)    