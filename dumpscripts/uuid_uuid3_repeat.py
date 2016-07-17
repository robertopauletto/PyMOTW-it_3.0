#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import uuid

for i in xrange(3):
    print uuid.uuid3(uuid.NAMESPACE_DNS, 'www.doughellmann.com')