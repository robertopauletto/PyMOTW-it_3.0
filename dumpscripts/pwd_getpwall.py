# pwd_getpwall.py

import pwd
import operator

# Carica tutti i dati degli utenti, ordinati per nome utente
all_user_data = pwd.getpwall()
interesting_users = sorted(
    (u for u in all_user_data
     if not u.pw_name.startswith('_')),
    key=operator.attrgetter('pw_name')
)

# Cerca la lunghezza massima per alcuni campi
username_length = max(len(u.pw_name)
                      for u in interesting_users) + 1
home_length = max(len(u.pw_dir)
                  for u in interesting_users) + 1
uid_length = max(len(str(u.pw_uid))
                 for u in interesting_users) + 1

# Stampa le intestazioni del report
fmt = ' '.join(['{:<{username_length}}',
                '{:>{uid_length}}',
                '{:<{home_length}}',
                '{}'])
print(fmt.format('User',
                 'UID',
                 'Directory Home',
                 'Descrizione',
                 username_length=username_length,
                 uid_length=uid_length,
                 home_length=home_length))
print('-' * username_length,
      '-' * uid_length,
      '-' * home_length,
      '-' * 20)

# Stampa i dati
for u in interesting_users:
    print(fmt.format(u.pw_name,
                     u.pw_uid,
                     u.pw_dir,
                     u.pw_gecos,
                     username_length=username_length,
                     uid_length=uid_length,
                     home_length=home_length))
