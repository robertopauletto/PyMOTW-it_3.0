# json_mixed_data.py

import json

decoder = json.JSONDecoder()


def get_decoded_and_remainder(input_data):
    obj, end = decoder.raw_decode(input_data)
    remaining = input_data[end:]
    return (obj, end, remaining)


encoded_object = '[{"a": "A", "c": 3.0, "b": [2, 4]}]'
extra_text = 'Questo testo non è JSON.'

print('JSON davanti:')
data = ' '.join([encoded_object, extra_text])
obj, end, remaining = get_decoded_and_remainder(data)

print('Oggetto                   :', obj)
print('Fine dell\'input elaborato:', end)
print('Testo rimanente           :', repr(remaining))

print()
print('JSON incorporato:')
try:
    data = ' '.join([extra_text, encoded_object, extra_text])
    obj, end, remaining = get_decoded_and_remainder(data)
except ValueError as err:
    print('ERRORE:', err)
