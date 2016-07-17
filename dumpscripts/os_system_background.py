#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import time

print 'Chiamata...'
os.system('date; (sleep 3; date) &')

print 'In pausa...'
time.sleep(5)
