# asyncio_echo_server_protocol.py

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

class EchoServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log = logging.getLogger(
            'EchoServer_{}_{}'.format(*self.address)
        )
        self.log.debug('connessione accettata')

    def data_received(self, data):
        self.log.debug('ricevuto {!r}'.format(data))
        self.transport.write(data)
        self.log.debug('inviato {!r}'.format(data))

    def eof_received(self):
        self.log.debug('ricevuto EOF')
        if self.transport.can_write_eof():
            self.transport.write_eof()

    def connection_lost(self, error):
        if error:
            self.log.error('ERRORE: {}'.format(error))
        else:
            self.log.debug('chiusura')
        super().connection_lost(error)


# Crea il server e lasci che il ciclo finisca la coroutine prima di far
# partire il vero ciclo di eventi.
factory = event_loop.create_server(EchoServer, *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)
log.debug('in partenza on {} porta {}'.format(*SERVER_ADDRESS))


# Entra nel ciclo di eventi in modo permanente per gestire tutte le connessioni
try:
    event_loop.run_forever()
finally:
    log.debug('chiusura del server')
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    log.debug('chiusura del ciclo di eventi')
    event_loop.close()
