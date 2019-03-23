# resource_getrusage.py

import resource


RESOURCES = [
    ('ru_utime', 'Tempo utente'),
    ('ru_stime', 'Tempo sistema'),
    ('ru_maxrss', 'Dimensione massima memoria\nfisica'
                  ' mappata dal processo     '),
    ('ru_ixrss', 'Dimensione memoria condivisa '),
    ('ru_idrss', 'Dimensione memoria non condivisa'),
    ('ru_isrss', 'Dimensione dello stack'),
    ('ru_inblock', 'Blocchi input'),
    ('ru_oublock', 'Blocchi output'),
]

usage = resource.getrusage(resource.RUSAGE_SELF)

for name, desc in RESOURCES:
    print('{:<32} ({:<10}) = {}'.format(
        desc, name, getattr(usage, name)))
