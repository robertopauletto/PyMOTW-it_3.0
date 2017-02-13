# subprocess_popen2.py
import subprocess

print('popen2:')

proc = subprocess.Popen(
    ['cat', '-'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)
msg = 'attraverso stdin a stdout'.encode('utf-8')
stdout_value = proc.communicate(msg)[0].decode('utf-8')
print('passa attraverso:', repr(stdout_value))
