# signal_ignore.py

import signal
import os
import time


def do_exit(sig, stack):
    raise SystemExit('In uscita')

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print('Il mio PID:', os.getpid())

signal.pause()
