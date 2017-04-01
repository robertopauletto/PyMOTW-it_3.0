# decimal_create.py

import decimal

fmt = '{0:<25} {1:<25}'

print(fmt.format('Input', 'Output'))
print(fmt.format('-' * 25, '-' * 25))

# Intero
print(fmt.format(5, decimal.Decimal(5)))

# Stringa
print(fmt.format('3.14', decimal.Decimal('3.14')))

# Virgola mobile
f = 0.1
print(fmt.format(repr(f), decimal.Decimal(str(f))))
print('{:<0.23g} {:<25}'.format(
    f,
    str(decimal.Decimal.from_float(f))[:25])
)
