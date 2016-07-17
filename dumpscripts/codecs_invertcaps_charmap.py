#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import string

# Mappatura di ogni carattere su se stesso
decoding_map = codecs.make_identity_dict(range(256))

# Genera una lista di coppie di valori ordinali per le lettere 
# minunscole e maiuscole
pairs = zip([ ord(c) for c in string.ascii_lowercase],
            [ ord(c) for c in string.ascii_uppercase])

# Modifica la mappatura per convertire da maiuscolo a minuscolo e da 
# minuscolo a maiuscolo.
decoding_map.update( dict( (upper, lower) for (lower, upper) in pairs) )
decoding_map.update( dict( (lower, upper) for (lower, upper) in pairs) )

# Crea una mappa di codifica a se stante.
encoding_map = codecs.make_encoding_map(decoding_map)

if __name__ == '__main__':
    print codecs.charmap_encode('abc.DEF', 'strict', encoding_map)
    print codecs.charmap_decode('abc.DEF', 'strict', decoding_map)
    print encoding_map == decoding_map
    