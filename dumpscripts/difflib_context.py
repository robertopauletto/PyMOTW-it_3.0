#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import difflib
from difflib_data import *

diff = difflib.context_diff(text1_lines, text2_lines, lineterm='')
print '\n'.join(list(diff))