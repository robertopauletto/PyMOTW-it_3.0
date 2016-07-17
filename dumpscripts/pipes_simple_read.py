#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pipes
import tempfile

# Si predispone una pipeline molto semplice usando stdio
p = pipes.Template()
p.append('cat -', '--')
p.debug(True)

# Si imposta un file di input 
t = tempfile.NamedTemporaryFile(mode='w')
t.write('Porzione di testo')
t.flush()

# Si passa del testo attraverso la pipeline,
# salvando l'output in un file temporaneo
f = p.open(t.name, 'r')
try:
    contents = f.read()
finally:
    f.close()

print contents
