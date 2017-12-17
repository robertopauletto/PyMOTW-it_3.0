# locale_atof.py
import locale

sample_data = [
    ('USA', 'en_US', '1,234.56'),
    ('Francia', 'fr_FR', '1234,56'),
    ('Spagna', 'es_ES', '1234,56'),
    ('Portogallo', 'pt_PT', '1234.56'),
    ('Polonia', 'pl_PL', '1 234,56'),
]

for name, loc, a in sample_data:
    locale.setlocale(locale.LC_ALL, loc)
    print('{:>10}: {:>9} => {:f}'.format(
        name,
        a,
        locale.atof(a),
    ))
