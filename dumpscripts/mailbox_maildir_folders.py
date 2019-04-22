# mailbox_maildir_folders.py

import mailbox
import os


def show_maildir(name):
    os.system('find {} -print'.format(name))


mbox = mailbox.Maildir('Esempio')
print('Prima:', mbox.list_folders())
show_maildir('Esempio')

print('\n{:#^30}\n'.format(''))

mbox.add_folder('sottocartella')
print('creata sottocartella:', mbox.list_folders())
show_maildir('Esempio')

subfolder = mbox.get_folder('sottocartella')
print('sottocartella contiene:', subfolder.list_folders())

print('\n{:#^30}\n'.format(''))

subfolder.add_folder('secondo_livello')
print('creato secondo_livello:', subfolder.list_folders())
show_maildir('Esempio')

print('\n{:#^30}\n'.format(''))

subfolder.remove_folder('secondo_livello')
print('secondo_livello rimosso:', subfolder.list_folders())
show_maildir('Esempio')
