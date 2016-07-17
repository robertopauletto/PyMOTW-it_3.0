#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from xml.etree.ElementTree import XML

parsed = XML('''
<root>
  <group>
    <child id="a">Questo è il figlio "a".</child>
    <child id="b">Questo è il figlio "b".</child>
  </group>
  <group>
    <child id="c">Questo è il figlio "c".</child>
  </group>
</root>
''')

print 'parsed =', parsed

for elem in parsed.getiterator():
    print elem.tag
    if elem.text is not None and elem.text.strip():
        print '  text: "%s"' % elem.text
    if elem.tail is not None and elem.tail.strip():
        print '  tail: "%s"' % elem.tail
    for name, value in sorted(elem.attrib.items()):
        print '  %-4s = "%s"' % (name, value)
    print
