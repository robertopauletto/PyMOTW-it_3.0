#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

pid = os.fork()

if pid:
    print 'Id del processo:', pid
else:
    print 'Sono il figlio'
