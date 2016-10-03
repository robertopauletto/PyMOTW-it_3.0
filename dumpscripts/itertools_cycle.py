# itertools_cycle.py

from itertools import *

for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)
