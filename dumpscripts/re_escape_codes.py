# re_escape_codes.py

from re_test_patterns import test_patterns

test_patterns(
    'A prime #1 example!',
    [(r'\d+', 'sequenza di cifre'),
     (r'\D+', 'sequenza di non cifre'),
     (r'\s+', 'sequenza di whitespace'),
     (r'\S+', 'sequenza di non whitespace'),
     (r'\w+', 'caratteri alfanumerici'),
     (r'\W+', 'non alfanumerici')],
)
