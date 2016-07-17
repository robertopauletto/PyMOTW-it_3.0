#!/usr/bin/env python
# -*- coding: Latin-1 -*-
import json

decoder = json.JSONDecoder()
def get_decoded_and_remainder(input_data):
    obj, end = decoder.raw_decode(input_data)
    remaining = input_data[end:]
    return (obj, end, remaining)

encoded_object = '[{"a": "A", "c": 3.0, "b": [2, 4]}]'
extra_text = 'Testo NON JSON.'

print 'Prima JSON:'
obj, end, remaining = get_decoded_and_remainder(' '.join([encoded_object, extra_text]))
print 'Oggetto             :', obj
print 'Fine input elaborato:', end
print 'Testo rimanente     :', repr(remaining)

print
print 'JSON contenuto:'
try:
    obj, end, remaining = get_decoded_and_remainder(
        ' '.join([extra_text, encoded_object, extra_text])
        )
except ValueError, err:
    print 'ERRORE:', err

    

