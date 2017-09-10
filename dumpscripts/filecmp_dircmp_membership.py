# filecmp_dircmp_membership.py

import filecmp
import pprint

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2')
print('Comuni  :')
pprint.pprint(dc.common)

print('\nSinistra:')
pprint.pprint(dc.left_only)

print('\nDestra  :')
pprint.pprint(dc.right_only)
