# locale_env.py

import locale
import os
import pprint

# Impostazioni predefinite in base all'ambiente dell'utente.
locale.setlocale(locale.LC_ALL, '')

print('Impostazioni di ambiente:')
for env_name in ['LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE']:
    print('  {} = {}'.format(
        env_name, os.environ.get(env_name, ''))
    )

# What is the locale?
print('\nLocalizzazione da ambiente:', locale.getlocale())

template = """
Formattazione numerica:

  Separatore decimale      : "{decimal_point}"
  Raggruppamento posizioni : {grouping}
  Separatore migliaia      : "{thousands_sep}"

Formattazione valuta:

  Simbolo internazionale valuta        : "{int_curr_symbol!r}"
  Simbolo valuta locale                : {currency_symbol!r}
  Simbolo che precede valore positivo  : {p_cs_precedes}
  Simbolo che precede valore negativo  : {n_cs_precedes}
  Separatore decimale                  : "{mon_decimal_point}"
  Cifre in valori frazione             : {frac_digits}
  Cifre in valori frazione,
                   internazionale      : {int_frac_digits}
  Raggruppamento posizioni             : {mon_grouping}
  Separatore migliaia                  : "{mon_thousands_sep}"
  Segno positivo                       : "{positive_sign}"
  Posizione segno positivo             : {p_sign_posn}
  Segno negativo                       : "{negative_sign}"
  Posizione segno negativo             : {n_sign_posn}

"""

sign_positions = {
    0: 'Racchiuso tra parentesei',
    1: 'Prima di valore e simbolo',
    2: 'Dopo valore e simbolo',
    3: 'Prima del valore',
    4: 'Dopo il valore',
    locale.CHAR_MAX: 'Non specificato',
}

info = {}
info.update(locale.localeconv())
info['p_sign_posn'] = sign_positions[info['p_sign_posn']]
info['n_sign_posn'] = sign_positions[info['n_sign_posn']]

print(template.format(**info))
