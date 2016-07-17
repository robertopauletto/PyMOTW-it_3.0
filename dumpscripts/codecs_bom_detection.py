import codecs
from codecs_to_hex import to_hex

# Lettura dei dati grezzi
with open('non-native-encoded.txt', mode='rb') as f:
    raw_bytes = f.read()

print 'Raw    :', to_hex(raw_bytes, 2)

# Riapertura del file lasciando che codecs identifichi il  BOM
with codecs.open('non-native-encoded.txt', mode='rt', encoding='utf-16') as f:
    decoded_text = f.read()

print 'Decodificato:', repr(decoded_text)	