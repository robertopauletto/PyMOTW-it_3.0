# sys_flags.py

import sys

if sys.flags.bytes_warning:
    print('Avvertimento su errori byte/stringa')
if sys.flags.debug:
    print('Debug')
if sys.flags.inspect:
    print('Entra in modalità interattiva dopo l\'esecuzione')
if sys.flags.optimize:
    print('Ottimizza byte-code')
if sys.flags.dont_write_bytecode:
    print('Non scrivere file byte-code')
if sys.flags.no_site:
    print('Nom importare "site"')
if sys.flags.ignore_environment:
    print('Ignora l\'ambiente')
if sys.flags.verbose:
    print('Modalità verbosa')
