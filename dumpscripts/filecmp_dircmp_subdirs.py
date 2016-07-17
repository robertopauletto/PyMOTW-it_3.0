import filecmp

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2')
print 'Sottodirectory:'
print dc.subdirs
