# urllib_parse_urldefrag.py

from urllib.parse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print('originale:', original)
d = urldefrag(original)
print('url      :', d.url)
print('frammento:', d.fragment)
