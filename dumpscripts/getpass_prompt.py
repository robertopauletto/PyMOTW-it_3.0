# getpass_prompt.py

import getpass

p = getpass.getpass(prompt='Quale è il colore preferito? ')
if p.lower() == 'blu':
    print('Bene. Puoi andare.')
else:
    print('Auuuuugh!')
