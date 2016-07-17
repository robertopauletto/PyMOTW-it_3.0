import base64

original_string = 'Questi sono i dati in chiaro'
print 'Originali   :', original_string

encoded_string = base64.b16encode(original_string)
print 'Codificati  :', encoded_string

decoded_string = base64.b16decode(encoded_string)
print 'Decodificati:', decoded_string

