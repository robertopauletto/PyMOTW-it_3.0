# ElementTree_extend_node.py

from xml.etree.ElementTree import Element, SubElement, tostring, XML)
from ElementTree_pretty import prettify

top = Element('top')

parent = SubElement(top, 'genitore')

children = XML(
    '<root><figlio num="0" /><figlio num="1" />'
    '<figlio num="2" /></root>'
)
parent.extend(children)

print(prettify(top))
