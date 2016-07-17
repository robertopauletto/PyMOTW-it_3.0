#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time

now = time.ctime()
print now
parsed = time.strptime(now)
print parsed
print time.strftime("%a %b %d %H:%M:%S %Y", parsed)
