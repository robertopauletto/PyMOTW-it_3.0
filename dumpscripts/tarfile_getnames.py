#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import tarfile

t = tarfile.open('esempio.tar', 'r')
print t.getnames()
 