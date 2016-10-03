# re_charset_exclude.py

from re_test_patterns import test_patterns

test_patterns(
    'Questa è una porzione di testo -- con punteggiatura.',
    [('[^-. ]+', 'sequenze senza -, ., o spazio')],
)
