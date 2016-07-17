# functools_reduce_short_sequences.py

import functools


def do_reduce(a, b):
    print('do_reduce({}, {})'.format(a, b))
    return a + b


print('Singolo elemento in sequenza:',
      functools.reduce(do_reduce, [1]))

print('Single elemento in sequenza con inizializzatore:',
      functools.reduce(do_reduce, [1], 99))

print('Sequenza vuota con inizializzatore:',
      functools.reduce(do_reduce, [], 99))

try:
    print('Sequenza vuota:', functools.reduce(do_reduce, []))
except TypeError as err:
    print('ERRORE: {}'.format(err))
