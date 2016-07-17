from codecs_to_hex import to_hex

text = u'pi: p'
encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')

print 'Originali   :', repr(text)
print 'Codificati  :', to_hex(encoded, 1), type(encoded)
print 'Decodificati:', repr(decoded), type(decoded)