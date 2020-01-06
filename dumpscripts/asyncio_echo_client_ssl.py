# asyncio_echo_client_coroutine.py

import asyncio
import logging
import ssl
import sys

MESSAGES = [
    b"Questo e' il messaggio. ",
    b"Sara' inviato ",
    b'in parti.',
]
SERVER_ADDRESS = ('localhost', 10000)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()


async def echo_client(address, messages):
    log = logging.getLogger('echo_client')

    log.debug('connessione a {} porta {}'.format(*address))

    # Il certificato è creato con pymotw.com come nome host,
    # il che non corrisponderà quando il codice di esempio viene eseguito
    # altrove, quindi si disabiliti la verifica del nome host
    ssl_context = ssl.create_default_context(
        ssl.Purpose.SERVER_AUTH,
    )
    ssl_context.check_hostname = False
    ssl_context.load_verify_locations('pymotw.crt')
    reader, writer = await asyncio.open_connection(
        *address, ssl=ssl_context)

    # Potrebbe essere writer.writelines() eccetto che
    # avrebbe reso più difficile mestrare ciascuna parte del messaggio
    # che sta per essere spedito..
    for msg in messages:
        writer.write(msg)
        log.debug('sending {!r}'.format(msg))
    # SSL non supporta EOF, quindi si invia un byte null per indicare
    # la fine del messaggio.
    writer.write(b'\x00')
    await writer.drain()

    log.debug('in attesa di risposta')
    while True:
        data = await reader.read(128)
        if data:
            log.debug('ricevuto {!r}'.format(data))
        else:
            log.debug('in chiusura')
            writer.close()
            return

try:
    event_loop.run_until_complete(
        echo_client(SERVER_ADDRESS, MESSAGES)
    )
finally:
    log.debug('chiusura del ciclo di eventi')
    event_loop.close()
