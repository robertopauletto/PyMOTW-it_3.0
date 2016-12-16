# pwd_getpwnam.py

import pwd
import sys

username = sys.argv[1]
user_info = pwd.getpwnam(username)

print('Nome Utente:', user_info.pw_name)
print('Password   :', user_info.pw_passwd)
print('Commento   :', user_info.pw_gecos)
print('UID/GID    :', user_info.pw_uid, '/', user_info.pw_gid)
print('Dir. Home  :', user_info.pw_dir)
print('Shell      :', user_info.pw_shell)
