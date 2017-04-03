# signal_child.py

import os
import signal
import time
import sys

pid = os.getpid()
received = False


def signal_usr1(signum, frame):
    "Callback chiamato quando viene ricevuto un segnale"
    global received
    received = True
    print('FIGLIO {:>6}: Ricevuto USR1'.format(pid))
    sys.stdout.flush()


print('FIGLIO {:>6}: Impostazione del gestore di segnale'.format(pid))
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)
print('FIGLIO {:>6}: In pausa in attesa del segnale'.format(pid))
sys.stdout.flush()
time.sleep(3)

if not received:
    print('FIGLIO {:>6}: Segnale mai ricevuto'.format(pid))
