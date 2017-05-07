# json_sort_keys.py
import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATI:', repr(data))

unsorted = json.dumps(data)
print('JSON    :', json.dumps(data))
print('ORDINATO:', json.dumps(data, sort_keys=True))

first = json.dumps(data, sort_keys=True)
second = json.dumps(data, sort_keys=True)

print('CORRISPONDENZA NON ORDINATA:', unsorted == first)
print('CORRISPONDENZA ORDINATA    :', first == second)
