# asyncio_signal.py

import asyncio
import functools
import os
import signal


def signal_handler(name):
    print('signal_handler({!r})'.format(name))


event_loop = asyncio.get_event_loop()

event_loop.add_signal_handler(
    signal.SIGHUP,
    functools.partial(signal_handler, name='SIGHUP'),
)
event_loop.add_signal_handler(
    signal.SIGUSR1,
    functools.partial(signal_handler, name='SIGUSR1'),
)
event_loop.add_signal_handler(
    signal.SIGINT,
    functools.partial(signal_handler, name='SIGINT'),
)


async def send_signals():
    pid = os.getpid()
    print('Partenza di send_signals per {}'.format(pid))

    for name in ['SIGHUP', 'SIGHUP', 'SIGUSR1', 'SIGINT']:
        print('sending {}'.format(name))
        os.kill(pid, getattr(signal, name))
        # La cessione del controllo consente al gestore del segnale di essere
        # eseguito visto che il segnale non interrompe il flusso del programma
        # in altro modo
        print('cessione del controllo')
        await asyncio.sleep(0.01)
    return


try:
    event_loop.run_until_complete(send_signals())
finally:
    event_loop.close()
