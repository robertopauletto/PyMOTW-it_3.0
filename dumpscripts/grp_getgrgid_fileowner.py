# grp_getgrgid_fileowner.py

import grp
import os

filename = 'grp_getgrgid_fileowner.py'
stat_info = os.stat(filename)
owner = grp.getgrgid(stat_info.st_gid).gr_name

print('Il proprietario di {} è {} ({})'.format(
    filename, owner, stat_info.st_gid))
