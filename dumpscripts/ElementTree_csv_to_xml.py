#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import datetime
from ElementTree_pretty import prettify

generated_on = str(datetime.datetime.now())

# Configura un attributo con set()
root = Element('opml')
root.set('version', '1.0')

root.append(Comment('Generato da ElementTree_csv_to_xml.py per PyMOTW-it'))

head = SubElement(root, 'head')
title = SubElement(head, 'title')
title.text = 'My Podcasts'
dc = SubElement(head, 'dateCreated')
dc.text = generated_on
dm = SubElement(head, 'dateModified')
dm.text = generated_on

body = SubElement(root, 'body')

with open('podcasts.csv', 'rt') as f:
    current_group = None
    reader = csv.reader(f)
    for row in reader:
        group_name, podcast_name, xml_url, html_url = row
        if not current_group or group_name != current_group.text:
            # Inizia un nuovo gruppo
            current_group = SubElement(body, 'outline', {'text':group_name})
        # Aggiunge questo podcast al gruppo
        # impostandone gli attibuti tutti in 
        # una volta.
        podcast = SubElement(current_group, 'outline',
                             {'text':podcast_name,
                              'xmlUrl':xml_url,
                              'htmlUrl':html_url,
                              })

print prettify(root)
