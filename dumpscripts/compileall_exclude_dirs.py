#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import compileall
import re

compileall.compile_dir('examples', 
    rx=re.compile(r'/\.svn'))