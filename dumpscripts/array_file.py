# array_file.py

import array
import binascii
import tempfile

a = array.array('i', range(5))
print('A1:', a)

# Scrivo un array di cifre in un file
output = tempfile.NamedTemporaryFile()
a.tofile(output.file)  # devo passare un *vero* file
output.flush()

# Leggo i dati grezzi
with open(output.name, 'rb') as input:
    raw_data = input.read()
    print('Contenuto grezzo:', binascii.hexlify(raw_data))

    # Read the data into an array
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2:', a2)
