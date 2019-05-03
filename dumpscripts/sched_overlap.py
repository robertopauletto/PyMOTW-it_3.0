# sched_overlap.py

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def long_event(name):
    print('INIZIO EVENTO :', time.ctime(time.time()), name)
    time.sleep(2)
    print('FINE EVENTO:', time.ctime(time.time()), name)


print('PARTENZA:', time.ctime(time.time()))
scheduler.enter(2, 1, long_event, ('primo',))
scheduler.enter(3, 1, long_event, ('secondo',))

scheduler.run()
