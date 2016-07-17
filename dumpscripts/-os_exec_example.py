#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

child_pid = os.fork()
if child_pid:
    os.waitpid(child_pid, 0)
else:
    os.execlp('ls', 'ls', '-l', '/tmp/')
