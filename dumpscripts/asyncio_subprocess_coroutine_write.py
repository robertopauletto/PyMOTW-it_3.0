# asyncio_subprocess_coroutine_write.py

import asyncio
import asyncio.subprocess


async def to_upper(input):
    print('in to_upper')

    create = asyncio.create_subprocess_exec(
        'tr', '[:lower:]', '[:upper:]',
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    print('processo lanciato')
    proc = await create
    print('pid {}'.format(proc.pid))

    print('communicazione con il processo')
    stdout, stderr = await proc.communicate(input.encode())

    print('in attesa del completamento del processo')
    await proc.wait()

    return_code = proc.returncode
    print('codice di ritorno {}'.format(return_code))
    if not return_code:
        results = bytes(stdout).decode()
    else:
        results = ''

    return (return_code, results)


MESSAGE = """
Questo messaggio sara' convertito a
tutte maiuscole.
"""

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
        to_upper(MESSAGE)
    )
finally:
    event_loop.close()

if return_code:
    print('errore in uscita {}'.format(return_code))
else:
    print('Originale : {!r}'.format(MESSAGE))
    print('Modificato: {!r}'.format(results))
