# random_shuffle.py

import random
import itertools

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('\u2665', '\u2666', '\u2663', '\u2660')


def new_deck():
    return [
        # Si utilizzano due caratteri per il valore in modo che le stringhe
        # abbiano una lunghezza consistente.
        '{:>2}{}'.format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS),
            SUITS,
        )
    ]


def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()

# Si crea un nuovo mazzo, con le carte ordinate
deck = new_deck()
print('Mazzo Iniziale :')
show_deck(deck)

# Si mescola il mazzo per rendere l'ordine casuale
random.shuffle(deck)
print('\nMazzo Mescolato:')
show_deck(deck)

# Si distribuiscono 4 mani di 5 carte ciascuna
hands = [[], [], [], []]

for i in range(5):
    for h in hands:
        h.append(deck.pop())

# Si mostrano le mani
print('\nMani:')
for n, h in enumerate(hands):
    print('{}:'.format(n + 1), end=' ')
    for c in h:
        print(c, end=' ')
    print()

# Si mostra la rimanenza del mazzo
print('\nRimaste nel mazzo:')
show_deck(deck)
