#!/usr/bin/env python
# -*- coding: Latin-1 -*-

import json
import json_myobj


obj = json_myobj.MyObj('Il valore di istanza va qui')

print 'Primo tentativo'
try:
    print json.dumps(obj)
except TypeError, err:
    print 'ERRORE:', err

def convert_to_builtin_type(obj):
    print 'default(', repr(obj), ')'
    # Converte gli oggetti in una dizionario della loro rappresentazione
    d = { '__class__':obj.__class__.__name__, 
          '__module__':obj.__module__,
          }
    d.update(obj.__dict__)
    return d

print
print 'Con default'
print json.dumps(obj, default=convert_to_builtin_type)
