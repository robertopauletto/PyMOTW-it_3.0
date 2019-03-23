# sys_float_info.py

import sys

print('Differenza più piccola (epsilon):', sys.float_info.epsilon)
print()
print('Cifre (dig)              :', sys.float_info.dig)
print('Cifre mantissa (mant_dig):', sys.float_info.mant_dig)
print()
print('Massimo (max):', sys.float_info.max)
print('Minimo (min):', sys.float_info.min)
print()
print('Radice degli esponenti (radix):', sys.float_info.radix)
print()
print('Massimo esponente per radice (max_exp):',
      sys.float_info.max_exp)
print('Minimo esponente per radice (min_exp):',
      sys.float_info.min_exp)
print()
print('Massimo esponente per potenze di 10 (max_10_exp):',
      sys.float_info.max_10_exp)
print('Minimo esponente per potenze di 10 (min_10_exp):',
      sys.float_info.min_10_exp)
print()
print('Arrotondamento per somma (rounds):', sys.float_info.rounds)
