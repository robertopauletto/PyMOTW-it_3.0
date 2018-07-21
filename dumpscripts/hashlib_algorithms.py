# hashlib_algorithms.py


import hashlib


print('Garantiti:\n{}\n'.format(
    ', '.join(sorted(hashlib.algorithms_guaranteed))))
print('Disponibili:\n{}'.format(
    ', '.join(sorted(hashlib.algorithms_available))))
