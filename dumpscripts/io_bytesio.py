# io_textiowrapper.py

import io

# Scrittura verso un buffer
output = io.BytesIO()
wrapper = io.TextIOWrapper(
    output,
    encoding='utf-8',
    write_through=True,
)
output.write('Questo va nel buffer. '.encode('utf-8'))
output.write('ÁÇÊ'.encode('utf-8'))

# Recupero dei valori scritti
print(output.getvalue())

output.close()  # scarica il buffer in memoria

# Inizializza un buffer in lettura
input = io.BytesIO(b'Valore iniziale per il buffer in lettura')

# Legge dal buffer
print(input.read())
