#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import timeit

iterations = 1000

def show_results(title, result, iterations):
    "Stampa i risultati in microsecondi per passaggio e per voce"
    per_pass = 1000000 * (result / iterations)
    print '%s:\t%.2f usec/passaggio' % (title, per_pass)


adler32 = timeit.Timer(
    stmt="zlib.adler32(data)",
    setup="import zlib; data=open('lorem.txt','r').read() * 10", 
    )
show_results('Adler32, separato     ', adler32.timeit(iterations), iterations)

adler32_running = timeit.Timer(
    stmt="cksum = zlib.adler32(data, cksum)",
    setup="import zlib; data=open('lorem.txt','r').read() * 10; cksum = zlib.adler32(data)", 
    )
show_results('Adler32, in esecuzione', adler32_running.timeit(iterations), iterations)

crc32 = timeit.Timer(
    stmt="zlib.crc32(data)",
    setup="import zlib; data=open('lorem.txt','r').read() * 10", 
    )
show_results('CRC-32, separato     ', crc32.timeit(iterations), iterations)

crc32_running = timeit.Timer(
    stmt="cksum = zlib.crc32(data, cksum)",
    setup="import zlib; data=open('lorem.txt','r').read() * 10; cksum = zlib.crc32(data)", 
    )
show_results('CRC-32, in esecuzione', crc32_running.timeit(iterations), iterations)
