# os_fork_example.py
import os

pid = os.fork()

if pid:
    print('Id del processo figlio:', pid)
else:
    print('Sono il figlio')
