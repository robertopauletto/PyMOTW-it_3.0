# grp_getgrgid_process.py

import grp
import os

gid = os.getgid()
group_info = grp.getgrgid(gid)
print('Attualmente in esecuzione con GID={} nome={}'.format(
    gid, group_info.gr_name))
