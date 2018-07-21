# ElementTree_extend.py

from xml.etree.ElementTree import Element, tostring
from ElementTree_pretty import prettify

top = Element('top')

children = [
    Element('figlio', num=str(i))
    for i in range(3)
]

top.extend(children)

print(prettify(top))
