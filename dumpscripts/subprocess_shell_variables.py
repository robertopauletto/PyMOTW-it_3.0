#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import subprocess

# Comando con espansione della shell 
subprocess.call('ls -1 $HOME', shell=True)
