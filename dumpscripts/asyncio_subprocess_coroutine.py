# asyncio_subprocess_coroutine.py

import asyncio
import asyncio.subprocess


def _parse_results(output):
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



async def run_df():
    print('in run_df')

    buffer = bytearray()

    create = asyncio.create_subprocess_exec(
        'df', '-hl',
        stdout=asyncio.subprocess.PIPE,
    )
    print('processo lanciato')
    proc = await create
    print('processo partito {}'.format(proc.pid))

    while True:
        line = await proc.stdout.readline()
        print('letto {!r}'.format(line))
        if not line:
            print('non ci sono più risultati dal comando')
            break
        buffer.extend(line)

    print('in attesa di completamento del processo')
    await proc.wait()

    return_code = proc.returncode
    print('codice di ritorno {}'.format(return_code))
    if not return_code:
        cmd_output = bytes(buffer).decode()
        results = _parse_results(cmd_output)
    else:
        results = []

    return (return_code, results)

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
        run_df()
    )
finally:
    event_loop.close()

if return_code:
    print('errore in uscita {}'.format(return_code))
else:
    print('\nSpazio libero:')
    for r in results:
        print('{Mounted:25}: {Avail}'.format(**r))
