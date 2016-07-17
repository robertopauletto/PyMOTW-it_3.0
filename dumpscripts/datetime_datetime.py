# datetime_datetime.py

import datetime

print('Oggi      ,', datetime.datetime.today())
print('UTC adesso,', datetime.datetime.utcnow())
print

FIELDS = [
    ('year', 'anno'),
    ('month', 'mese'),
    ('day', 'giorno'),
    ('hour', 'ora'),
    ('minute', 'minuto'),
    ('second', 'secondi'),
    ('microsecond', 'microsecondi')
]

d = datetime.datetime.now()
for attr, descr in FIELDS:
    print('{:15}, {}'.format(descr, getattr(d, attr)))
