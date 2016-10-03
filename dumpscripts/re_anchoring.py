# re_anchoring.py

from re_test_patterns import test_patterns

test_patterns(
    'Trova in parte di testo -- con punteggiatura.',
    [(r'^\w+', 'parola ad inizio stringa'),
     (r'\A\w+', 'parola ad inizio stringa'),
     (r'\w+\S*$', 'parola verso la fine della stringa, senza punteggiatura'),
     (r'\w+\S*\Z', 'parola verso la fine della stringa, senza punteggiatura'),
     (r'\w*t\w*', 'parola che contiene t'),
     (r'\bt\w+', 't ad inizio della parola'),
     (r'\w+t\b', 't alla fine della parola'),
     (r'\Bt\B', 't, non all\'inizio o fine della parola')],
)
