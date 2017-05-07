# urllib_parse_urlparseattrs.py

from urllib.parse import urlparse

url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlparse(url)
print('schema      :', parsed.scheme)
print('loc. di rete:', parsed.netloc)
print('percorso    :', parsed.path)
print('parametri   :', parsed.params)
print('query       :', parsed.query)
print('frammento   :', parsed.fragment)
print('nome utene  :', parsed.username)
print('password    :', parsed.password)
print('nome host   :', parsed.hostname)
print('porta       :', parsed.port)
