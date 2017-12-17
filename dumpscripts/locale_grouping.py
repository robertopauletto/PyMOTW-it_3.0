# locale_grouping.py

import locale

sample_locales = [
    ('USA', 'en_US'),
    ('Francia', 'fr_FR'),
    ('Spagna', 'es_ES'),
    ('Portogallo', 'pt_PT'),
    ('Polonia', 'pl_PL'),
]

print('{:>14} {:>10} {:>15}'.format(
    'Localizzazione', 'Intero', 'Virgola mobile')
)
for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)

    print('{:>14}'.format(name), end=' ')
    print(locale.format('%10d', 123456, grouping=True), end=' ')
    print(locale.format('%15.2f', 123456.78, grouping=True))
