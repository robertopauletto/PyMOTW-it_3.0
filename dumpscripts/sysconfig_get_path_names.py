# sysconfig_get_path_names.py

import sysconfig

for name in sysconfig.get_path_names():
    print(name)
