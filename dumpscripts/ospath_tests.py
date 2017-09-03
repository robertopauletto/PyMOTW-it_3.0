# ospath_tests.py
import os.path

FILENAMES = [
    __file__,
    os.path.dirname(__file__),
    '/',
    './collegamento_interrotto',
]

for file in FILENAMES:
    print('File                             : {!r}'.format(file))
    print('Assoluto                         :', os.path.isabs(file))
    print("E' un File?                      :", os.path.isfile(file))
    print("E' una directory                 :", os.path.isdir(file))
    print("E' un collegamento simbolico?    :", os.path.islink(file))
    print('Punto di montaggio?              :', os.path.ismount(file))
    print('Esiste?                          :', os.path.exists(file))
    print('Esiste il collegamento simbolico?:', os.path.lexists(file))
    print()
