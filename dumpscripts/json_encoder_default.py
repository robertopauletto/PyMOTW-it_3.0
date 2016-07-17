import json
import json_myobj

class MyEncoder(json.JSONEncoder):
    
    def default(self, obj):
        print 'default(', repr(obj), ')'
        # Converte gli oggetti in un dizionario della loro rappresentazione
        d = { '__class__':obj.__class__.__name__, 
              '__module__':obj.__module__,
              }
        d.update(obj.__dict__)
        return d

obj = json_myobj.MyObj('dati interni')
print obj
print MyEncoder().encode(obj)
