# subprocess_popen3.py

import subprocess

print('popen3:')
proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
msg = 'attraverso stdin a stdout'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(msg)
print('passa attraverso:', repr(stdout_value.decode('utf-8')))
