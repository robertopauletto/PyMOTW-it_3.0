# gettext_plural.py

from gettext import translation
import sys

t = translation('plurale', 'locale', fallback=False)
num = int(sys.argv[1])
msg = t.ngettext('{num} significa singolare.',
                 '{num} significa plurale.',
                 num)

# Occorre anche aggiungere i valori al messaggio.
print(msg.format(num=num))
