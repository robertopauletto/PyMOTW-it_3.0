# re_charset.py

from re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('[ab]', 'sia a che b'),
     ('a[ab]+', 'a seguito da uno o più a oppure b'),
     ('a[ab]+?', 'a seguito da uno o più a oppure b, non greedy')],
)
