# asyncio_debug.py

import argparse
import asyncio
import logging
import sys
import time
import warnings

parser = argparse.ArgumentParser('debugging asyncio')
parser.add_argument(
    '-v',
    dest='verbose',
    default=False,
    action='store_true',
)
args = parser.parse_args()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)7s: %(message)s',
    stream=sys.stderr,
)
LOG = logging.getLogger('')


async def inner():
    LOG.info('inner in partenza')
    # Usa un passo bloccante via sleep per simulare
    # esecuzione di lavoro all'interno della funzione
    time.sleep(0.1)
    LOG.info('inner completata')


async def outer(loop):
    LOG.info('outer in partenza')
    await asyncio.ensure_future(loop.create_task(inner()))
    LOG.info('outer completata')


event_loop = asyncio.get_event_loop()
if args.verbose:
    LOG.info('debugging abilitato')

    # Enable debugging
    event_loop.set_debug(True)

    # Imposta la soglia per attività "lente" molto bassa a scopi
    # illustrativi. Il valore predefinito è 0.1, o 100 millisecondi.
    event_loop.slow_callback_duration = 0.001

    # Segnala tutti gli errori gestiti dalle risorse asincrone
    warnings.simplefilter('always', ResourceWarning)

LOG.info('entrata nel ciclo di eventi')
event_loop.run_until_complete(outer(event_loop))
