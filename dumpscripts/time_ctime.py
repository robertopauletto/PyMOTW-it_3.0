# time_ctime.py


import time

print("L'ora è          :", time.ctime())
later = time.time() + 15
print('15 sec. da adesso:', time.ctime(later))
