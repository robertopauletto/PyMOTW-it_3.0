# os_symlinks.py

import os

link_name = '/tmp/' + os.path.basename(__file__)

print('Creaione del collegamento {} -> {}'.format(link_name, __file__))
os.symlink(__file__, link_name)

stat_info = os.lstat(link_name)
print('Permessi:', oct(stat_info.st_mode))

print('Punta a:', os.readlink(link_name))

# Pulizia
os.unlink(link_name)
