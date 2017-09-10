# filecmp_dircmp_common.py

import filecmp
import pprint

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2')
print('Comuni:')
pprint.pprint(dc.common)

print('\nDirectory:')
pprint.pprint(dc.common_dirs)

print('\nFile:')
pprint.pprint(dc.common_files)

print('\nFunny:')
pprint.pprint(dc.common_funny)

