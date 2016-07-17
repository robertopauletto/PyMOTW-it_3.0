import json

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATI:', repr(data)

unsorted = json.dumps(data)
print 'JSON    :', json.dumps(data)
print 'ORDINATI:', json.dumps(data, sort_keys=True)

first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)

print 'CORRISPONDENZA NON ORDINATI:', unsorted == first
print 'CORRISPONDENZA ORDINATI    :', first == second
