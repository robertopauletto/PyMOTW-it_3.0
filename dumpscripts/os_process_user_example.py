#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

TEST_GID=501
TEST_UID=527

def show_user_info():
    print 'Utente effettivo :', os.geteuid()
    print 'Gruppo effettivo :', os.getegid()
    print 'Utente reale     :', os.getuid(), os.getlogin()
    print 'Gruppo reale     :', os.getgid()
    print 'Gruppi reali     :', os.getgroups()
    return

print 'PRIMA DELLA MODIFICA:'
show_user_info()
print

try:
    os.setegid(TEST_GID)
except OSError:
    print 'ERRORE: Impossibile cambiare il gruppo effettivo. Rieseguire come root.'
else:
    print 'GRUPPO MODIFICATO:'
    show_user_info()
    print

try:
    os.seteuid(TEST_UID)
except OSError:
    print "ERRORE: Impossibile cambiare l'utente effettivo. Rieseguire come root."
else:
    print 'MODIFICA UTENTE:'
    show_user_info()
    print
