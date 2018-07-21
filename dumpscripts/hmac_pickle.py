# hmac_pickle.py

import hashlib
import hmac
import io
import pickle
import pprint

def make_digest(message):
    "Restituisce una impronta di messaggio per message"
    hash = hmac.new(
        b'la-chiave-segreta-condivisa-va-qui',
        message,
        hashlib.sha1,
    )
    return hash.hexdigest().encode('utf-8')


class SimpleObject:
    """Dimostra la verifica di un impronta di messaggio prima di
    deserializzarlo
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# Simula un socket o pipe su cui scrivere con un buffer
out_s = io.BytesIO()

# Scrive un oggetto valido nel flusso:
# digest\nlength\npickle
o = SimpleObject('impronta di messaggio corrisponde')
pickled_data = pickle.dumps(o)
digest = make_digest(pickled_data)
header = b'%s %d\n' % (digest, len(pickled_data))
print('IN SCRITTURA: {}'.format(header))
out_s.write(header)
out_s.write(pickled_data)

# Scrive un oggetto non valido per il flusso
o = SimpleObject('impronta di messaggio non corrisponde')
pickled_data = pickle.dumps(o)
digest = make_digest(b'non utilizzo i dati serializzati')
header = b'%s %d\n' % (digest, len(pickled_data))
print('IN SCRITTURA: {}'.format(header))
out_s.write(header)
out_s.write(pickled_data)

out_s.flush()

# Simula un socket o pipe leggibile con un buffer
in_s = io.BytesIO(out_s.getvalue())

# Legge i dati
while True:
    first_line = in_s.readline()
    if not first_line:
        break
    incoming_digest, incoming_length = first_line.split(b' ')
    incoming_length = int(incoming_length.decode('utf-8'))
    print('\nIN LETTURA:', incoming_digest, incoming_length)

    incoming_pickled_data = in_s.read(incoming_length)

    actual_digest = make_digest(incoming_pickled_data)
    print('REALI:', actual_digest)

    if hmac.compare_digest(actual_digest, incoming_digest):
        obj = pickle.loads(incoming_pickled_data)
        print('OK:', obj)
    else:
        print('ATTENZIONE: Dati corrotti')







