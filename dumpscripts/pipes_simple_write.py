#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pipes
import tempfile

# Si predispone una pipeline molto semplice usando stdio
p = pipes.Template()
p.append('cat -', '--')
p.debug(True)

# Si passa del testo attraverso la pipeline,
# salvando l'output in un file temporaneo
t = tempfile.NamedTemporaryFile(mode='r')
f = p.open(t.name, 'w')
try:
    f.write('Porzione di testo')
finally:
    f.close()

# Ritorno ad inizio file e lettura del testo scritto
# nel file temporaneo
t.seek(0)
print t.read()
t.close()
