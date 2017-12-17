# gettext_example_corrected.py

import gettext

t = gettext.translation(
    'example', 'locale',
    fallback=True,
)
