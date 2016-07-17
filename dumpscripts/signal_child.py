#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import signal
import time
import sys

pid = os.getpid()
received = False

def signal_usr1(signum, frame):
    """Callback chiamato quando viene ricevuto un segnale"""
    global received
    received = True
    print 'FIGLIO %s: Ricevuto USR1' % pid
    sys.stdout.flush()

print 'FIGLIO %s: Impostazione del gestore di segnale' % pid
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)
print 'FIGLIO %s: In pausa in attesa del segnale' % pid
sys.stdout.flush()
time.sleep(3)

if not received:
    print 'FIGLIO %s: Segnale mai ricevuto' % pid
