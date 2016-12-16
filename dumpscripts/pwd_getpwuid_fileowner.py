# pwd_getpwuid_fileowner.py

import pwd
import os

filename = 'pwd_getpwuid_fileowner.py'
stat_info = os.stat(filename)
owner = pwd.getpwuid(stat_info.st_uid).pw_name

print('Il proprietario di {} è {} ({})'.format(
    filename, owner, stat_info.st_uid))
