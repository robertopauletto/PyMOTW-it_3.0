# datetime_timedelta_math.py

import datetime

one_day = datetime.timedelta(days=1)
print('1 giorno   :', one_day)
print('5 giorni   :', one_day * 5)
print('1.5 giorni :', one_day * 1.5)
print('1/4 giorno :', one_day / 4)

# si assume un ora per il pranzo
work_day = datetime.timedelta(hours=7)
meeting_length = datetime.timedelta(hours=1)
print('riunioni al giorno :', work_day / meeting_length)
