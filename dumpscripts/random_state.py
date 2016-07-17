# random_state.py

import random
import os
import pickle

if os.path.exists('state.dat'):
    # Ripristino dello stato precedentemente salvato
    print('Trovato state.dat, inizializzazione del modulo random')
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # Si usa uno stato di partenza noto
    print('state.dat non trovato, utilizzo un valore seme')
    random.seed(1)

# Produce valori casuali
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()

# Salva lo state per la prossima volta
with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

# Produce ulteriori valori casuali
print('\nDopo il salvataggio dello stato:')
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()
