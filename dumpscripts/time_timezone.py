# time_timezone.py

import time
import os


def show_zone_info():
    print('\tTZ    :', os.environ.get('TZ', '(non impostata)'))
    print('\ttzname:', time.tzname)
    print('\tZona  : {} ({})'.format(time.timezone, (time.timezone / 3600)))
    print('\tDST   :', time.daylight)
    print('\tOra   :', time.ctime())
    print

print('Predefinito :')
show_zone_info()

ZONES = [
    'GMT',
    'Europe/Moscow',
]

for zone in ZONES:
    os.environ['TZ'] = zone
    time.tzset()
    print(zone, ':')
    show_zone_info()
