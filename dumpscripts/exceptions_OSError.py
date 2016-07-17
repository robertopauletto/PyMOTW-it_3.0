#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

for i in range(10):
    print i, os.ttyname(i)
