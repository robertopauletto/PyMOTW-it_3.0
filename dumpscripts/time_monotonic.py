# time_monotonic.py

import time

start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print('inizio    : {:>9.2f}'.format(start))
print('fine      : {:>9.2f}'.format(end))
print('intervallo: {:>9.2f}'.format(end - start))
