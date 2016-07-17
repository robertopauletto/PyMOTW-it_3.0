#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import uuid

hostnames = ['www.doughellmann.com', 'blog.doughellmann.com']

for name in hostnames:
    print name
    print '\tMD5   :', uuid.uuid3(uuid.NAMESPACE_DNS, name)
    print '\tSHA-1 :', uuid.uuid5(uuid.NAMESPACE_DNS, name)