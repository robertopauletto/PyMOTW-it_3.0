# pickle_unpickle.py

import pickle
import pprint

data1 = [{'a': 'A', 'b': 2, 'c': 3.0}]
print('PRIMA  : ', end=' ')
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print('DOPO   : ', end=' ')
pprint.pprint(data2)

print('STESSI?:', (data1 is data2))
print('UGUALI?:', (data1 == data2))
