#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import zipfile

zf = zipfile.ZipFile('esempio.zip', 'r')
print zf.namelist()
