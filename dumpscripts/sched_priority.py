# sched_priority.py

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name):
    print('EVENTO:', time.ctime(time.time()), name)


now = time.time()
print('PARTENZA:', time.ctime(now))
scheduler.enterabs(now + 2, 2, print_event, ('primo',))
scheduler.enterabs(now + 2, 1, print_event, ('secondo',))

scheduler.run()
