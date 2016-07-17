#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import locale
import os
import pprint
import codecs
import sys

sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

# Impostazioni predefinite in base all'ambiente dell'utente.
locale.setlocale(locale.LC_ALL, '')

print 'Impostazioni ambiente:'
for env_name in ['LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE']:
    print '\t%s = %s' % (env_name, os.environ.get(env_name, ''))

# Qual'è la localizzazione?
print
print 'Localizzazione dall\'ambiente:', locale.getlocale()

template = """
Formattazione numerica:

  Separatore decimale       : "%(decimal_point)s"
  Posizioni raggruppamento  : %(grouping)s
  Separatore migliaia       : "%(thousands_sep)s"

Formattazione di valuta:

  Simbolo valuta internazionale             : "%(int_curr_symbol)r"
  Simbolo valuta locale                     : %(currency_symbol)r (%(currency_symbol_u)s)
  Simbolo che precede un valore positivo    : %(p_cs_precedes)s
  Simbolo che precede un valore negativo    : %(n_cs_precedes)s
  Separatore decimale                       : "%(mon_decimal_point)s"
  Cifre in valori frazionari                : %(frac_digits)s
  Cifre in valori frazionari, internazionale: %(int_frac_digits)s
  Posizioni raggruppamento                  : %(mon_grouping)s
  Separatore migliaia                       : "%(mon_thousands_sep)s"
  Segno positivo                            : "%(positive_sign)s"
  Posizione segno positivo                  : %(p_sign_posn)s
  Segno negativo                            : "%(negative_sign)s"
  Posizione segno negativo                  : %(n_sign_posn)s

"""

sign_positions = {
    0 : 'Racchiuso tra parentesi',
    1 : 'Prima di valore e simbolo',
    2 : 'Dopo valore e simbolo',
    3 : 'Prima del valore',
    4 : 'Dopo il valore',
    locale.CHAR_MAX : 'Non specificato',
    }

info = {}
info.update(locale.localeconv())
info['p_sign_posn'] = sign_positions[info['p_sign_posn']]
info['n_sign_posn'] = sign_positions[info['n_sign_posn']]
# converte il simbolo di valuta in unicode
info['currency_symbol_u'] = info['currency_symbol'].decode('utf-8')

print (template % info)
