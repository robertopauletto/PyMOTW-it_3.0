# urllib_parse_geturl.py

from urllib.parse import urlparse

original = 'http://netloc/path;param?query=arg#frag'
print('ORIGINALE  :', original)
parsed = urlparse(original)
print('ASSEMBLATO :', parsed.geturl())
