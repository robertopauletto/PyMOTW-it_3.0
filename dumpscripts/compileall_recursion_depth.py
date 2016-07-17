#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import compileall
import re

compileall.compile_dir('examples', 
    maxlevels=0, 
    rx=re.compile(r'/\.svn'))