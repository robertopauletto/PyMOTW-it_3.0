# sysconfig_get_config_var.py

import sysconfig

print('Directory base utente:',
      sysconfig.get_config_var('userbase'))
print('Variable sconosciuta :',
      sysconfig.get_config_var('NoSuchVariable'))
