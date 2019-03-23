# sysconfig_get_scheme_names.py

import sysconfig

for name in sysconfig.get_scheme_names():
    print(name)
