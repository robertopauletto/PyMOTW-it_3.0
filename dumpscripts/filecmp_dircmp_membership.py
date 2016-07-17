import filecmp

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2')
print 'Comuni:', dc.common
print 'Left  :', dc.left_only
print 'Right :', dc.right_only
