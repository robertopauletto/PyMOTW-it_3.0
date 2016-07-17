#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

print 'popen3:'
pipe_stdin, pipe_stdout, pipe_stderr = os.popen3('cat -; echo ";allo stderr" 1>&2')
try:
    pipe_stdin.write('attraverso stdin a stdout')
finally:
    pipe_stdin.close()
try:
    stdout_value = pipe_stdout.read()
finally:
    pipe_stdout.close()
print '\tpassa attraverso:', repr(stdout_value)
try:
    stderr_value = pipe_stderr.read()
finally:
    pipe_stderr.close()
print '\tstderr:', repr(stderr_value)


