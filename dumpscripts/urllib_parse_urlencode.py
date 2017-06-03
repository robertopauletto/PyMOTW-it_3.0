# urllib_parse_urlencode.py

from urllib.parse import urlencode

query_args = {
    'q': 'query string',
    'foo': 'bar',
}
encoded_args = urlencode(query_args)
print('Codificati:', encoded_args)
