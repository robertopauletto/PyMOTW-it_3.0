# itertools_tee_error.py

from itertools import *

r = islice(count(), 5)
i1, i2 = tee(r)

print('r:', end=' ')
for i in r:
    print(i, end=' ')
    if i > 1:
        break
print()

print('i2:', list(i2))
print('i1:', list(i1))
