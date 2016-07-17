#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

print tree
