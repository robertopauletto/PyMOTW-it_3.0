# resource_getrlimit.py

import resource


LIMITS = [
    ('RLIMIT_CORE', 'Dimensione file core'),
    ('RLIMIT_CPU', 'Tempo CPU'),
    ('RLIMIT_FSIZE', 'Dimensione file'),
    ('RLIMIT_DATA', 'Dimensione heap '),
    ('RLIMIT_STACK', 'Dimensione stack '),
    ('RLIMIT_RSS', 'Dimensione massima memoria\n'
                   'fisica mappata del processo     '),
    ('RLIMIT_NPROC', 'Numero di processi'),
    ('RLIMIT_NOFILE', 'Numero di file aperti'),
    ('RLIMIT_MEMLOCK', 'Indirizzo di memoria bloccabile'),
]

print('Limit delle risorse (soft/hard):')
for name, desc in LIMITS:
    limit_num = getattr(resource, name)
    soft, hard = resource.getrlimit(limit_num)
    print('{:<32} {}/{}'.format(desc, soft, hard))
