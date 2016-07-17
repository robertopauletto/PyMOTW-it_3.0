#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import signal
import subprocess
import time

proc = subprocess.Popen('atexit_signal_child.py')
print 'GENITORE: In pausa prima di inviare il segnale...'
time.sleep(1)
print 'GENITORE: Invio segnale al figlio'
os.kill(proc.pid, signal.SIGTERM)