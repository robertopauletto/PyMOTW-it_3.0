# sched_cancel.py

import sched
import threading
import time

scheduler = sched.scheduler(time.time, time.sleep)

# Imposta variabile globale che può essere modificata daithread
counter = 0


def increment_counter(name):
    global counter
    print('EVENTO:', time.ctime(time.time()), name)
    counter += 1
    print('ADESSO:', counter)


print('PARTENZA:', time.ctime(time.time()))
e1 = scheduler.enter(2, 1, increment_counter, ('E1',))
e2 = scheduler.enter(3, 1, increment_counter, ('E2',))

# Fa partire un thread per eseguire gli eventi
t = threading.Thread(target=scheduler.run)
t.start()

# Ritorna al thread principale, cancella il primo evento pianificato
scheduler.cancel(e1)

# Attende che il pianificatore termini l'esecuzione nel thread
t.join()

print('FINALE:', counter)
