# math_hypot.py

import math

print('{:^7} {:^7} {:^10}'.format('X', 'Y', 'Ipotenusa'))
print('{:-^7} {:-^7} {:-^10}'.format('', '', ''))

POINTS = [
    # semplici punti
    (1, 1),
    (-1, -1),
    (math.sqrt(2), math.sqrt(2)),
    (3, 4),  # triangolo 3-4-5
    # sul cerchio
    (math.sqrt(2) / 2, math.sqrt(2) / 2),  # radianti pi/4
    (0.5, math.sqrt(3) / 2),  # radianti pi/3
]

for x, y in POINTS:
    h = math.hypot(x, y)
    print('{:7.2f} {:7.2f} {:7.2f}'.format(x, y, h))
