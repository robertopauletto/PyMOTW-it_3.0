# filecmp_cmp.py

import filecmp

print('file_comune  :', end=' ')
print(filecmp.cmp('esempio/dir1/file_comune',
                  'esempio/dir2/file_comune'),
      end=' ')
print(filecmp.cmp('esempio/dir1/file_comune',
                  'esempio/dir2/file_comune',
                  shallow=False))

print('non_lo_stesso:', end=' ')
print(filecmp.cmp('esempio/dir1/non_lo_stesso',
                  'esempio/dir2/non_lo_stesso'),
      end=' ')
print(filecmp.cmp('esempio/dir1/non_lo_stesso',
                  'esempio/dir2/non_lo_stesso',
                  shallow=False))

print('identici     :', end=' ')
print(filecmp.cmp('esempio/dir1/file_solo_in_dir1',
                  'esempio/dir1/file_solo_in_dir1'),
      end=' ')
print(filecmp.cmp('esempio/dir1/file_solo_in_dir1',
                  'esempio/dir1/file_solo_in_dir1',
                  shallow=False))
