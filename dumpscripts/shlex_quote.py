# shlex_quote.py

import shlex

examples = [
    "Annidato'SingoloApice",
    'Annidato"DoppioApice',
    'Annidato Spazio',
    '~CarattereSpeciale',
    r'BarraRove\sciata',
]

for s in examples:
    print('ORIGINALE : {}'.format(s))
    print('TRA APICI : {}'.format(shlex.quote(s)))
    print()
