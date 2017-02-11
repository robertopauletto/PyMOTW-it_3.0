# subprocess_run_output.py

import subprocess

completed = subprocess.run(
    ['ls', '-1', '/home/robby/test'],
    stdout=subprocess.PIPE,
)
print('returncode:', completed.returncode)
print('Ci sono {} byte in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8'))
)
