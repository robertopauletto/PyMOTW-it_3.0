# random_choice.py

import random
import itertools

outcomes = {
    'heads': 0,
    'tails': 0,
}
sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print('Testa:', outcomes['heads'])
print('Croce:', outcomes['tails'])
