# collections_deque_maxlen.py

import collections
import random

# Imposta il parametro di random seed in modo da vedere lo stesso
# risultato ogni volta che viene eseguito lo script
random.seed(1)

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)

for i in range(5):
    n = random.randint(0, 100)
    print('n =', n)
    d1.append(n)
    d2.appendleft(n)
    print('D1:', d1)
    print('D2:', d2)
