# re_charset_dot.py

from re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('a.', 'a seguito da qualsiasi carattere'),
     ('b.', 'b seguito da qualsiasi carattere'),
     ('a.*b', 'a seguito da qualunque cosa che finisca per b'),
     ('a.*?b', 'a seguito da qualunque cosa, che finisca per b')],
)
