# http_cookies_coded_value.py

from http import cookies


c = cookies.SimpleCookie()
c['intero'] = 5
c['con_virgolette'] = 'Disse, "Ciao, Mondo!"'

for name in ['intero', 'con_virgolette']:
    print(c[name].key)
    print('  {}'.format(c[name]))
    print('  value={!r}'.format(c[name].value))
    print('  coded_value={!r}'.format(c[name].coded_value))
    print()
