# datetime_date_math.py

import datetime

today = datetime.date.today()
print('Oggi     :', today)

one_day = datetime.timedelta(days=1)
print('Un giorno:', one_day)

yesterday = today - one_day
print('Ieri     :', yesterday)

tomorrow = today + one_day
print('Domani   :', tomorrow)

print('domani - ieri:', tomorrow - yesterday)
print('ieri - domani:', yesterday - tomorrow)
