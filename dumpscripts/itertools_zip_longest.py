# itertools_zip_longest.py

from itertools import *

r1 = range(3)
r2 = range(2)

print('zip si ferma prima:')
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)

print('\nzip_longest elabora tutti i valori:')
print(list(zip_longest(r1, r2)))
