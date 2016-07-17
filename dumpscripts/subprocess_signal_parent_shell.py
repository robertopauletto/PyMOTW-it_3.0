#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import signal
import subprocess
import tempfile
import time
import sys

script = '''#!/bin/sh
echo "Shell script in esecuzione $$"
set -x
python signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(['sh %s' % script_file.name], shell=True, close_fds=True)
print 'GENITORE: In pausa prima di inviare il segnale al figlio %s...' % proc.pid
sys.stdout.flush()
time.sleep(1)
print 'GENITORE: Segnalazione al figlio  %s' % proc.pid
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
time.sleep(3)
