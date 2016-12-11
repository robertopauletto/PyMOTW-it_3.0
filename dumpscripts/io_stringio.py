# io_stringio.py

import io

# Scrittura verso un buffer
output = io.StringIO()
output.write('Questo va nel buffer. ')
print('Anche questo.', file=output)

# Recupero dei valori scritti
print(output.getvalue())

output.close()  # scarica il buffer in memoria

# Inizializza un buffer in lettura
input = io.StringIO('Valore iniziale per il buffer in lettura')

# Legge dal buffer
print(input.read())
