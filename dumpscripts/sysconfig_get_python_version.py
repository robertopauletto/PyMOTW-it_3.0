# sysconfig_get_python_version.py

import sysconfig
import sys

print('sysconfig.get_python_version():',
      sysconfig.get_python_version())
print('\nsys.version_info:')
print('  maggiore        :', sys.version_info.major)
print('  minore          :', sys.version_info.minor)
print('  micro           :', sys.version_info.micro)
print('  livello rilascio:', sys.version_info.releaselevel)
print('  seriale         :', sys.version_info.serial)
