# pwd_getpwuid_process.py

import pwd
import os

uid = os.getuid()
user_info = pwd.getpwuid(uid)
print('Attualmente in esecuzione con UID={} nome utente={}'.format(
    uid, user_info.pw_name))
