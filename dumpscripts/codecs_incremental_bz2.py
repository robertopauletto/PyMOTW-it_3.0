#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys

from codecs_to_hex import to_hex

text = 'abcdefghijklmnopqrstuvwxyz\n'
repetitions = 50

print 'Lung. testo   :', len(text)
print 'Ripetizioni   :', repetitions
print 'Lung. prevista:', len(text) * repetitions

# Codifica il testo parecchie volte sviluppando un grande ammontare di dati
encoder = codecs.getincrementalencoder('bz2')()
encoded = []

print
print 'Encoding :',
for i in range(repetitions):
    en_c = encoder.encode(text, final = (i==repetitions-1))
    if en_c:
        print '\nCodificati: {} byte'.format(len(en_c))
        encoded.append(en_c)
    else:
        sys.stdout.write('.')
    
bytes = ''.join(encoded)
print
print 'Lung. totale codificati:', len(bytes)
print

# Decodifica la stringa di byte un byte alla volta
decoder = codecs.getincrementaldecoder('bz2')()
decoded = []

print 'Decoding:',
for i, b in enumerate(bytes):
    final= (i+1) == len(text)
    c = decoder.decode(b, final)
    if c:
        print '\nDecodificati : {} caratteri'.format(len(c))
        print 'Decoding:',
        decoded.append(c)
    else:
        sys.stdout.write('.')
print

restored = u''.join(decoded)

print
print 'Lung. totale non compressi:', len(restored)