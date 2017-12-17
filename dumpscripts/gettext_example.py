# gettext_example.py

import gettext

# Set up message catalog access
t = gettext.translation(
    'example_domain', 'locale',
    fallback=True,
)
_ = t.gettext

print(_("Questo messaggio si trova nello script."))
