# asyncio_subprocess_protocol.py

import asyncio
import functools


async def run_df(loop):
    print('in run_df')

    cmd_done = asyncio.Future(loop=loop)
    factory = functools.partial(DFProtocol, cmd_done)
    proc = loop.subprocess_exec(
        factory,
        'df', '-hl',
        stdin=None,
        stderr=None,
    )
    try:
        print('lancio del processo')
        transport, protocol = await proc
        print('in attesa del completamento del processo')
        await cmd_done
    finally:
        transport.close()

    return cmd_done.result()


class DFProtocol(asyncio.SubprocessProtocol):

    FD_NAMES = ['stdin', 'stdout', 'stderr']

    def __init__(self, done_future):
        self.done = done_future
        self.buffer = bytearray()
        super().__init__()

    def connection_made(self, transport):
        print('processo iniziato {}'.format(transport.get_pid()))
        self.transport = transport

    def pipe_data_received(self, fd, data):
        print('letti {} byte da {}'.format(len(data),
                                           self.FD_NAMES[fd]))
        if fd == 1:
            self.buffer.extend(data)

    def process_exited(self):
        print('processo uscito')
        return_code = self.transport.get_returncode()
        print('codice ritornato {}'.format(return_code))
        if not return_code:
            cmd_output = bytes(self.buffer).decode()
            results = self._parse_results(cmd_output)
        else:
            results = []
        self.done.set_result((return_code, results))

    def _parse_results(self, output):
        print('elaborazione risultati')
        # Il risultato ha una riga di intestazioni, tutte parole singole.
        # Le righe rimanenti sono una per il filesystem, con colonne
        # che corrispondono alle intestazioni (assumendo che nessun punti di
        # montaggio abbia spazi nel nome).
        if not output:
            return []
        lines = output.splitlines()
        headers = lines[0].split()
        devices = lines[1:]
        results = [
            dict(zip(headers, line.split()))
            for line in devices
        ]
        return results


event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
        run_df(event_loop)
    )
finally:
    event_loop.close()

if return_code:
    print('errore in uscita {}'.format(return_code))
else:
    print('\nSpazio libero:')
    for r in results:
        print('{Mounted:25}: {Avail}'.format(**r))
