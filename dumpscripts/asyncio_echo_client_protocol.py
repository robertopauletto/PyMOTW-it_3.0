# asyncio_echo_client_protocol.py

import asyncio
import functools
import logging
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

class EchoClient(asyncio.Protocol):

    def __init__(self, messages, future):
        super().__init__()
        self.messages = messages
        self.log = logging.getLogger('EchoClient')
        self.f = future

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.log.debug(
            'connessione a {} porta {}'.format(*self.address)
        )
        # Potrebbe essere transport.writelines() eccetto che
        # avrebbe reso più difficile mestrare ciascuna parte del messaggio
        # che sta per essere spedito..
        for msg in self.messages:
            transport.write(msg)
            self.log.debug('in invio {!r}'.format(msg))
        if transport.can_write_eof():
            transport.write_eof()

    def data_received(self, data):
        self.log.debug('ricevuto {!r}'.format(data))

    def eof_received(self):
        self.log.debug('ricevuto EOF')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)

    def connection_lost(self, exc):
        self.log.debug('il server ha chiuso la connessione')
        self.transport.close()
        if not self.f.done():
            self.f.set_result(True)
        super().connection_lost(exc)


client_completed = asyncio.Future()

client_factory = functools.partial(
    EchoClient,
    messages=MESSAGES,
    future=client_completed,
)
factory_coroutine = event_loop.create_connection(
    client_factory,
    *SERVER_ADDRESS,
)

log.debug('in attesa del client per completare')
try:
    event_loop.run_until_complete(factory_coroutine)
    event_loop.run_until_complete(client_completed)
finally:
    log.debug('chiusura del ciclo di eventi')
    event_loop.close()
