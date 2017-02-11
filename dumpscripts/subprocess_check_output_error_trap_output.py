# subprocess_check_output_error_trap_output.py

import subprocess

try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2',
        shell=True,
        stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as err:
    print('ERRORE:', err)
else:
    print('Ci sono {} byte in output: {!r}'.format(
        len(output),
        output.decode('utf-8'))
    )
