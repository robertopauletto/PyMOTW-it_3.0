# http_cookies_js_output.py

from http import cookies
import textwrap


c = cookies.SimpleCookie()
c['ilmiocookie'] = 'valore del cookie'
c['altro_cookie'] = 'secondo valore'
js_text = c.js_output()
print(textwrap.dedent(js_text).lstrip())
