# getpass_prompt.py

import getpass

p = getpass.getpass(prompt='Quale è il tuo colore preferito? ')
if p.lower() == 'blu':
    print('Bene. Puoi andare.')
else:
    print('Auuuuugh!')
