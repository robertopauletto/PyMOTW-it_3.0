# time_strptime.py

import time


def show_struct(s):
    print('  tm_year (anno)            :', s.tm_year)
    print('  tm_mon  (mese)            :', s.tm_mon)
    print('  tm_mday (giorno del mese) :', s.tm_mday)
    print('  tm_hour (ora)             :', s.tm_hour)
    print('  tm_min  (minuti)          :', s.tm_min)
    print('  tm_sec  (secondi)         :', s.tm_sec)
    print('  tm_wday (giorno settimana):', s.tm_wday)
    print('  tm_yday (giorno nell\'anno):', s.tm_yday)
    print('  tm_isdst (flag ora legale):', s.tm_isdst)

now = time.ctime()
print('Adesso:', now)

parsed = time.strptime(now)
print('\nElaborato:')
show_struct(parsed)

print('\nFormattato:',
      time.strftime("%a %b %d %H:%M:%S %Y", parsed))
