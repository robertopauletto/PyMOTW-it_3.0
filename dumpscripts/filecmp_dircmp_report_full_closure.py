# filecmp_dircmp_report_full_closure.py

import filecmp

dc = filecmp.dircmp('esempio/dir1', 'esempio/dir2')
dc.report_full_closure()
