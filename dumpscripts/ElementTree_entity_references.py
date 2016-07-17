#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from xml.etree import ElementTree

with open('data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

node = tree.find('entity_expansion')
print node.tag
print "  nell'attributo:", node.attrib['attribute']
print '  nel testo     :', node.text
