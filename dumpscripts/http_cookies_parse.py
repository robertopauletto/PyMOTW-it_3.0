# http_cookies_parse.py

from http import cookies


HTTP_COOKIE = '; '.join([
    r'intero=5',
    r'con_virgolette="Disse, \"Ciao, Mondo!\""',
])

print('Dal Costruttore:')
c = cookies.SimpleCookie(HTTP_COOKIE)
print(c)

print()
print('Da load():')
c = cookies.SimpleCookie()
c.load(HTTP_COOKIE)
print(c)
