# filecmp_dircmp_list_filter.py

import filecmp
import pprint

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2',
                    ignore=['file_comune'])

print('Sinistra:')
pprint.pprint(dc.left_list)

print('\nDestra  :')
pprint.pprint(dc.right_list)
