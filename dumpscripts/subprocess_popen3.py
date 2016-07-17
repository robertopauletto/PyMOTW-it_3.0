#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

print '\npopen3:'
proc = subprocess.Popen('cat -; echo ";to stderr" 1>&2',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        )
stdout_value, stderr_value = proc.communicate('attraverso stdin a stdout')
print '\tpassa attraverso:', repr(stdout_value)
print '\tstderr:', repr(stderr_value)
