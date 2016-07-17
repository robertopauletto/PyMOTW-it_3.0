#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import getpass
import sys

p = getpass.getpass(stream=sys.stderr)
print 'Hai digitato:', p