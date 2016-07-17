import json

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
data_string = json.dumps(data)
print 'CODIFICATI  :', data_string

decoded = json.loads(data_string)
print 'DECODIFICATI:', decoded

print 'ORIGINALI   :', type(data[0]['b'])
print 'DECODIFICATI:', type(decoded[0]['b'])
