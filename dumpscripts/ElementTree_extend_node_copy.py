# ElementTree_extend_node_copy.py

from xml.etree.ElementTree import (Element, SubElement, tostring, XML)
from ElementTree_pretty import prettify

top = Element('top')

parent_a = SubElement(top, 'genitore', id='A')
parent_b = SubElement(top, 'genitore', id='B')

# Crea figlio
children = XML(
    '<root><figlio num="0" /><figlio num="1" />'
    '<figlio num="2" /></root>'
)

# Imposta l'id all'id dell'oggetto Python del nodo
# per facilitare l'individuazione dei duplicati.
for c in children:
    c.set('id', str(id(c)))

# Aggiunge al primo genitore
parent_a.extend(children)

print('A:')
print(prettify(top))
print()

# Copia nodi al secondo genitore
parent_b.extend(children)

print('B:')
print(prettify(top))
print()
