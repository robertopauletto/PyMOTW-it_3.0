# datetime_time.py

import datetime

t = datetime.time(1, 2, 3)
print(t)
print('ora         :', t.hour)
print('minuto      :', t.minute)
print('secondo     :', t.second)
print('microsecondo:', t.microsecond)
print('zona fuso or:', t.tzinfo)
