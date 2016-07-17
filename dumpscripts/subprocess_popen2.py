#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

print '\npopen2:'

proc = subprocess.Popen(['cat', '-'],
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
stdout_value = proc.communicate('attraverso stdin a stdout')[0]
print '\tpassa attraverso:', repr(stdout_value)
