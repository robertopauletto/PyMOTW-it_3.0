# sys_int_info.py

import sys

print('Numero di bit usati per contenete ciascuna cifra:',
      sys.int_info.bits_per_digit)
print('Dimensione in byte del tipo C usato per contenere ciascuna cifra:',
      sys.int_info.sizeof_digit)
