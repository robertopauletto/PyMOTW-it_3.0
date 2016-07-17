import datetime

d = datetime.datetime.today()


f = (
    '%a',
    '%A',
    '%w',
    '%d',
    '%b',
    '%B',
    '%m',
    '%y',
    '%Y',
    '%H',
    '%I',
    '%p',
    '%M',
    '%S',
    '%f',
    '%z',
    '%Z',
    '%j',
    '%W',
    '%c',
    '%x',
    '%X',
    '%%'
)
for i in f:
    print('{} {i}'.format(i, d))

