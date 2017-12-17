# codecs_invertcaps_charmap.py

import codecs
import string

# Mappa ogni caratter a se stesso
decoding_map = codecs.make_identity_dict(range(256))

# Fa una lista di coppie di valori ordinali per le
# lettere minuscole e maiuscole
pairs = list(zip(
    [ord(c) for c in string.ascii_lowercase],
    [ord(c) for c in string.ascii_uppercase],
))

# Modifica la mappatura per convertire le maiuscole in minuscole e viceversa
decoding_map.update({
    upper: lower
    for (lower, upper)
    in pairs
})
decoding_map.update({
    lower: upper
    for (lower, upper)
    in pairs
})

# Crea una mappa di codifica separata
encoding_map = codecs.make_encoding_map(decoding_map)

if __name__ == '__main__':
    print(codecs.charmap_encode('abcDEF', 'strict',
                                encoding_map))
    print(codecs.charmap_decode(b'abcDEF', 'strict',
                                decoding_map))
    print(encoding_map == decoding_map)
