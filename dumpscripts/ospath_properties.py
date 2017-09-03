# ospath_properties.py

import os.path
import time

print('File           :', __file__)
print('Ultimo accesso :', time.ctime(os.path.getatime(__file__)))
print('Ultima modifica:', time.ctime(os.path.getmtime(__file__)))
print('Creazione      :', time.ctime(os.path.getctime(__file__)))
print('Dimensione     :', os.path.getsize(__file__))
