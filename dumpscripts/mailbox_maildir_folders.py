#!/usr/bin/env python
# -*- coding: UTF-8*-

import mailbox
import os

def show_maildir(name):
    os.system('find %s -print' % name)

mbox = mailbox.Maildir('Example')
print 'Prima:', mbox.list_folders()
show_maildir('Example')

print
print '#' * 30
print

mbox.add_folder('sottocartella')
print 'creata sottocartella:', mbox.list_folders()
show_maildir('Example')

subfolder = mbox.get_folder('sottocartella')
print 'sottocartella contiene:', subfolder.list_folders()

print
print '#' * 30
print

subfolder.add_folder('secondo_livello')
print 'creato secondo_livello:', subfolder.list_folders()
show_maildir('Example')

print
print '#' * 30
print

subfolder.remove_folder('secondo_livello')
print 'secondo_livello rimosso:', subfolder.list_folders()
show_maildir('Example')
