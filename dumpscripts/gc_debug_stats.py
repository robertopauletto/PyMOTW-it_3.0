# gc_debug_stats.py

import gc

gc.set_debug(gc.DEBUG_STATS)

gc.collect()
print('Uscita')
