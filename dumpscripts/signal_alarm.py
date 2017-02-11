# signal_alarm.py

import signal
import time


def receive_alarm(signum, stack):
    print('Allarme :', time.ctime())

# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print('Prima:', time.ctime())
time.sleep(4)
print('Dopo :', time.ctime())
