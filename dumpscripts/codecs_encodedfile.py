# codecs_encodedfile.py
from codecs_to_hex import to_hex

import codecs
import io

# Versione grezza dei dati originali
data = 'français'

# Codifica manuale come UTF-8
utf8 = data.encode('utf-8')
print('Parte com UTF-8     :', to_hex(utf8, 1))


# Imposta un buffer in uscita, quindi lo incapsula come EncodedFile.
output = io.BytesIO()
encoded_file = codecs.EncodedFile(output, data_encoding='utf-8',
                                  file_encoding='utf-16')
encoded_file.write(utf8)

# Recupera il contenuto del buffer con codifica della stringa
# di byte in UTF-16
utf16 = output.getvalue()
print('Codificato in UTF-16:', to_hex(utf16, 2))

# Imposta un altro buffer con i dati UTF-16 per la lettura
# e li incapsula con un altro EncodedFile.
buffer = io.BytesIO(utf16)
encoded_file = codecs.EncodedFile(buffer, data_encoding='utf-8',
                                  file_encoding='utf-16')

# Legge la versione dati codificata come UTF-8
recoded = encoded_file.read()
print('Ritorna a UTF-8     :', to_hex(recoded, 1))
