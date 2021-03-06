# os_stat_chmod.py

import os
import stat

filename = 'os_stat_chmod_example.txt'
if os.path.exists(filename):
    os.unlink(filename)
with open(filename, 'wt') as f:
    f.write('contenuto')

# Determina quali permessi sono già impostati usando  stat
existing_permissions = stat.S_IMODE(os.stat(filename).st_mode)

if not os.access(filename, os.X_OK):
    print('Aggiunta dei permessi di esecuzione')
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Rimozione dei permessi di esecuzione')
    # usa xor per rimuovere il permesso di esecuzione per l'utente
    new_permissions = existing_permissions ^ stat.S_IXUSR

os.chmod(filename, new_permissions)
