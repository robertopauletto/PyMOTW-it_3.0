# sysconfig_get_config_vars_by_name.py

import sysconfig

bases = sysconfig.get_config_vars('base', 'platbase', 'userbase')
print('Directory base:')
for b in bases:
    print('  ', b)
