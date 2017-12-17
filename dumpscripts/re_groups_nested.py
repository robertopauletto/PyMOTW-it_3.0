# re_groups_nested.py

from re_test_patterns_groups import test_patterns

test_patterns(
    'abbaabbba',
    [(r'a((a*)(b*))', 'a seguita da 0-n a e 0-n b')],
)
