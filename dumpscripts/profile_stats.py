# profile_stats.py

import cProfile as profile
import pstats
from profile_fibonacci_memoized import fib, fib_seq

# Crea 5 insiemi di statistiche
for i in range(5):
    filename = 'profile_stats_{}.stats'.format(i)
    profile.run('print({}, fib_seq(20))'.format(i), filename)

# Legge i 5 file di statistica in un singolo oggetto
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_{}.stats'.format(i))

# Toglie i nomi delle directory dai file per il report
stats.strip_dirs()

# Ordina le statistiche per tempo cumulativo trascorso
# nella funzione
stats.sort_stats('cumulative')

stats.print_stats()
