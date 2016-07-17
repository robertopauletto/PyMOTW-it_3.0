import filecmp

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2')
print 'Comuni     :', dc.common
print 'Directory  :', dc.common_dirs
print 'File       :', dc.common_files
print 'Funny      :', dc.common_funny
