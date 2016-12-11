# time_get_clock_info.py

import textwrap
import time


# Esempio modificato dal traduttore per gestire la traduzione degli
# orologi disponibili
available_clocks = [
    ('clock', time.clock, 'orologio'),
    ('monotonic', time.monotonic, 'monotonico'),
    ('perf_counter', time.perf_counter, 'misuratore di prestazioni'),
    ('process_time', time.process_time, 'tempo di elaborazione'),
    ('time', time.time, 'tempo'),
]

for clock_name, func, translation in available_clocks:
    print(textwrap.dedent('''\
    {name}:
        modificabile   : {info.adjustable}
        implementazione: {info.implementation}
        monotonico     : {info.monotonic}
        risoluzione    : {info.resolution}
        attuale        : {current}
    ''').format(
        name=translation,
        info=time.get_clock_info(clock_name),
        current=func())
    )
