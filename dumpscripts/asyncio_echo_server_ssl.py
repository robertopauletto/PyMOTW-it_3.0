# asyncio_echo_server_ssl.py

import asyncio
import logging
import ssl
import sys

SERVER_ADDRESS = ('localhost', 10000)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(name)s: %(message)s',
    stream=sys.stderr,
)
log = logging.getLogger('main')

event_loop = asyncio.get_event_loop()


async def echo(reader, writer):
    address = writer.get_extra_info('peername')
    log = logging.getLogger('echo_{}_{}'.format(*address))
    log.debug('connessione accettata')

    while True:
        data = await reader.read(128)
        terminate = data.endswith(b'\x00')
        data = data.rstrip(b'\x00')
        if data:
            log.debug('ricevuto {!r}'.format(data))
            writer.write(data)
            await writer.drain()
            log.debug('inviato {!r}'.format(data))
        if not data or terminate:
            log.debug('messaggio terminato, chiusura connessione')
            writer.close()
            return


# Il certificato è creato con pymotw.com come nome host,
# il che non corrisponderà quando il codice di esempio viene eseguito
# altrove, quindi si disabiliti la verifica del nome host
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.check_hostname = False
ssl_context.load_cert_chain('pymotw.crt', 'pymotw.key')

# Crea il server e lascia che il ciclo finisca la coroutine prima di
# far partire il ciclo di eventi effettivo
factory = asyncio.start_server(echo, *SERVER_ADDRESS, ssl=ssl_context)
server = event_loop.run_until_complete(factory)
log.debug('in partenza su {} porta {}'.format(*SERVER_ADDRESS))

# Entra nel ciclo di eventi permanentemente per gestire tutte le connesisoni.
try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    log.debug('server in chiusura')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('chiusura del ciclo di eventi')
    event_loop.close()
