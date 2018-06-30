# pickle_stream.py

import io
import pickle
import pprint


class SimpleObject:

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return


data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('preserva'))
data.append(SimpleObject('ultimo'))

# Simula a file.
out_s = io.BytesIO()

# Scrive verso lo stream
for o in data:
    print('IN SCRITTURA : {} ({})'.format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

# Imposta uno stream leggibile
in_s = io.BytesIO(out_s.getvalue())

# Legge i dati
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print('LETTURA      : {} ({})'.format(
            o.name, o.name_backwards))
