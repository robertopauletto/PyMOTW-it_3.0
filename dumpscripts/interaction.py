#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

print 'Una riga alla volta:'
proc = subprocess.Popen('python repeater.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
for i in range(10):
    proc.stdin.write('%d\n' % i)
    output = proc.stdout.readline()
    print output.rstrip()
remainder = proc.communicate()[0]
print remainder

print
print "Tutto l'output in una volta:"
proc = subprocess.Popen('python repeater.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
for i in range(10):
    proc.stdin.write('%d\n' % i)

output = proc.communicate()[0]
print output
