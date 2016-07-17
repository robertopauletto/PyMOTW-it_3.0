import json

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATI:', repr(data)
print 'repr(data)                  :', len(repr(data))
print 'dumps(data)                 :', len(json.dumps(data))
print 'dumps(data, indentazione=2) :', len(json.dumps(data, indent=2))
print 'dumps(data, separatori)     :', len(json.dumps(data, separators=(',',':')))
