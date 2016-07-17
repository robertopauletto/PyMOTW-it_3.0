#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

print '\npopen4:'
proc = subprocess.Popen('cat -; echo ";to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        )
stdout_value, stderr_value = proc.communicate('attraverso stdin a stdout\n')
print '\tOutput combinato:', repr(stdout_value)
