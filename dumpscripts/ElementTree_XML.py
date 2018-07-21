# ElementTree_XML.py

from xml.etree.ElementTree import XML

def show_node(node):
  print/
  if node.text is not None and node.text.strip():
      print('  text: "%s"' % node.text)
  if node.tail is not None and node.tail.strip():
      print('  tail: "%s"' % node.tail)
  for name, value in sorted(node.attrib.items()):
      print('  %-4s = "%s"' % (name, value))
  for child in node:
    show_node(child)


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

for elem in parsed:
  show_node(elem)
