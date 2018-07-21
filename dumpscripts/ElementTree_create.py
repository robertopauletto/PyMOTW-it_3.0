# ElementTree_create.py

from xml.etree.ElementTree import Element, SubElement, Comment, tostring

top = Element('top')

comment = Comment('Generato per PyMOTW-it')
top.append(comment)

child = SubElement(top, 'figlio')
child.text = 'Questo figlio contiene testo.'

child_with_tail = SubElement(top, 'figlio_con_coda')
child_with_tail.text = 'Questo figlio contiene testo normale.'
child_with_tail.tail = 'E testo "in coda".'

child_with_entity_ref = SubElement(top, 'figlio_con_rif_entita')
child_with_entity_ref.text = 'Questo & Quello'

print(tostring(top))

