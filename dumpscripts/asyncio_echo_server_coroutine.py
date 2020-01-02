# asyncio_echo_server_coroutine.py

import asyncio
import logging
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
        if data:
            log.debug('ricevuto {!r}'.format(data))
            writer.write(data)
            await writer.drain()
            log.debug('inviato {!r}'.format(data))
        else:
            log.debug('in chiusura')
            writer.close()
            return


# Crea il server e lascia che ciclo termini la coroutine prima di far
# partire il ciclo di eventi effettivo.
factory = asyncio.start_server(echo, *SERVER_ADDRESS)
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
