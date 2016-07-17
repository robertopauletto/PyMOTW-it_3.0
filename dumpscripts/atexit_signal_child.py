#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import atexit
import time
import sys

def not_called():
    print 'FIGLIO: il gestore di atexit non dovrebbe essere stato chiamato'

print 'FIGLIO: Registrazione del gestore atexit'
sys.stdout.flush()
atexit.register(not_called)

print 'FIGLIO: In pausa in attesa del segnale'
sys.stdout.flush()
time.sleep(5)