# profile_stats_callers.py

import cProfile as profile
import pstats
from profile_fibonacci_memoized import fib, fib_seq

# Legge tutti e 5 i file di statistica in un singolo oggetto
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_{}.stats'.format(i))
stats.strip_dirs()
stats.sort_stats('cumulative')

print('CHIAMANTI IN ENTRATA:')
stats.print_callers('\(fib')

print('CHIAMATE IN USCITA  :')
stats.print_callees('\(fib')
