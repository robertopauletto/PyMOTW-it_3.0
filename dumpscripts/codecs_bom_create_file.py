import codecs
from codecs_to_hex import to_hex

# Sceglie la versione non-nativa dell'encodign UTF-16 
if codecs.BOM_UTF16 == codecs.BOM_UTF16_BE:
    bom = codecs.BOM_UTF16_LE
    encoding = 'utf_16_le'
else:
    bom = codecs.BOM_UTF16_BE
    encoding = 'utf_16_be'

print 'Ordine nativo     :', to_hex(codecs.BOM_UTF16, 2)
print 'Ordine selezionato:', to_hex(bom, 2)

# Codifica il testo.
encoded_text = u'pi: \u03c0'.encode(encoding)
print '{:14}: {:}'.format(encoding, to_hex(encoded_text, 2))
#print '%s: %s' % (encoding[:14], to_hex(encoded_text, 2))

with open('non-native-encoded.txt', mode='wb') as f:
    # Scrive il byte-order marker selezionato.  Non e' incluso nel
    # testo codificato in quanto la cosa e' stata resa esplicita in fase di 
    # selezione della codifica
    f.write(bom)
    # Scrive la stringa di byte per il testo codificato.
    f.write(encoded_text)
