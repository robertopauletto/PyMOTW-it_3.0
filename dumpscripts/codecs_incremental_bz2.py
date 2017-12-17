# codecs_incremental_bz2.py
import codecs
import sys

from codecs_to_hex import to_hex

text = b'abcdefghijklmnopqrstuvwxyz\n'
repetitions = 50

print('Lung. testo   :', len(text))
print('Ripetizioni   :', repetitions)
print('Lung. prevista:', len(text) * repetitions)


# Codifica il testo parecchie volte sviluppando un grande ammontare di dati
encoder = codecs.getincrementalencoder('bz2')()
encoded = []

print()
print('In codifica:', end=' ')
last = repetitions - 1
for i in range(repetitions):
    en_c = encoder.encode(text, final=(i == last))
    if en_c:
        print('\nCodificati  : {} byte'.format(len(en_c)))
        encoded.append(en_c)
    else:
        sys.stdout.write('.')

all_encoded = b''.join(encoded)
print()
print('Lunghezza totale codificati:', len(all_encoded))
print()

# Decodifica la stringa di byte un byte alla volta
decoder = codecs.getincrementaldecoder('bz2')()
decoded = []

print('In decodifica:', end=' ')
for i, b in enumerate(all_encoded):
    final = (i + 1) == len(text)
    c = decoder.decode(bytes([b]), final)
    if c:
        print('\nDecodificati : {} caratteri'.format(len(c)))
        print('In decodifica:', end=' ')
        decoded.append(c)
    else:
        sys.stdout.write('.')
print()

restored = b''.join(decoded)

print()
print('Lunghezza totale non compressi:', len(restored))

