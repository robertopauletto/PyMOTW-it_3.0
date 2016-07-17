#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import collections

Persona = collections.namedtuple('Persona', 'nome anni genere')

print 'Tipo di Persona:', type(Persona)

bob = Persona(nome='Bob', anni=30, genere='maschio')
print 'Rappresentazione:', bob

jane = Persona(nome='Jane', anni=29, genere='femmina')
print '\nCampo riferito da indice:', jane.nome

print '\nCampi riferiti da indice:'
for p in [ bob, jane ]:
    print '%s ha %d anni, %s' % p