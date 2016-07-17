import filecmp

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2')
print 'Uguali    :', dc.same_files
print 'Diversi   :', dc.diff_files
print 'Funny     :', dc.funny_files
