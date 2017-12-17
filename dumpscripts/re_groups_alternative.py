# re_groups_alternative.py

from re_test_patterns_groups import test_patterns

test_patterns(
    'abbaabbba',
    [(r'a((a+)|(b+))', 'a poi sequenza di a o sequenza di b'),
     (r'a((a|b)+)', 'a poi sequenza di [ab]')],
)
