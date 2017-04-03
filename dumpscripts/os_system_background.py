# os_system_background.py

import os
import time

print('Chiamata...')
os.system('date; (sleep 3; date) &')

print('In pausa...')
time.sleep(5)
