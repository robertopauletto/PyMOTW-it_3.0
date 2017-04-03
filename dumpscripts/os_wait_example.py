# os_wait_example.py

import os
import sys
import time

for i in range(2):
    print('GENITORE {}: Forking {}'.format(os.getpid(), i))
    worker_pid = os.fork()
    if not worker_pid:
        print('WORKER {}: In partenza'.format(i))
        time.sleep(2 + i)
        print('WORKER {}: Sta finendo'.format(i))
        sys.exit(i)

for i in range(2):
    print('GENITORE: In attesa di {}'.format(i))
    done = os.wait()
    print('GENITORE: Figlio completato:', done)
