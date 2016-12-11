# io_textiowrapper.py

import io

# Scrittura verso un buffer
output = io.BytesIO()
wrapper = io.TextIOWrapper(
    output,
    encoding='utf-8',
    write_through=True,
)
wrapper.write('Questo va nel buffer. ')
wrapper.write('ÁÇÊ')

# Recupero dei valori scritti
print(output.getvalue())

output.close()  # scarica il buffer in memoria

# Inizializza un buffer in lettura
input = io.BytesIO(
    b'Valore iniziale per il buffer in lettura' + 'ÁÇÊ'.encode('utf-8')
)
wrapper = io.TextIOWrapper(input, encoding='utf-8')

# Legge dal buffer
print(wrapper.read())
