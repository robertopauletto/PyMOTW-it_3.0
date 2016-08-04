# glob_subdir.py

import glob

print('Nominata esplicitamente:')
for name in sorted(glob.glob('dir/subdir/*')):
    print('\t', name)

print('nominata con caratteri jolly:')
for name in sorted(glob.glob('dir/*/*')):
    print('\t', name)
