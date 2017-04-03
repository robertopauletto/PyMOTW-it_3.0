# os_kill_example.py

import os
import signal
import time


def signal_usr1(signum, frame):
    "Callback chiamto alla ricezione di un segnale"
    pid = os.getpid()
    print('Ricevuto USR1 nel processo {}'.format(pid))

print('Fase di fork...')
child_pid = os.fork()
if child_pid:
    print('GENITORE: In pausa prima di inviare il segnale...')
    time.sleep(1)
    print('GENITORE: In segnalazione {}'.format(child_pid))
    os.kill(child_pid, signal.SIGUSR1)
else:
    print('FIGLIO: Impostazione del gestore di segnale')
    signal.signal(signal.SIGUSR1, signal_usr1)
    print('FIGLIO: In pausa, in attesa del segnale')
    time.sleep(5)
