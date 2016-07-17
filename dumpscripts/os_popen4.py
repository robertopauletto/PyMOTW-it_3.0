#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

print 'popen4:'
pipe_stdin, pipe_stdout_and_stderr = os.popen4('cat -; echo ";allo stderr" 1>&2')
try:
    pipe_stdin.write('attraverso stdin allo stdout')
finally:
    pipe_stdin.close()
try:
    stdout_value = pipe_stdout_and_stderr.read()
finally:
    pipe_stdout_and_stderr.close()
print '\toutput combinato:', repr(stdout_value)


