#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pipes
import pprint
import tempfile

p = pipes.Template()
p.append('cd "$WORKON_HOME"; for f in */bin/activate; do echo $f; done', '--')
p.append(r"sed 's|^\./||'", '--')
p.append("sed 's|/bin/activate||'", '--')
p.append('sort', '--')

t = tempfile.NamedTemporaryFile('r')

f = p.open(t.name, 'r')
try:
    sandboxes = [ l.strip() for l in f.readlines() ]
finally:
    f.close()

print 'SANDBOXES:'
pprint.pprint(sandboxes)
