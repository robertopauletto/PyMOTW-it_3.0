#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# textwrap_fill.py

import textwrap
from textwrap_example import sample_text

print('Nessuna deindentazione:\n')
print(textwrap.fill(sample_text, width=50))

