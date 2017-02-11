# signal_threads.py

import signal
import threading
import os
import time


def signal_handler(num, stack):
    print('Segnale {} ricevuto in {}'.format(
        num, threading.currentThread().name))

signal.signal(signal.SIGUSR1, signal_handler)


def wait_for_signal():
    print('In attesa dell\'entrata del segnale',
          threading.currentThread().name)
    signal.pause()
    print('Attesa terminata')

# Inizia un thread che non riceverà il segnale
receiver = threading.Thread(
    target=wait_for_signal,
    name='ricevente',
)
receiver.start()
time.sleep(0.1)


def send_signal():
    print('Invio del segnale', threading.currentThread().name)
    os.kill(os.getpid(), signal.SIGUSR1)

sender = threading.Thread(target=send_signal, name='mittente')
sender.start()
sender.join()

# Attende il thread per vedere il signale (non succederà!)
print('In attesa di', receiver.name)
signal.alarm(2)
receiver.join()
