#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from codecs_invertcaps_charmap import encoding_map

text = u'pi: π'

for error in [ 'ignore', 'replace', 'strict' ]:
    try:
        encoded = codecs.charmap_encode(text, error, encoding_map)
    except UnicodeEncodeError, err:
        encoded = str(err)
    print '{:7}: {}'.format(error, encoded)