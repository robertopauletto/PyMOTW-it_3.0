# sys_getrefcount.py

import sys

one = []
print('Alla partenza      :', sys.getrefcount(one))

two = one

print('Secondo riferimento:', sys.getrefcount(one))

del two

print('Dopo del            :', sys.getrefcount(one))
