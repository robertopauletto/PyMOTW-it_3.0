#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import profile
import pstats
from profile_fibonacci_memoized import fib, fib_seq

# Legge tutti e 5 i file di statistica in un singolo oggetto
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_%d.stats' % i)
stats.strip_dirs()
stats.sort_stats('cumulative')

# limita l'output alle righe che contengono  "(fib" 
stats.print_stats('\(fib')

