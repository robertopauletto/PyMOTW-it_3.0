# json_simple_types.py

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATI:', repr(data))

data_string = json.dumps(data)
print('JSON:', data_string)
