# math_fsum.py

import math

values = [0.1] * 10

print('Valori in input:', values)

print('sum()       : {:.20f}'.format(sum(values)))

s = 0.0
for i in values:
    s += i
print('ciclo-for   : {:.20f}'.format(s))

print('math.fsum() : {:.20f}'.format(math.fsum(values)))
