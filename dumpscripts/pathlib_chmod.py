# pathlib_chmod.py

import os
import pathlib
import stat

# Crea un nuovo file di testo
f = pathlib.Path('pathlib_chmod_esempio.txt')
if f.exists():
    f.unlink()
f.write_text('contenuto')

# Determa che permessio sono già impostati usando stat.
existing_permissions = stat.S_IMODE(f.stat().st_mode)
print('Prima: {:o}'.format(existing_permissions))

# Decide in che modo alternarli.
if not (existing_permissions & os.X_OK):
    print('Aggiunto permesso di esecuzione')
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Rimosso permesso di esecuzione')
    # usa xor per rimuovere il permesso di esecuzione utente
    new_permissions = existing_permissions ^ stat.S_IXUSR

# Esegue la modifica e mostra il nuovo valore.
f.chmod(new_permissions)
after_permissions = stat.S_IMODE(f.stat().st_mode)
print('Dopo: {:o}'.format(after_permissions))
