# collections_counter_elements.py

import collections

c = collections.Counter('estramamente')
c['z'] = 0
print(c)
print(list(c.elements()))
