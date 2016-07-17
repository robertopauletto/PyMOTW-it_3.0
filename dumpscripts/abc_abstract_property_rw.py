#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import abc

class Base(object):
    __metaclass__ = abc.ABCMeta
    
    def value_getter(self):
        return 'Questo non si dovrebbe mai vedere'
    
    def value_setter(self, newvalue):
        return

    value = abc.abstractproperty(value_getter, value_setter)


class PartialImplementation(Base):
    
    @abc.abstractproperty
    def value(self):
        return 'Sola lettura'


class Implementation(Base):
    
    _value = 'Valore predefinito'
    
    def value_getter(self):
        return self._value

    def value_setter(self, newvalue):
        self._value = newvalue

    value = property(value_getter, value_setter)


try:
    b = Base()
    print 'Base.value:', b.value
except Exception, err:
    print 'ERRORE:', str(err)

try:
    p = PartialImplementation()
    print 'PartialImplementation.value:', p.value
except Exception, err:
    print 'ERRORE:', str(err)

i = Implementation()
print 'Implementation.value:', i.value

i.value = 'Nuovo valore'
print 'Valore modificato:', i.value#if __name__ == '__main__':
    
    
    
    #print 'Sottoclasse:', issubclass(IncompleteImplementation, PluginBase)
    #print 'Istanza    :', isinstance(IncompleteImplementation(), PluginBase)    