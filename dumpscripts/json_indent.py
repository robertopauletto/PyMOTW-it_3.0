import json

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATI:', repr(data)

print 'NORMALE  :', json.dumps(data, sort_keys=True)
print 'INDENTATO:', json.dumps(data, sort_keys=True, indent=2)
