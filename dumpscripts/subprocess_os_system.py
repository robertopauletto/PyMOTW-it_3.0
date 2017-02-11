# subprocess_os_system.py

import subprocess

completed = subprocess.run(['ls', '-1'])
print('codice_di_ritorno:', completed.returncode)
