# re_repetition_non_greedy.py

from re_test_patterns import test_patterns

test_patterns(
    'abbaabbba',
    [('ab*?', 'a seguito da zero o più b'),
     ('ab+?', 'a seguito da one o più b'),
     ('ab??', 'a seguito da zero od una b'),
     ('ab{3}?', 'a seguito da tre b'),
     ('ab{2,3}?', 'a seguito da due fino a tre b')],
)
