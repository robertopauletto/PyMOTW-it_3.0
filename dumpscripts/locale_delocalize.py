# locale_delocalize.py

import locale

sample_locales = [
    ('USA', 'en_US'),
    ('Francia', 'fr_FR'),
    ('Spagna', 'es_ES'),
    ('Portogallo', 'pt_PT'),
    ('Polonia', 'pl_PL'),
]

for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)
    localized = locale.format('%0.2f', 123456.78, grouping=True)
    delocalized = locale.delocalize(localized)
    print('{:>10}: {:>10}  {:>10}'.format(
        name,
        localized,
        delocalized,
    ))
