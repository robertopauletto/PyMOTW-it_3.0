# filecmp_dircmp_report.py

import filecmp

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2')
dc.report()
