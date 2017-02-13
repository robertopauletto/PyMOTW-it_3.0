# subprocess_signal_setpgrp.py

import os
import signal
import subprocess
import tempfile
import time
import sys


def show_setting_prgrp():
    print('Chiamata di os.setpgrp() da {}'.format(os.getpid()))
    os.setpgrp()
    print('Il gruppo di procsso è ora {}'.format(
        os.getpid(), os.getpgrp()))
    sys.stdout.flush()


script = '''#!/bin/sh
echo "Shell script in esecuzione $$"
set -x
python3 signal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(
    ['sh', script_file.name],
    preexec_fn=show_setting_prgrp,
)
print('GENITORE      : In pausa prima di segnalare {}...'.format(
    proc.pid))
sys.stdout.flush()
time.sleep(1)
print('GENITORE      : Segnalazione del gruppo di processo {}'.format(
    proc.pid))
sys.stdout.flush()
os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)
