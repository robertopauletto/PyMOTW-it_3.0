# decimal_instance_context.py

import decimal

# Imposta un contesto con precisione limiata
c = decimal.getcontext().copy()
c.prec = 3

# Crea una propria costante
pi = c.create_decimal('3.1415')

# Il falore della costante viene arrotondato
print('PI GRECO :', pi)

# Il risultato derivato dall'uso della costante usa il contesto globale
print('RISULTATO:', decimal.Decimal('2.01') * pi)
