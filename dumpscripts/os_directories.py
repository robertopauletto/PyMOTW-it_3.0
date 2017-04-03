# os_directories.py

import os

dir_name = 'os_directory_esempio'

print('Creazione', dir_name)
os.makedirs(dir_name)

file_name = os.path.join(dir_name, 'esempio.txt')
print('Creazione', file_name)
with open(file_name, 'wt') as f:
    f.write('file di esempio')

print('Pulizia')
os.unlink(file_name)
os.rmdir(dir_name)
