#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from xml.etree import ElementTree

with open('data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

for path in [ './child', './child_with_tail' ]:
    node = tree.find(path)
    print node.tag
    print '  testo del nodo figlio:', node.text
    print '  e testo di coda      :', node.tail
