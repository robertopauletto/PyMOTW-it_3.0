# signal_threads_alarm.py

import signal
import threading
import time


def signal_handler(num, stack):
    print(time.ctime(), 'Allarme in',
          threading.currentThread().name)

signal.signal(signal.SIGALRM, signal_handler)


def use_alarm():
    t_name = threading.currentThread().name
    print(time.ctime(), 'Impostazione allarme in', t_name)
    signal.alarm(1)
    print(time.ctime(), 'In pausa per', t_name)
    time.sleep(3)
    print(time.ctime(), 'Pausa terminata in', t_name)

# Inizia un thread che non riceverà il segnale
alarm_thread = threading.Thread(
    target=use_alarm,
    name='alarm_thread',
)
alarm_thread.start()
time.sleep(0.1)

# Attende il thread per vedere il signale (non succederà!)
print(time.ctime(), 'In attesa di', alarm_thread.name)
alarm_thread.join()

print(time.ctime(), 'Uscita normale')
