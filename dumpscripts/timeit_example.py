# timeit_example.py

import timeit

# using setitem
t = timeit.Timer("print('istruzione principale')", "print('impostazione')")

print('TIMEIT:')
print(t.timeit(2))

print('RIPETE:')
print(t.repeat(3, 2))
