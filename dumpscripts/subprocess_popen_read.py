#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

print '\nlettura:'
proc = subprocess.Popen(['echo', '"to stdout"'], 
                        shell=True, 
                        stdout=subprocess.PIPE,
                        )
stdout_value = proc.communicate()[0]
print '\tstdout:', repr(stdout_value)
