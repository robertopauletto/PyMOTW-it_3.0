# subprocess_signal_parent_shell.py

import os
import signal
import subprocess
import tempfile
import time
import sys

script = '''#!/bin/sh
echo "Shell script in esecuzione $$"
set -x
python3 signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(['sh', script_file.name])
print('GENITORE      : In pausa prima di segnalare {}...'.format(
    proc.pid))
sys.stdout.flush()
time.sleep(1)
print('GENITORE      : Segnalazione al figlio {}'.format(proc.pid))
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
time.sleep(3)
