# os_waitpid_example.py

import os
import sys
import time

workers = []
for i in range(2):
    print('GENITORE {}: Forking {}'.format(os.getpid(), i))
    worker_pid = os.fork()
    if not worker_pid:
        print('WORKER {}: In partenza'.format(i))
        time.sleep(2 + i)
        print('WORKER {}: Sta finendo'.format(i))
        sys.exit(i)
    workers.append(worker_pid)

for pid in workers:
    print('GENITORE: In attesa di  {}'.format(pid))
    done = os.waitpid(pid, 0)
    print('GENITORE: Figlio completato:', done)
