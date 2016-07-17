from operator import *

class NoType(object):
   """Nessun supporto alle API di tipo"""
    
class MultiType(object):
    """Supporto alle API di tipo multiplo"""
    def __len__(self):
        return 0
    def __getitem__(self, name):
        return 'mappatura'
    def __int__(self):
        return 0

o = NoType()
t = MultiType()

for func in (isMappingType, isNumberType, isSequenceType):
    print '%s(o):' % func.__name__, func(o)
    print '%s(t):' % func.__name__, func(t)

