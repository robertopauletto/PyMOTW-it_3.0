#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

os.spawnlp(os.P_WAIT, 'ls', 'ls', '-l', '/tmp/')
