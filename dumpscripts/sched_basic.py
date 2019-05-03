# sched_basic.py

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name, start):
    now = time.time()
    elapsed = int(now - start)
    print('EVENTO: {} trascorso={} nome={}'.format(
        time.ctime(now), elapsed, name))


start = time.time()
print('PARTENZA:', time.ctime(start))
scheduler.enter(2, 1, print_event, ('primo', start))
scheduler.enter(3, 1, print_event, ('secondo', start))

scheduler.run()
