# os_process_user_example.py

import os

TEST_GID = 1000
TEST_UID = 1000


def show_user_info():
    print('Utente (reale/effettivo)  : {} / {}'.format(
        os.getuid(), os.geteuid()))
    print('Gruppo (reale/effettivo) : {} / {}'.format(
        os.getgid(), os.getegid()))
    print('Gruppi reali   :', os.getgroups())


print('PRIMA DELLA MDOIFICA:')
show_user_info()
print()

try:
    os.setegid(TEST_GID)
except OSError:
    print('ERRORE: Non è stato possibile cambiare il gruupo effettivo. '
          'Rieseguire come root.')
else:
    print('MODIFICA Gruppo:')
    show_user_info()
    print()

try:
    os.seteuid(TEST_UID)
except OSError:
    print('ERRORE: Non è stato possibile cambiare l\'utente effettivo. '
          'Rieseguire come root.')
else:
    print('MODIFICA UTENTE:')
    show_user_info()
    print()
