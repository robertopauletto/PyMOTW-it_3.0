import filecmp

filecmp.dircmp('esempio/dir1', 'esempio/dir2').report_full_closure()
