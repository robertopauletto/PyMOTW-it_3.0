#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

print 'popen, lettura:'
pipe_stdout = os.popen('echo "allo stdout"', 'r')
try:
    stdout_value = pipe_stdout.read()
finally:
    pipe_stdout.close()
print '\tstdout:', repr(stdout_value)

print '\npopen, scrittura:'
pipe_stdin = os.popen('cat -', 'w')
try:
    pipe_stdin.write('\tstdin: allo stdin\n')
finally:
    pipe_stdin.close()
