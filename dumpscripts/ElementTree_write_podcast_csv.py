#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv
from xml.etree.ElementTree import iterparse
import sys

#f = open('podcasts.csv', 'w')

writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
#writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

group_name = ''

for (event, node) in iterparse('podcasts.opml', events=['start']):
    if node.tag != 'outline':
        # Ignora qualsiasi parte al di fuori di outline
        continue
    if not node.attrib.get('xmlUrl'):
        # Ricorda il gruppo corrente
        group_name = node.attrib['text']
    else:
        # Scrive una voce di podcast
        writer.writerow( (group_name, node.attrib['text'],
                          node.attrib['xmlUrl'],
                          node.attrib.get('htmlUrl', ''),
                          )
                         )

