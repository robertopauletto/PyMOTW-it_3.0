# re_groups_noncapturing.py

from re_test_patterns_groups import test_patterns

test_patterns(
    'abbaabbba',
    [(r'a((a+)|(b+))', 'forma catturante'),
     (r'a((?:a+)|(?:b+))', 'non catturante')],
)
