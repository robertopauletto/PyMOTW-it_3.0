# codecs_bom_detection.py
import codecs
from codecs_to_hex import to_hex

# Lettura dei dati grezzi
with open('nonnative-encoded.txt', mode='rb') as f:
    raw_bytes = f.read()

print('Grezzo      :', to_hex(raw_bytes, 2))

# Riapertura del file lasciando che codecs identifichi il  BOM
with codecs.open('nonnative-encoded.txt',
                 mode='r',
                 encoding='utf-16',
                 ) as f:
    decoded_text = f.read()

print('Decodificato:', repr(decoded_text))
