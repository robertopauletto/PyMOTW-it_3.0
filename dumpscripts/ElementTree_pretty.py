# ElementTree_pretty.py

from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Ritorna una stringa XML pretty-print per Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")
