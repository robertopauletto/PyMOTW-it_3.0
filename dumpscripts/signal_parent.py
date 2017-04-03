# signal_parent.py

import os
import signal
import subprocess
import time
import sys

proc = subprocess.Popen(['python3', 'signal_child.py'])
print('GENITORE: In pausa prima di inviare il segnale...')
sys.stdout.flush()
time.sleep(1)
print('GENITORE: Segnalazione al figlio')
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
