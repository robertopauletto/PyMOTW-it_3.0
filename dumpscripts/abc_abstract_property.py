#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import abc

class Base(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractproperty
    def value(self):
        return 'Non si dovrebbe mai arrivare qui'


class Implementation(Base):
    
    @property
    def value(self):
        return 'proprietà concreta'


try:
    b = Base()
    print 'Base.value:', b.value
except Exception, err:
    print 'ERROR:', str(err)

i = Implementation()
print 'Implementation.value:', i.value


#if __name__ == '__main__':
    #print 'Sottoclasse:', issubclass(IncompleteImplementation, PluginBase)
    #print 'Istanza    :', isinstance(IncompleteImplementation(), PluginBase)    