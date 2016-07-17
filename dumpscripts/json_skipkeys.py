import json

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0, ('d',):'D tuple' } ]

print 'Primo tentativo'
try:
    print json.dumps(data)
except TypeError, err:
    print 'ERRORE:', err

print
print 'Secondo tentativo'
print json.dumps(data, skipkeys=True)
