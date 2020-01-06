# asyncio_getnameinfo.py

import asyncio
import logging
import socket
import sys


TARGETS = [
    ('104.130.43.121', 443),
    ('198.91.81.13', 80),
]


async def main(loop, targets):
    for target in targets:
        info = await loop.getnameinfo(target)
        print('{:15}: {} {}'.format(target[0], *info))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, TARGETS))
finally:
    event_loop.close()
