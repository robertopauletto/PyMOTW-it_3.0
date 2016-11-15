# re_look_behind.py

import re

twitter = re.compile(
    '''
    # Un handle di Twitter: @username
    (?<=@)
    ([\w\d_]+)       # username
    ''',
    re.VERBOSE)

text = '''Questo testo include due Twitter handle.
Uno per @ThePSF, ed uno per l'autore, @doughellmann.
'''

print(text)
for match in twitter.findall(text):
    print('Handle:', match)

