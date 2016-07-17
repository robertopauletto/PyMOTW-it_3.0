#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from xml.etree.ElementTree import XMLID
tree, id_map = XMLID('''
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

for key, value in sorted(id_map.items()):
    print '%s = %s' % (key, value)
    
