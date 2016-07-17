# collections_deque_rotate.py

import collections

d = collections.deque(range(10))
print('Normale       :', d)

d = collections.deque(range(10))
d.rotate(2)
print('Rotazione destra:', d)

d = collections.deque(range(10))
d.rotate(-2)
print('Rotazione sinistra:', d)
