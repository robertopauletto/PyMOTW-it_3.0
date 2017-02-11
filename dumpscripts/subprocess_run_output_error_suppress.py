# subprocess_run_output_error_suppress.py

import subprocess

try:
    completed = subprocess.run(
        'echo to stdout; echo to stderr 1>&2; exit 1',
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
except subprocess.CalledProcessError as err:
    print('ERRORE:', err)
else:
    print('returncode:', completed.returncode)
    print('stdout è {!r}'.format(completed.stdout))
    print('stderr è {!r}'.format(completed.stderr))
