# http_cookies_setheaders.py

from http import cookies


c = cookies.SimpleCookie()
c['ilmiocookie'] = 'valore_del_cookie'
print(c)
