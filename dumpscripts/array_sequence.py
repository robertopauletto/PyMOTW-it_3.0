# array_sequence.py

import array
import pprint

a = array.array('i', range(3))
print('Iniziale :', a)

a.extend(range(3))
print('Esteso   :', a)

print('Slice    :', a[2:5])

print('Iteratore:')
print(list(enumerate(a)))
