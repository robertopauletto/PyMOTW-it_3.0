# grp_getgrnam.py

import grp

name = 'adm'
info = grp.getgrnam(name)
print('Nome    :', info.gr_name)
print('GID     :', info.gr_gid)
print('Password:', info.gr_passwd)
print('Membri  :', ', '.join(info.gr_mem))
