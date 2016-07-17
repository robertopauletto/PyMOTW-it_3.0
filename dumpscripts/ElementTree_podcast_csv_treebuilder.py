#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import csv
from xml.etree.ElementTree import XMLTreeBuilder
import sys

class PodcastListToCSV(object):

    def __init__(self, outputFile):
        self.writer = csv.writer(outputFile, quoting=csv.QUOTE_NONNUMERIC)
        self.group_name = ''
        return

    def start(self, tag, attrib):
        if tag != 'outline':
            # Ignora qualsiasi al di fuori di outline
            return
        if not attrib.get('xmlUrl'):
            # Ricorda il gruppo corrente
            self.group_name = attrib['text']
        else:
            # Scrive una voce di podcast
            self.writer.writerow( (self.group_name, attrib['text'],
                                   attrib['xmlUrl'],
                                   attrib.get('htmlUrl', ''),
                                   )
                                  )

    def end(self, tag):
        # Ignora i tag di chiusura
        pass
    def data(self, data):
        # Ignora i dati all'interno dei nodi
        pass
    def close(self):
        # Nulla di speciale da fare qui
        return


target = PodcastListToCSV(sys.stdout)
parser = XMLTreeBuilder(target=target)
with open('podcasts.opml', 'rt') as f:
    for line in f:
        parser.feed(line)
parser.close()

