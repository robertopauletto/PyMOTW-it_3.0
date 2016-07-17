#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

print 'Partenza:', os.getcwd()
print os.listdir(os.curdir)

print 'Risalita di uno:', os.pardir
os.chdir(os.pardir)

print 'Dopo lo spostamento:', os.getcwd()
print os.listdir(os.curdir)