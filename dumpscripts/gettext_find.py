# gettext_find.py

import gettext

catalogs = gettext.find('example', 'locale', all=True)
print('Cataloghi:', catalogs)
