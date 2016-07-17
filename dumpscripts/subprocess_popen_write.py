#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

print '\nscrittura:'
proc = subprocess.Popen(['cat', '-'],
                        shell=True,
                        stdin=subprocess.PIPE,
                        )
proc.communicate('\tstdin: to stdin\n')
