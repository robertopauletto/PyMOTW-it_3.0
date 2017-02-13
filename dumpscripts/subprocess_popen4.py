# subprocess_popen4.py

import subprocess

print('popen4:')
proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
msg = 'attraverso stdin a stdout\n'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(msg)
print('output combinato:', repr(stdout_value.decode('utf-8')))
print('valore di stderr:', repr(stderr_value))
