# urllib_parse_urlsplit.py

from urllib.parse import urlsplit

url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlsplit(url)
print(parsed)
print('schema      :', parsed.scheme)
print('loc. di rete:', parsed.netloc)
print('percorso    :', parsed.path)
print('query       :', parsed.query)
print('frammento   :', parsed.fragment)
print('nome utene  :', parsed.username)
print('password    :', parsed.password)
print('nome host   :', parsed.hostname)
print('porta       :', parsed.port)
